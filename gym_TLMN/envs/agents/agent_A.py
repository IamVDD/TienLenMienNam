from ..base.player import Player
import random
from colorama import Fore, Style
import json
import os
import numpy as np
path = os.path.dirname(os.path.abspath(__file__)) + "/"
np.seterr(divide='ignore', invalid='ignore')


class Agent(Player):
    sequences_value = np.load(path+"sequences_value.npy")
    sequences_times = np.load(path+"sequences_times.npy")
    def __init__(self, name):
        super().__init__(name)
        self.actions = []


    def action(self, dict_input):
        State = self.get_list_state(dict_input)
        list_action = self.get_list_index_action(State)
        action = random.choice(list_action)
        if len(self.actions) == 0:
            pass
        else:
            result_ =  np.nan_to_num(Agent.sequences_value/Agent.sequences_times, nan=-1, posinf=-1, neginf=-1)
            use = result_[self.actions[-1]]
            max_expected = 0
            for act in list_action:
                if use[act] > max_expected:
                    action = act
                    max_expected = use[act]
        self.actions.append(action)
        winning = self.check_victory(State)
        if winning != -1:
            try:
                sequences_value = np.load(path+"sequences_value.npy")
            except:
                sequences_value = [[0 for _ in range(self.amount_action_space)] for _ in range(self.amount_action_space)]
            try:
                sequences_times = np.load(path+"sequences_times.npy")
            except:
                sequences_times = [[0 for _ in range(self.amount_action_space)] for _ in range(self.amount_action_space)]
            for id_act in range(len(self.actions)-1):
                old_act = self.actions[id_act]
                new_act = self.actions[id_act+1]
                sequences_value[old_act][new_act] += winning
                sequences_times[old_act][new_act] += 1
            with open(path+'sequences_value.npy', 'wb') as f:
                np.save(f, sequences_value)
            with open(path+'sequences_times.npy', 'wb') as f:
                np.save(f, sequences_times)
            self.actions = []
        return action