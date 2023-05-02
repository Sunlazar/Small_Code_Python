from Location import Player_Location
from random import choice
from Enemy_Info import All_Enemies


if Player_Location.local == 1:
	#FOREST ENEMIES
	Enemies = [1,1,1,1]
	Enemy_Choice = choice(Enemies)

	#SHRUB-LORD(Forest)
	if Enemy_Choice == 1:
		
		name = All_Enemies.Shrub.name
		Intro = All_Enemies.Shrub.Intro
		Sdmg = All_Enemies.Shrub.Sdmg
		Ndmg = All_Enemies.Shrub.Ndmg
		Wdmg = All_Enemies.Shrub.Wdmg
		
		B_max = All_Enemies.Shrub.B_max
		mult = All_Enemies.Shrub.mult
		exp = All_Enemies.Shrub.exp
		
		atk1 = All_Enemies.Shrub.atk1		
		atk2 = All_Enemies.Shrub.atk2		
		atk3 = All_Enemies.Shrub.atk3
		atk4 = All_Enemies.Shrub.atk4
		effect = All_Enemies.Shrub . effect
		atk5 = All_Enemies.Shrub.atk5
		atkboost = All_Enemies.Shrub.atkboost
		BC_min = All_Enemies.Shrub.BC_min

		P_res = All_Enemies.Shrub.P_res
		B_res = All_Enemies.Shrub.B_res
		F_res = All_Enemies.Shrub.F_res
		
	#GOJANGO(Forest)
	elif Enemy_Choice == 2:
		name = All_Enemies.Gojango.name
		Intro = All_Enemies.Gojango.Intro
		Sdmg = All_Enemies.Gojango.Sdmg
		Ndmg = All_Enemies.Gojango.Ndmg
		Wdmg = All_Enemies.Gojango.Wdmg
		
		B_max = All_Enemies.Gojango.B_max
		mult = All_Enemies.Gojango.mult
		exp = All_Enemies.Gojango.exp
		
		atk1 = All_Enemies.Gojango.atk1		
		atk2 = All_Enemies.Gojango.atk2		
		atk3 = All_Enemies.Gojango.atk3
		atk4 = All_Enemies.Gojango.atk4
		effect = All_Enemies.Gojango.effect
		atk5 = All_Enemies.Gojango.atk5
		atkboost = All_Enemies.Gojango.atkboost
		BC_min = All_Enemies.Gojango.BC_min

		P_res = All_Enemies.Gojango.P_res
		B_res = All_Enemies.Gojango.B_res
		F_res = All_Enemies.Gojango.F_res