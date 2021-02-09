import gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical
import numpy as np
import random

env = gym.make("CartPole-v1")
learning_rate = 0.002
sample_batch_size = 32
gamma = 0.98



class Qnet(nn.Module):
    def __init__(self):
        super(Qnet,self).__init__()
        self.memory = []
        # self.model = self.forward()

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

    def put_data(self, action, reward,  done):
        self.memory.append([action, reward, done])

    def train(self):
        if len(self.memory) < sample_batch_size:
           return 
        self.optimizer.zero_grad()
        loss = nn.MSELoss()
        sample_batch = random.sample(self.memory, sample_batch_size)
        for action, reward, done in sample_batch:
            target = reward
            if not done:
                target = reward + gamma * np.amax(self.memory[:][1])
            # print(reward)
            # print(target)
            # [(1, 1.0,  False)]
            # loss = nn.MSELoss(reward, torch.tensor(target))
            output = torch.tensor((target - reward) ** 2, requires_grad= True)
            output.backward()
            self.optimizer.step()


Qn = Qnet()
score = 0.0



for n_epi in range(10000):
    state = env.reset()
    eps = max(0.01, 0.08-0.01*(n_epi/10000))
    done = False
    while not done:
        state = torch.tensor(state, dtype = torch.float)
        if n_epi% 500 == 0 and n_epi :
            env.render()
        # if score > 175:
        #     render_option = True

        # if render_option:
        #     env.render()
        action = Qn.sample_action(state, eps)
        
        new_state, reward, done, __ = env.step(action)       
        if done:
            break
        score += reward
        Qn.put_data(action, reward, done)
        state = new_state

    Qn.train()
    if n_epi%20 ==0 and n_epi !=0:
        print("# of episode :{}, Avg score : {}".format(n_epi, score/20))
        score = 0
    
    
env.close()



