from gym_TLMN.envs.agents import Phong as p1
from gym_TLMN.envs.agents import Phong_cu as p2
from gym_TLMN.envs.agents import random as p3
from gym_TLMN.envs.agents import random as p4

# from gym_TLMN.envs.agents import agent_random as p1
# from gym_TLMN.envs.agents import agent_random as p2
# from gym_TLMN.envs.agents import agent_random as p3
# from gym_TLMN.envs.agents import agent_random as p4

agent1 = p1.Agent('Phong')
agent2 = p2.Agent('Phong_Cu')
agent3 = p3.Agent('Nam')
agent4 = p4.Agent('Bắc')

list_player = [agent1, agent2, agent3, agent4]