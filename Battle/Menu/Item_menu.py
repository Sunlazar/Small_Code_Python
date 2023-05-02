Item_num = 0
atk_max = 3
while atk_max >= Item_num:
#Null
	if Item_num == 0:
		Item_Nam = "Null"
		Item_num = 0
		Item_num += 1
#Vitals Viewer
	if Item_num == 1:
		Item_Nam = "Vitals Viewer"
		print(str(Item_num) + "." + str(Item_Nam))
		Item_num += 1
