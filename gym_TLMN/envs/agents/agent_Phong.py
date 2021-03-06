from ..base.player import Player
import random
from colorama import Fore, Style
import json
import numpy as np

# print(card.card_type)  # đang bị lỗi
class Agent(Player):
    def __init__(self, name):
        super().__init__(name)
    def action(self, dict_input):
        t = self.get_list_state(dict_input)

        #Tạo một list các lá bài ở trong tay
        dict_card = {}
        for card in dict_input['Turn_player_cards']:
            dict_card[card] = card.score
        dict_card = dict(sorted(dict_card.items(), key = lambda item:item[1]))

        list_sc_dict = list(dict_card.values())
        list_sc = list(set(list_sc_dict) - set(x for x in list_sc_dict if list_sc_dict.count(x) > 1))
        list_sc_copy = list_sc.copy()
        
        #tìm bài lẻ ở trên bàn
        if 12 in list_sc_copy:
            list_sc_copy.remove(12)
        for score in list_sc_copy:
            if (score+1 in list_sc_dict) and (score+2 in list_sc_dict):
                list_sc.remove(score)
            elif (score+1 in list_sc_dict) and (score-1 in list_sc_dict):
                list_sc.remove(score) 
            elif (score-1 in list_sc_dict) and (score-2 in list_sc_dict):
                list_sc.remove(score)

        #Nếu khởi đầu vòng mới có nhiều lá bài lẻ thì đánh lá nhỏ nhất
        action_space = self.action_space(dict_input['Turn_player_cards'], dict_input['Board'].turn_cards, dict_input['Board'].turn_cards_owner)
        if t[114] == 0:
          #  # print(Fore.LIGHTYELLOW_EX + 'Phong khởi đầu vòng mới')
            if len(list_sc) > 1:
                for card in dict_card:
                    if card.score in list_sc:
                        return [card]

        #Đánh bộ có nhiều quân nhất ở trên tay(bộ có thể đánh)
        action = action_space[list(action_space.keys())[-1]][0]
        list_card_action = action['list_card']
        len_list_card = len(list_card_action)
        for id in range(len(action_space)):
            if len_list_card < len(action_space[list(action_space.keys())[id]][0]['list_card']):
                action = action_space[list(action_space.keys())[id]][0]
                list_card_action = action['list_card']
                len_list_card = len(list_card_action)
                
        #Nếu chặt một lá thì đánh lá bài có giá trị thấp nhất
        for card in dict_card:
            if len(list_card_action) == 1:
                if card.score in list_sc:
                    if list_card_action[0].score == card.score:
                        if list_card_action[0].stt > card.stt:
                            return [card]
        #Check Victory
        self.check_vtr(dict_input)
        return list_card_action

    def check_vtr(self, dict_input):
        victory = self.check_victory(self.get_list_state(dict_input))
        if victory == 1:
          #  # print(self.name, 'Thắng')
            pass
        elif victory == 0:
          #  # print(self.name, 'Thua')
            pass