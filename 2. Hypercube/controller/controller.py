from rx import Observable
from rx.subjects import Subject
import redis
import os
import json
import random
import sys
import time
from datetime import datetime

import copy

TOPIC_CONSUME =  ('TOPIC_CONSUME' in os.environ and os.environ['TOPIC_CONSUME']) or "evolved-population-objects"
TOPIC_PRODUCE =  ('TOPIC_PRODUCE' in os.environ and os.environ['TOPIC_PRODUCE']) or "population-objects"

WORKER_HEARTBEAT_INTERVAL = 10

bandera = False

r = redis.StrictRedis(host=os.environ['REDIS_HOST'], port=6379, db=0)
#r = redis.Redis(host='localhost', port=6379, db=0)

redis_ready = False 
while not redis_ready:
    try:
        redis_ready = r.ping()
    except:
        print("waiting for redis")
        time.sleep(3)
    
print("redis alive")




class DockerExperiment():
    def __init__(self, env):
        self.counter = 0
        self.state = "work"
        self.env = env
        self.problem_id = env["problem"]["problem_id"]
        self.consumed_messages = Subject()
        self.messages = Subject()
        self.population_objects_topic = "population-objects"
        self.valid_messages = self.consumed_messages\
                               .filter(lambda x: x["problem"]["problem_id"] == self.problem_id) \
                               .take(env["problem"]["max_iterations"]).publish()
            
        self.valid_messages.buffer_with_count(8)\
                            .subscribe( on_next=lambda x : self.population_mixer(x), on_completed = self.finish)

        self.valid_messages.subscribe(lambda message: self.one_more(message), on_completed = lambda : print("MESSAGES COMPLETED"))
        #self.valid_messages.subscribe(lambda message: self.log_to_redis_coco(message), on_completed = lambda : print("MESSAGES COMPLETED"))
        self.valid_messages.connect()

        self.messages.publish()
        self.messages.subscribe(lambda populations : self.produce(populations), on_completed = lambda : print("MESSAGES COMPLETED") )


    def one_more(self, message):
        #print(message)
        print('CONSUMED:{}, Max {}'.format(self.counter, self.env["problem"]["max_iterations"]))
        self.counter+=1
        self.log_to_redis_coco(message)
        if 'best_score' in message and message["problem"]["problem_id"] == self.problem_id:
            error = abs(message['best_score']-message["fopt"])
            print ('Best:{}, Fopt {}, Error {}'.format( message['best_score'], message["fopt"], error  ))
            
            if 1e-8 >= error:
                self.finish()


        

    def finish(self):

        print("Consume Finished")
        self.state = "stop"
        self.consumed_messages.on_completed()
        self.messages.on_completed()
        #self.messages.dispose() # not needed? Raised an exception
        #sys.exit(0)



        

    def population_mixer(self, populations):
        if len(populations) == 8:
            print("MIXER:",len(populations))
            #populations = [json.loads(message.data) for message in populations]contr
            #populations[0]['population'] = cxBestFromEach(populations[0]['population'], populations[1]['population'])
            #populations[1]['population'] = cxBestFromEach(populations[1]['population'], populations[2]['population'])
            #populations[2]['population'] = cxBestFromEach(populations[2]['population'], populations[0]['population'])

            populations[0]['population'], populations[1]['population'], populations[2]['population'], populations[3]['population'], populations[4]['population'], populations[5]['population'], populations[6]['population'], populations[7]['population'] = merge_hypercube_v1(populations[0]['population'], populations[1]['population'],populations[2]['population'],populations[3]['population'],populations[4]['population'],populations[5]['population'],populations[6]['population'],populations[7]['population'])

            #Iteracion hay que saber si sera el unico metodo o necesito otro
            #habra bandera para primera optimizacion?
            #deberian optimizarse 2 veces?
            #cxBestFromEach de donde viene?
            

            # I can´t fo map(...on_next, populations )
            self.messages.on_next(populations[0])
            self.messages.on_next(populations[1])
            self.messages.on_next(populations[2])
            self.messages.on_next(populations[3])
            self.messages.on_next(populations[4])
            self.messages.on_next(populations[5])
            self.messages.on_next(populations[6])
            self.messages.on_next(populations[7])
            
        
    
    def read_from_queue(self):
        while self.state == 'work':
            print('working')
            data = None
            # if we need a QUEUE we use blpop
            # we can also use a STACK with brpop
            message =  r.blpop(TOPIC_CONSUME, 2)
            if not message:
                print("NO DATA, WAITING...")
                time.sleep(2)                 
            else:
                data = message[1]
                
                pop_dict = json.loads(data)
        
                print("message read from queue")
               
                self.consumed_messages.on_next(pop_dict)
        
        return self.problem_id

               

    def produce(self, population):
        print("pop sent:", "population")
        json_data = json.dumps(population)
        # Data must be a bytestring
        message = json_data.encode('utf-8')
        ack = r.rpush(TOPIC_PRODUCE, message)
        print("Produce:", ack)

    def log_to_redis_coco(self, population):
        log_name =  "log:swarm"
        r.rpush(log_name, json.dumps(self.get_benchmark_data(population)))




    def get_benchmark_data(self, population):
        #print("\n\npopulation\n\n", population)
        return {
                "time_stamp": datetime.timestamp(datetime.now()) , 
                "evals": population["iterations"],
                "instance":population["problem"]["instance"],
                "worker_id":population["worker_id"],
                "params":{"sample_size":population["population_size"],
                        "init":"random:[-5,5]",
                        "NGEN":population["params"]["GA"]["iterations"]
                        },
                "experiment_id":population['experiment']["experiment_id"],
                "algorithm":population["algorithm"],
                "alg_params":population["params"][population["algorithm"]],

                "dim":population["problem"]["dim"],
                "benchmark":population["problem"]["function"],
                "fopt":population["fopt"],
                "message_counter": self.counter,
                "message_id":population["message_id"],
                "best_score": ("best_score" in population and population["best_score"]) or None }


def cxBestFromEach(pop1, pop2, key = lambda p: p['fitness']['score']):
    # small is better
    pop1.sort(key=key)
    pop2.sort(key=key)
    size = min(len(pop1), len(pop2))

    cxpoint = (size - 1) // 2

    pop1[cxpoint:] = pop2[:cxpoint+2]
    return pop1

def merge_chain_simple(pop1, pop2, pop3, key = lambda p: p['fitness']['score']):
    pl1 = len(pop1)
    pl2 = len(pop2)
    pl3 = len(pop3)

    pop1.sort(key=key)
    pop2.sort(key=key)
    pop3.sort(key=key)

    aux_p1 = copy.deepcopy(pop1[:10])
    aux_p2 = copy.deepcopy(pop2[:10])
    aux_p3 = copy.deepcopy(pop3[:10])

    print('Aqui se copiaron los primero 10 elementos de cada una')

    pop1[:10] = aux_p2
    pop2[:10] = aux_p3
    pop3[:10] = aux_p1
    
    print('aqui se combinaron las 3 poblaciones')

   
    return (pop1, pop2, pop3)

def merge_hypercube_v1(pop1, pop2, pop3, pop4, pop5, pop6, pop7, pop8, key= lambda p: p['fitness']['score']):
    percernt = int((len(pop1))*(.10))
    print('--------------------')
    print('--------------------')
    print('--------------------')
    print(percernt)
    print('--------------------')
    print('--------------------')
    print('--------------------')
    
    #Grupo 1
    pop1.sort(key=key)
    pop2.sort(key=key)
    pop3.sort(key=key)
    pop4.sort(key=key)

    #Grupo 2
    pop5.sort(key=key)
    pop6.sort(key=key)
    pop7.sort(key=key)
    pop8.sort(key=key)


    aux_p1 = copy.deepcopy(pop1[:percernt])
    aux_p2 = copy.deepcopy(pop2[:percernt])
    aux_p3 = copy.deepcopy(pop3[:percernt])
    aux_p4 = copy.deepcopy(pop4[:percernt])
    aux_p5 = copy.deepcopy(pop5[:percernt])
    aux_p6 = copy.deepcopy(pop6[:percernt])
    aux_p7 = copy.deepcopy(pop7[:percernt])
    aux_p8 = copy.deepcopy(pop8[:percernt])

    global bandera
    if bandera == False:
        #Los cambios seran internos entre grupos
        #Cambios grupo 1
        print('********************')
        print('********************')
        print('********************')
        print('Fase 1')
        print('********************')
        print('********************')
        print('********************')
        pop1[:percernt] = aux_p4
        pop2[:percernt] = aux_p1
        pop3[:percernt] = aux_p2
        pop4[:percernt] = aux_p3

        #Cambios grupo 2
        pop5[:percernt] = aux_p8
        pop6[:percernt] = aux_p5
        pop7[:percernt] = aux_p6
        pop8[:percernt] = aux_p7

        
    else: 
        #Los cambios seran externos entre grupos
        print('********************')
        print('********************')
        print('********************')
        print('Fase 2')
        print('********************')
        print('********************')
        print('********************')
        pop1[:percernt] = aux_p5
        pop2[:percernt] = aux_p6
        pop3[:percernt] = aux_p7
        pop4[:percernt] = aux_p8
        pop5[:percernt] = aux_p1
        pop6[:percernt] = aux_p2
        pop7[:percernt] = aux_p3
        pop8[:percernt] = aux_p4

    bandera = not bandera

    return(pop1, pop2, pop3, pop4, pop5, pop6, pop7, pop8)





def pull_experiment(time_out=WORKER_HEARTBEAT_INTERVAL):
        #Pop task from queue
        #This is a blocking operation
        #task is a tuple (queue_name, task_id)
        message = r.blpop("experiment_queue", time_out)
        if message:
            config_json = message[1]
            config = json.loads(config_json)

            return config
    
        else:
            return ""


if __name__ == "__main__":
    while True:
        print("pulling")
        t = pull_experiment()
        if (t):
            print("DockerExp env", t)
            problemid = DockerExperiment(t).read_from_queue()
            print(problemid, "Done")
            r.rpush("experiment_finished", problemid)
        else:
            print("waiting for experiment")




#DockerExperiment({"problem":{"max_iterations":100}})
#time.sleep(4)


