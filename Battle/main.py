import os
import time
import importlib
from PLAYERZ import PInfo
from PLAYERZ import Player
from random import choice

name = PInfo.name
def clear():
	os.system("cls")

Ulv = 0
Battle_num = PInfo.BC
def Level_Check():
	Battle_num = PInfo.BC
	input(str(Battle_num))
	#LEV    EL_UP
	if Battle_num <= 0:
		lv =PInfo.lv_start
		hplv = PInfo.hplv_start

		atklv = PInfo.atklv_start
		mplv = PInfo.mplv_start
		mp_max = PInfo.mp_max_start

		P_res = PInfo.P_res_start
		B_res = PInfo.B_res_start
		F_res = PInfo.F_res_start
	elif Battle_num >= 1:
		input("Oh My")
		try:
			ULV_Req = (20 + lv*10)
		except UnboundLocalError:
			input("Whoops")
			lv = 1
			ULV_Req = (20 + lv*10)
		Ulv = PInfo.Ulv
		if Ulv >= ULV_Req:
			print ("You Leveled Up")
			lv = lv + 1

			lv_choice = [1,1,1,2,2,2,3,3,5]

			lvnum = choice(lv_choice)
			atklv += lvnum
			print("Atk: +" + str(lvnum))
			lvnum = choice(lv_choice)
			hplv += lvnum
			print("HP: +" + str(lvnum))


			lvnum = choice(lv_choice)
			mplv += lvnum
			mp_max += lvnum
			print("MP: +" + str(lvnum))

			lvnum = choice(lv_choice)
			P_res += lvnum
			print("P_res: +" + str(lvnum))

			lvnum = choice(lv_choice)
			B_res += lvnum
			print("B_res: +" + str(lvnum))

			lvnum = choice(lv_choice)
			F_res += lvnum
			print("F_res: +" + str(lvnum))
	clear()
	print(name + " is level: " + str(lv))

def Level_Up():
	
	if Battle_num >= 0:
		input("Leveling up!!")
		try:
			ULV_Req = (20 + lv*10)
			Ulv = ULV_Req

		except UnboundLocalError:
			input("Whoopsie")
			lv = 1
			ULV_Req = (20 + lv*10)
			Ulv = ULV_Req
		lv =PInfo.lv_start
		hplv = PInfo.hplv_start

		atklv = PInfo.atklv_start
		mplv = PInfo.mplv_start
		mp_max = PInfo.mp_max_start

		P_res = PInfo.P_res_start
		B_res = PInfo.B_res_start
		F_res = PInfo.F_res_start

		if Ulv >= ULV_Req:
			print ("You Leveled Up")
			lv = lv + 1

			lv_choice = [1,1,1,2,2,2,3,3,5]

			lvnum = choice(lv_choice)
			atklv += lvnum
			print("Atk +" + str(lvnum))
			lvnum = choice(lv_choice)
			hplv += lvnum
			print("HP +" + str(lvnum))


			lvnum = choice(lv_choice)
			mplv += lvnum
			mp_max += lvnum
			print("MP +" + str(lvnum))

			lvnum = choice(lv_choice)
			P_res += lvnum
			print("P_res +" + str(lvnum))

			lvnum = choice(lv_choice)
			B_res += lvnum
			print("B_res +" + str(lvnum))

			lvnum = choice(lv_choice)
			F_res += lvnum
			print("F_res +" + str(lvnum))
			input()
			Ulv += 1

	clear()
	print(name + " is level: " + str(lv))
#FOREST-----------------------------------------
locChoice = 1
from Location import Player_Location
print(Player_Location.L_name)
def Fight():
	if PInfo.BC <= 1:
		ULV = 0
	B_Complete = False
	if B_Complete == False:
		from Encounter import One_V_One_Battle
		B_Complete = One_V_One_Battle.B_Complete
	if B_Complete == True:
		PInfo.BC += 1
		ULV += One_V_One_Battle.ULV
		input(str(ULV))
		Level_Check()
		print ("Battle Complete")

Level_Check()
input()
clear()
first_action = int(input("1.Level\n2.Fight\n3.Level Up\n"))
Test_count = 0
while Test_count <= 3:
	Test_count += 1
	if first_action == 1:
		Level_Check()
		input()
		continue

	if first_action == 2:
		Fight()
		input()
		continue
	
	if first_action == 3:
		Level_Up()
		input()
		continue

print ("Game Over")
Level_Check()
time.sleep(2)
clear()

print("-----NEW CONTENT SOON-----")