import simpy
import numpy as np

def generate_interarrival():

    return np.random.exponential(1./3.0) 

def generate_service(): 
    
    return np.random.exponential(1./4.0) 

def cafe_run(env, servers):
    i = 0
    while True:
        i+=1
        intensity = i/4
        traffic.append(intensity)
        traffic_in = traffic.pop()
        print(" ")
        print("The traffic intensity at time ", env.now, "is: ", traffic_in)
        
        yield env.timeout(generate_interarrival())
        env.process(customer(env, i, servers))

service_t = []
traffic = []
        
def customer(env, customer, servers):
    with servers.request() as request: 
        t_arrival = env.now
        print ("At time ", env.now, "customer {} arrives".format(customer))
        yield request
        
        print ("At time ", env.now, "customer {} is being served".format(customer))
        yield env.timeout(generate_service())
        
        print ("At time ", env.now, "customer {} departs".format(customer))
        t_depart = env.now
        service_t.append(t_depart - t_arrival)

        print ( "Service time for each customer so far: ", service_t)
        
        
        print(" ")
        

np.random.seed(0)


env = simpy.Environment()

servers = simpy.Resource(env, capacity=1) 

env.process(cafe_run(env, servers))
"""the simulation run time"""
env.run(until=4)
