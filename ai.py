import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations_with_replacement


LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 500
SHOW_EVERY = 50
#training proportions
intensities={'steady state':34,
             'Aerobic thershold':33,
             'Anaerobic':33}

ind={1:'steady state',
     2:'Aerobic thershold',
     3:'Anaerobic'}

#Fake 2km times
#480=8 mins
times = list()
for i in range(60):
    times.append(480-i)
for i in range(60,70):
    times.append(480-(i*2))
for i in range(70,80):
    times.append(480-(i*3))
for i in reversed(range(80,101)):
    times.append(480-i*1.5)

plt.plot(times)
plt.xlabel('percentage')
plt.ylabel('Time (secs)')


#Function to get seconds of improvement the athlete made
#given the agents determination of the intensities (Steady state,aerobic thershold, anerobic)
def get_split_diff(state,new_state):
    diff=(times[new_state[2]]-times[state[2]])/100
    if diff >=0:
        diff = -1
    else:
        diff=-1*diff

    return diff

#This is a map of whether to increase,decrease or neither to the intensities.
q_table=np.random.uniform(low=-2, high=0, size=(101,101,101,8))



def do_action(state, actions,episode):
    div=len(intensities)-1
    action=actions//div
    subaction=(actions%div)+1
    new_state=list()
    
    if subaction>=action:
        subaction+=1
 
    #do nothing
    if action==0:
        if episode % SHOW_EVERY==0:
            print(f"Intensities are not changed, {intensities}")
            
        reward=get_split_diff(state,state)
        return state, reward
   
    #Update system
    elif intensities[ind[action]]<100 and intensities[ind[subaction]]>0 :
        intensities[ind[action]]+=1
        intensities[ind[subaction]]-=1
        for i in range(len(intensities)):
            if i==(action-1):
                new_state.append(state[i]+1)
            elif i==(subaction-1):
                new_state.append(state[i]-1)
            else:
                new_state.append(state[i])
        
        if episode % SHOW_EVERY==0:
            print(f"{ind[action]} is increased, {ind[subaction]} is decreased")
            print(f"The intensities are {intensities}")
            
        reward=get_split_diff(state,new_state)
        return tuple(new_state), reward  

#For loop
state=tuple([34,33,33])
for episode in range (EPISODES):
    action=np.argmax(q_table[state])
    new_state, reward=do_action(state, action,episode)
    if reward >0:
        new_q=reward
    else:
        max_future_q = np.amax(q_table[new_state])
        current_q = q_table[state +(action, )]
        new_q = (1-LEARNING_RATE) * current_q + LEARNING_RATE + (reward + DISCOUNT * max_future_q)
    q_table[state+(action, )] = new_q
    
    if episode % SHOW_EVERY==0:
        print(f"Episode: {episode}")
        
    state=new_state
