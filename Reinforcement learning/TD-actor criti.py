import gym
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical


class ActorCritic(nn.Module):
    def __init__(self):
        super(ActorCritic, self).__init__()
        self.loss_1st = []
        
        self.fc1 = nn.Linear(4, 128)
        self.fc_pi = nn.Linear(128,2)
        self.fc_v = nn.Linear(128,1)
        self.optimizer = optim.Adam(self.parameters(), lr = 0.002)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        pol = self.fc_pi(x)
        pi = F.softmax(pol, dim = 0)
        v = self.fc_v(x)
        return pi, v
    
    def gather_loss(self, loss):
        self.loss_1st.append(loss.unsqueeze(0))

    def train(self):
        loss = torch.cat(self.loss_1st).sum()
        loss = loss/len(self.loss_1st)
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()
        self.loss_1st = []

env = gym.make("CartPole-v1")
model = ActorCritic()   
gamma = 0.98
score = 0.0

for n_epi in range(10000):
    obs = env.reset()

    for t in range(600):
        obs = torch.from_numpy(obs).float()
        pi, v = model(obs)
        m = Categorical(pi)
        action = m.sample()

        obs, r, done, info = env.step(action.item())
        _, next_v = model(torch.from_numpy(obs).float())
        delta = r*gamma * next_v - v
        loss = torch.log(pi[action]) + delta.item() +delta * delta
        model.gather_loss(loss)

        if done:
            break
        
        model.train()

