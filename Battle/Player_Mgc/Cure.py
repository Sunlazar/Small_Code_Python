from random import choice
from PLAYERZ import Player

#CURE
Mana_Cost = (Player.mp_max/2)
Mana_Up = 0

mgc_num = 2
mgc_Nam = "Cure"
Req_MLV = 1

mult = [1,1,1,1,1]
dmg = 0
Max_dmg = 1

heal =[1,1,2,2,3]
mult = choice(heal)

hp_rec = int(mult/10)
patk_up = 0
matk_up = 0
def_up = 0

poison = 0
burn = 1
frost = 0

type = 0