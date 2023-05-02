from random import choice
import time
import os
import importlib
ULV = 0
Battle_Count = 0
from PLAYERZ import PInfo
from PLAYERZ import Player
from Encounter import Enemy_choice

def clear():
	os.system("cls")

class Being:
	def __init__(Being, name, dmg, attack, atkMult, Total_HP_Bar):
		Being.name = name
		Being.dmg = dmg
		Being.attack = attack
		Being.atkMult = atkMult
		Being.Total_HP_Bar = Total_HP_Bar
		
	def HP_BarCheck(Being):
		print(Being.name + " Health: " + str(Being.Total_HP_Bar - Being.dmg) + "\n")

	def Recover(Being):
		if Being.dmg >> 0:
			print("Working")
			Being.dmg = Being.dmg - ( Being.Total_HP_Bar /5 )
			print(str(Being.name) + " recoverd health\n")
		elif Being.dmg <= 0:
			print( str(Being.name) + "'s health is full\n")
			Being.dmg = 0

	def Attack(Being):
		Being.attack * Being.atkMult

Player_name = PInfo.name     
Enemy_name = Enemy_choice.name

P_dmg = 0
B_dmg = 0
PhpC = True
BhpC = False

Focus_Count = 0
BFocus_Count = 0
Boost = 0

pp = 0
bb = 0

M_lv = 0
Mana = PInfo.MP
B_Charge = 0

recnum = 0

B_max = Enemy_choice.B_max
P_max = PInfo.P_max 

P_Exp = 0

#ATK
B_atk = choice(Enemy_choice.Ndmg)

clear()
print(PInfo.name + " encountered " + Enemy_choice.Intro)
input()
B_Complete = False
B_count = 0

#Poison
Pp_Count = 0
P_Poison = False
Pe_Count = 0
E_Poison = False

#Frost
Frp_Count = 0
P_Freeze = False
Fre_Count = 0
E_Freeze = False
#Burn
Bup_Count = 0
P_Burn = False
Bue_Count = 0
E_Burn = False

while B_Complete == False:
	#PlayerZ's turn
	if P_dmg>= P_max:
		Battle_Complete = True
		Victory = False
		break
	clear()
	if Focus_Count >= 1:
		from Menu import Main_menu
		clear()
		PhpC = True

		Focus_Count -= 1
		print(Player_name + " is " + Enemy_choice.effect)
		time.sleep(3)
		input()
	#User ATTACK--------
	elif Focus_Count == 0:
		PhpC = True
		try:
			from Menu import Main_menu
			clear()
			#Health Bar
			if P_Poison == True:
				print("P")
			hp = P_max - P_dmg
			from PLAYERZ import HP_BAR
			clear()
			if PhpC == True:
				importlib.reload(HP_BAR)
			elif PhpC == False:
				importlib.close(HP_BAR)
			print("What should " +  Player_name +" do?")
			importlib.reload(Main_menu)
			UserChoice = int(input())

		except ValueError:
			clear()
			input("That is not a option please try again")
			continue
		if UserChoice == 1:
			try:
				clear()
				from Menu import Atk_menu
				clear()
				importlib.reload(Atk_menu)
				Atknum = int(input())
			except ValueError:
				clear()
				input("That is not a option please try again")
				continue

			from PLAYERZ import Patk_Choice
			clear()
			importlib.reload(Patk_Choice)
			#---Attack---#
			if Atknum == Patk_Choice.atknum:
				clear()
				print(Player_name + " used " + Patk_Choice.AtkNam)
				time.sleep(3)
				M_dmg = Patk_Choice.atk	
				 #MULT
				atkMult = Patk_Choice.mult
				#DAMAGE_CHECK
				M_dmg_dmg = (M_dmg * atkMult)
				B_dmg += M_dmg_dmg
				#CRITS!!
				crit = Patk_Choice.Critatk
				if M_dmg_dmg >= crit:
					clear()
					print("CRIT!!")
					if M_dmg_dmg >= crit*2:
						clear()
						print("SUPER CRIT!!")
					if M_dmg_dmg >= crit*4:
						clear()
						print("ULTRA CRIT!!")
					time.sleep(3)
					if Patk_Choice.burn >> 1:
						print(Enemy_name + " took "  + str(Patk_Choice.burn * atkMult) + " burn damage")
						B_dmg += (Patk_Choice.burn * atkMult)
					if Patk_Choice.frost <= 0:
						frost = Patk_Choice.frost
						BFocus_Count += frost
					if Patk_Choice.poison >= 1 and Patk_Choice.P == True:
						E_Poison = Patk_Choice.P
						Pe_Count += Patk_Choice.P_Count
					elif Patk_Choice.frost >> Enemy_choice.F_res:
						Frost_stall = print("Can't be stunned anymore")
					elif Patk_Choice.frost >> 0:
						BFocus_Count += 1
				elif 0 >= M_dmg_dmg:
					print(Player_name + " MISSED!!")
					time.sleep(3)
					clear()
				print(Player_name + " did " + str(M_dmg_dmg) + " dmg")
				time.sleep(3)
				clear()
				#Being
				p_1 = Being (Player_name, P_dmg, M_dmg, atkMult, P_max)
				b_1 = Being(Enemy_name, B_dmg, B_atk,atkMult, B_max)
		if UserChoice == 2:
			print ("1.Vitals Viewer\n(Press any letter to go back)")
			try:
				clear()
				from Menu import Item_menu
				clear()
				importlib.reload(Item_menu)
				Item_Choice = int(input())
				#ITEMS
			except ValueError:	
				clear()
				input("That is not a option please try again")
				continue
			if Item_Choice == 1:
				print(Enemy_choice.name + " HP_Bar: " + str(B_max - B_dmg ) + "/" + str(B_max))
				print(Player_name + " HP_Bar: " + str(P_max - P_dmg ) + "/" + str(P_max))
				time.sleep(3)
				continue
		
		#User MAGIC----------------------------------
		if UserChoice == 3:
			try:
				clear()
				print("MP::" + str(Mana))
				from Menu import Mgc_menu
				clear()
				importlib.reload(Mgc_menu)
				Mgc_Choice = int(input())
			except ValueError:
				input("That is not a option please try again")
				continue
			#Magic
			from PLAYERZ import Pmgc_Choice
			clear()
			importlib.reload(Pmgc_Choice)
			if Player.mplv >= Pmgc_Choice.Req_MLV:
				print("mplv >= Req_MLV")
				if Mgc_Choice == Pmgc_Choice.mgc_num:
					clear()
					mgc_nam = Pmgc_Choice.mgc_nam
					print(Player_name + " used " + mgc_nam)
					time.sleep(3)
					M_dmg = Pmgc_Choice.dmg	
					 #MULT
					mgcMult = Pmgc_Choice.mult
					#DAMAGE_CHECK
					P_mgc_dmg = (M_dmg * mgcMult)
					B_dmg += P_mgc_dmg

					#Heals
					if Pmgc_Choice.hp_rec >> 0:
							P_dmg -= P_max * Pmgc_Choice.hp_rec
							print(str(Player_name) + " recovered " + str(P_max * Pmgc_Choice.hp_rec))
					#CRITS!!
					crit = Pmgc_Choice.Max_dmg
					if P_mgc_dmg >= crit:
						if P_mgc_dmg >= 10:
							clear()
							print("CRITICAL HIT!!")
							time.sleep(1)	
						#BURN!!
						if Pmgc_Choice.burn >= 1:
            	        #ADD A BOOLEAN!!!
							print(Enemy_name + " took "  + str(Pmgc_Choice.burn * mgcMult) + " burn damage")
							B_dmg += (Pmgc_Choice.burn * mgcMult)
						#FREEZE!!
						if Pmgc_Choice.frost <= 3:
						#Don't do that here
							frost = Pmgc_Choice.frost + 1
							BFocus_Count += frost
						#POISON!!
						if Pmgc_Choice.poison >> Enemy_choice.P_res:
							if Pmgc_Choice.poison >= 1:
							#POISON!!!
								print(Enemy_name + " took "  + str(Pmgc_Choice.poison) + " poison damage")
								B_dmg += (Pmgc_Choice.poison - Enemy_choice.P_res)
						elif Pmgc_Choice.poison <= Enemy_choice.P_res:
							print("It doesent affect " + Enemy_choice.name)
						elif Pmgc_Choice.frost >> Enemy_choice.F_res:
							Frost_stall = print("Can't be stunned anymore")
						elif Pmgc_Choice.frost >> 0:
							BFocus_Count += 1
					if 0 >= P_mgc_dmg:
						print(Player_name + " MISSED!!")
						time.sleep(3)
					if P_mgc_dmg >> 0:
						print(Player_name + " did " + str(P_mgc_dmg) + " dmg")
						time.sleep(3)
				clear()

			#Being
			p_1 = Being (Player_name, P_dmg, M_dmg, mgcMult, P_max)
			b_1 = Being(Enemy_name, B_dmg, B_atk,mgcMult, B_max)
			input()


		if UserChoice == 4:
			print("1.End PlayerZ\n2.End Enemy")
			try:
				Debug_Choice = int(input())
			except ValueError:
				input("That is not a option please try again")
				continue
				
			if Debug_Choice == 1:
				P_dmg = P_max
			elif Debug_Choice == 2:
				B_dmg = B_max
			clear()
	#______________________________________________________

	#Enemy's turn
	#Mision Failed we'll get 'em next time
	if B_dmg>= B_max:
		Battle_Complete = True
		Victory = True
		break
	clear()
	if BFocus_Count >= 1:
		BFocus_Count -= 1
		print(Enemy_name + " is too dazed to attack")
		time.sleep(3)
	elif BFocus_Count == 0:
		PhpC = False

		Sdmg = choice(Enemy_choice.Sdmg)
		Ndmg = choice(Enemy_choice.Ndmg)
		Wdmg = choice(Enemy_choice.Wdmg)
		clear()
		if B_Charge < Enemy_choice.BC_min:
			BossChoice =[1,1,1,1,2,2,2,3,3,4]
		elif B_Charge >= Enemy_choice.BC_min:
			BossChoice =[2,2,2,3,3,4,5,5,5,]
		BossAttack =choice(BossChoice)  
		print("The " + Enemy_name + " attacks\n")	

		time.sleep(3)
		clear()
	#--PUNCH--#
		if BossAttack == 1:
			#MULT
			atkMult = 1 +  Boost
			#ATK
			print(Enemy_name + " used " + Enemy_choice.atk1 )
			time.sleep(3)
			Player.atk = [6,7,10,10]
			M_dmg = choice(Player.atk)
			B_atk = choice(Enemy_choice.Ndmg)
			if B_atk == 0:
				print(Enemy_name + " missed")
			#DAMAGE CHECK
			P_dmg = P_dmg + (B_atk * atkMult)
	
		#Trick punch
		if BossAttack == 2:
			print(Enemy_name + " used " + Enemy_choice.atk2)
			print(Player_name + "\'s gaurd was lowered\n")
			time.sleep(3)
			Boost = Boost + 1
			#MULT
			atkMult = 1
			#ATK
			Player.atk = [3,4,7,7]
			M_dmg = choice(Player.atk)
			B_atk = 3	

			#DAMAGE CHECK
			P_dmg = P_dmg + (B_atk)	
			#Beings
			p_1 = Being (Player_name, P_dmg, M_dmg, atkMult, P_max)
			b_1 = Being(Enemy_name, B_dmg, B_atk, atkMult, B_max )
		#CHARGE
		if BossAttack == 3:
			print(Enemy_name + " charges...Something")
			time.sleep(3)
			B_Charge = B_Charge + 1
			Boost = Boost + 2
		#FOUCUS BREAKER
		if BossAttack == 4:
			Focus_Count = Focus_Count + 2
			#MULT
			atkMult = choice(Enemy_choice.mult) + Boost
			#ATK
			Player.atk = [6,7,10,10]
			M_dmg = choice(Player.atk)
			B_atk = choice(Enemy_choice.Sdmg)	

			#DAMAGE CHECK
			P_dmg = P_dmg + (B_atk * atkMult)

			#Beings
			p_1 = Being (Player_name, P_dmg, M_dmg, atkMult, P_max)
			b_1 = Being(Enemy_name, B_dmg, B_atk, atkMult, B_max )
			print(Enemy_name + " used " + Enemy_choice.atk4)
			time.sleep(3)
			Boost = Boost * 0
		elif BossAttack == 5:
			print(Enemy_name + " unleashed " + Enemy_choice.atk5)
			time.sleep(3)
			#MULT
			Emult = choice(Enemy_choice.mult)
			atkMult = Emult + Boost
			#ATK
			Player.atk = [6,7,10,10]
			M_dmg = choice(Player.atk)
			B_atk = Sdmg + Enemy_choice.atkboost

			#DAMAGE CHECK
			P_dmg = P_dmg + (B_atk * atkMult)	

			#Beings
			p_1 = Being (Player_name, P_dmg, M_dmg, atkMult, P_max)
			b_1 = Being(Enemy_name, B_dmg, B_atk, atkMult, B_max )
		if E_Poison == True or Pe_Count >= 1:
			print(Enemy_name + " is hurt by poison")
			time.sleep(3)
			Pe_Count -= Enemy_choice.P_res
			B_dmg += (Patk_Choice.poison - Enemy_choice.P_res)

		#MISC
		bb = bb + 1 
		clear()

		p_1.HP_BarCheck()
		time.sleep(3)
		clear()

	#The End
if Victory == True:
	input("You win (Perfect)")
	ULV = Enemy_choice.exp
	B_Complete = True
elif Victory == False:
	ULV = 0
	input("YOU LOSE\nYou get nothing!\nGooday sir")
	B_Complete = True
