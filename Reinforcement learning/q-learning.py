import gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical
import numpy as np
import random

env = gym.make("CartPole-v1")
learning_rate = 0.05
gamma = 0.98



class Qnet(nn.Module):
    def __init__(self):
        super(Qnet,self).__init__()
        self.memory = []
        # self.state_lst ,self.action_lst , self.reward_lst, self.new_state_lst, self.done_mask = [], [], [], [], []

        self.fc1 = nn.Linear(4,128)
        self.fc2 = nn.Linear(128,128)
        self.fc3 = nn.Linear(128,2)
        self.optimizer = optim.Adam(self.parameters(), lr = learning_rate)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def sample_action(self, obs, epsilon):
        out = self.forward(obs)
        coin = random.random() 
        if coin < epsilon:
            return random.randint(0,1)
        else:
            return out.argmax().item()

    def put_data(self, x):
        self.memory.append(x)

    def sample(self):
        s_lst, a_lst, r_lst, s_prime_lst, done_mask_lst = [], [], [], [], []
        
        for transition in self.memory:
            s, a, r, s_prime, done_mask = transition
            s_lst.append(s)
            a_lst.append([a])
            r_lst.append([r])
            s_prime_lst.append(s_prime)
            done_mask_lst.append([done_mask])

        return torch.tensor(s_lst, dtype=torch.float), torch.tensor(a_lst),torch.tensor(r_lst), torch.tensor(s_prime_lst, dtype=torch.float), torch.tensor(done_mask_lst)



    def train(self):
        self.optimizer.zero_grad()
        loss = nn.MSELoss()
        state,action,reward,next_state,done_mask = self.sample()
        out = self.forward(state).gather(1,action)
        max_q_prime = torch.max(self.forward(next_state))
        target = reward + gamma * max_q_prime* done_mask
        output = loss(out, target)
        output.backward()
        self.optimizer.step()
        self.memory = []
            


Qn = Qnet()
score = 0.0



for n_epi in range(10000):
    state = env.reset()
    eps = max(0.01, 0.08-0.01*(n_epi/10000))
    done = False
    while not done:
        action = Qn.sample_action(torch.tensor(state, dtype = torch.float), eps)
        
        new_state, reward, done, __ = env.step(action)   
        done_mask = 0.0 if done else 1.0    
        if done:
            break
        score += reward
        Qn.put_data((state, action, reward/100.0, new_state, done_mask))
        state = new_state
    Qn.train()
    if n_epi%20 ==0 and n_epi !=0:
        print("# of episode :{}, Avg score : {}".format(n_epi, score/20))
        score = 0
    
    
env.close()