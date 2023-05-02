from Player_Atk import All_Attacks
from PLAYERZ import PInfo
Atknum = 0
atk_max = 3
try:
	atk_lv = PInfo.atklv
except AttributeError:
	atk_lv = PInfo.atklv_start
	
while atk_max >= Atknum and atk_lv >= 1:
#Null
	if Atknum == 0:
		AtkNam = "Null"
		atknum = 0
		Atknum += 1
#Punch
	if Atknum == 1:
		AtkNam = All_Attacks.Punch.atkNam
		print(str(Atknum) + "." + str(AtkNam))
		Atknum += 1
#Tackle
	if Atknum == 2:
		AtkNam = All_Attacks.Tackle.atkNam
		print(str(Atknum) + "." + str(AtkNam))
		Atknum += 1
#Sneeze
	if Atknum == 3:
		AtkNam = All_Attacks.Sneeze.atkNam
		print(str(Atknum) + "." + str(AtkNam))
		Atknum += 1