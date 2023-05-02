P = 0
def rename():
	print("Name you character")
	name = input()
	P += 0
if P <= 0:
	print("Name you character")
	name = input()

BC = 0
lv_start = 0
hplv_start = 1
atklv_start = 1
mplv_start = 1
mp_max_start = 10
Ulv_start = 0
P_res_start = 0
B_res_start = 0
F_res_start = 0
try:
	from PLAYERZ import Player
	P_max = Player.P_max
	MP = Player.Mana
except ModuleNotFoundError:
	BC += 1


if BC == 1:
	import main
	from PLAYERZ import Player
	P_max = Player.P_max
	MP = Player.Mana

	name = name

	lv = main.lv
	hplv = main.hplv

	atklv = main.atklv
	mplv = main.mplv
	mp_max = main.mp_max

	Ulv = main.Ulv

	P_res = main.P_res
	B_res = main.B_res
	F_res = main.F.res
	from Encounter import One_V_One_Battle
	
	BC = One_V_One_Battle.Battle_Count
	print(BC)