import gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical
import numpy as np
import random

env = gym.make("CartPole-v1")
learning_rate = 0.0001
gamma = 0.9



class Qnet(nn.Module):
    def __init__(self):
        super(Qnet,self).__init__()
        self.memory = []

        self.fc1 = nn.Linear(4,32)
        self.fc2 = nn.Linear(32,32)
        self.fc3 = nn.Linear(32,2)
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
        loss = nn.MSELoss()
        state,action,reward,next_state,done_mask = self.sample()
        out = self.forward(state)
        q_out = out.gather(1,action)
        max_q_prime = torch.max(self.forward(next_state))
        target = reward + gamma * max_q_prime* done_mask
        target.detach()
        output = loss(q_out, target)
        self.optimizer.zero_grad()
        output.backward()
        self.optimizer.step()
        self.memory = []
            


Qn = Qnet()
score = 0.0

for n_epi in range(10000):
    eps = max(0.01, 0.08-0.01*(n_epi/200))
    state = env.reset()
    done = False

    while not done:
        action = Qn.sample_action(torch.from_numpy(state).float(), eps)
        new_state, reward, done, __ = env.step(action)   
        done_mask = 0.0 if done else 1.0 
        Qn.put_data((state, action, reward/100.0, new_state, done_mask))
        state = new_state  
        score += reward 
        if done:
            break
        
        
    Qn.train()
    if n_epi%20 ==0 and n_epi !=0:
        print("# of episode :{}, Avg score : {:.1f}, eps : {:.1f}".format(n_epi, score/20, eps*100))
        score = 0.0
    
    
env.close()
#30에서 40정도 사이로 수렴
