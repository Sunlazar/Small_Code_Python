from random import choice
fcount = 0
BC = 0

#p_1 = Being (Player_name, P_dmg, P_atk, atkMult, P_max)

#LEVEL
lv = 1
atklv = 1
hplv = 1
atklv = 1
mplv = 1
mp_max = 10


Ulv = 0
Catk = [12,15,16,20]

P_res = 0
B_res = 0
F_res = 0


if BC <= 1:
	Mana = 10
	BC += 1
elif BC >> 1:
	from Encounter import One_V_One_Battle
	Ulv = Ulv + One_V_One_Battle.ULV
	Battle_count = One_V_One_Battle.Battle_Count
	BC = PInfo.BC
	from PLAYERZ import PInfo
	name = PInfo.name

Battle_count = 0
fcount = fcount + Battle_count
if fcount << 1:
	atk = choice(Catk)
	Mana  = 10
	P_max = 30
	critatk = 20


elif fcount >= 1:
	dmg = One_V_One_Battle.p_1.dmg
	Mana  = 10 + (5 * mplv)
	atk = choice(Catk) + (5 + atklv * 2)
	critatk = 20 + (5 + atklv * 3)
	P_Max = 30 + (5 * hplv)
