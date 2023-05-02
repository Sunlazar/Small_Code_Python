Main_num = 0
Main_max = 4
while Main_max >= Main_num:
#Null
	if Main_num == 0:
		Main_Nam = "Null"
		Main_num += 1
#Attack
	if Main_num == 1:
		Main_Nam = "Attack"
		print(str(Main_num) + "." + str(Main_Nam))
		Main_num += 1
	
	
#Items
	if Main_num == 2:
		Main_Nam = "Items"
		print(str(Main_num) + "." + str(Main_Nam))
		Main_num += 1

#Magic
	if Main_num == 3:

		Main_Nam = "Magic"
		print(str(Main_num) + "." + str(Main_Nam))
		Main_num += 1

#Debug
	if Main_num == 4:

		Main_Nam = "Debug"

		Main_num = 4
		print(str(Main_num) + "." + str(Main_Nam))
		Main_num += 1
