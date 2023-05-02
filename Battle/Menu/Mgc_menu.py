Mgc_num = 0
Mgc_max = 2
while Mgc_max >= Mgc_num:
#Null
	if Mgc_num == 0:
		Mgc_Nam = "Null"
		Mgc_num += 1
#Charge
	if Mgc_num == 1:
		Mgc_Nam = "Charge"
		print(str(Mgc_num) + "." + str(Mgc_Nam))
		Mgc_num += 1
#Cure
	if Mgc_num == 2:
		Mgc_Nam = "Cure"
		print(str(Mgc_num) + "." + str(Mgc_Nam))
		Mgc_num += 1
