from numpy import random
import sys
import os

class Game:
	def __init__(self, action_point,size_x,size_y,pos_x,pos_y,inventory_dict, atlas,circle, part):
		self.action_point = action_point
		self.size_x = size_x
		self.size_y = size_y
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.inventory_dict = inventory_dict
		self.atlas = atlas
		self.circle = circle
		self.part = part 
 
def where_am_i(jump_atlas):
	part_of_the_day()
	if jump_atlas == "T" :
			print("Wood cutting? y/n")
			activity_tool(jump_atlas, "axe", "tree",10)
	elif jump_atlas == "G":
			print("ingathering? y/n")
			activity(jump_atlas, "grass")
	elif jump_atlas == "S" :
			print("Stone Mining? y/n")
			activity_tool(jump_atlas, "pickaxe", "stone", 7)
	elif jump_atlas == "B":
			print("ingathering? y/n")
			activity(jump_atlas, "bough")
	elif jump_atlas == "F":
			print("ingathering? y/n")
			activity(jump_atlas, "flower")
	elif jump_atlas == "W":
			print("WATER")
	elif jump_atlas == "E":
			print("EMPTY")
			print(jump_atlas)
			g.atlas[g.pos_x][g.pos_y] = jump_atlas.capitalize()
def activity_tool(jump_atlas, tool, raw_m, tool_cor): #pc,c
	activity = input("Enter the action command: \n")
	if activity == "y":
		tmp_l = g.inventory_dict[tool]
		if tmp_l[1] > 0:
			tmp_l[1] -= 1
			g.inventory_dict[raw_m] += 1
			g.inventory_dict[tool] = tmp_l
			g.atlas[g.pos_x][g.pos_y] = "E"
		elif tmp_l[1] == 0 and tmp_l[0] > 1: 
			tmp_l[1] += tool_cor
			tmp_l[0] -= 1
			g.inventory_dict[raw_m] += 1
			g.inventory_dict[tool] = tmp_l
		else:
			print("Make ", tool)

	elif activity == "n": 
		g.atlas[g.pos_x][g.pos_y] = jump_atlas.capitalize()
		print("OK, EXIT")
	else:
		print("INVALID character")
		where_am_i(jump_atlas)
def activity(jump_atlas, raw_m):
	activity = input("Enter the action command: \n")
	if activity == "y":
		g.inventory_dict[raw_m] += 1
		g.action_point -= 1
		g.atlas[g.pos_x][g.pos_y] = "E"
		print("OK, +1", raw_m)
		if raw_m == "flower": g.inventory_dict["brain"] + 2
	elif activity == "n":
		g.atlas[g.pos_x][g.pos_y] = jump_atlas.capitalize()
		print("OK")
	else:
		print("INVALID character")
		where_am_i(jump_atlas)
def helper():
	print("Control: W,A,S,D\n-m Map\n-ea - Eating\n-cf - Campfire\n-co - Cooking")
	print("-in - Inventory\n-ma - Make Axe\n-mp - Make pickaxe\n-mt - Make Trap\n-wr - wreath")
	print("-tr - trap_placement\n -n - Nothing\n-cp - campfire place")
	print(g.atlas)
	main()
def make_tool(raw_m, raw_m1, m_raw_m, pc1, pc2):
	if g.inventory_dict[raw_m] >= pc1 and g.inventory_dict[raw_m1] >= pc2:
		g.inventory_dict[raw_m] -= 6
		g.inventory_dict[raw_m1] -= 3
		g.action_point -= 1
		tmp_l = g.inventory_dict[m_raw_m]
		tmp_l[0] += 1
		g.atlas[g.pos_x][g.pos_y] = "E"
		g.inventory_dict[m_raw_m] = tmp_l
		print("Succesfull, +1 ", m_raw_m)
	else:
		g.atlas[g.pos_x][g.pos_y] = jump_atlas.capitalize()
		print("Not enough raw materials")
		g.atlas[g.pos_x][g.pos_y] = "C"
		helper()
def cooking(raw_m, co_raw_m):
	tmp_l = g.inventory_dict[raw_m]
	if tmp_l[0] >= 2:
		g.action_point -= 1
		tmp_l = g.inventory_dict[raw_m]
		tmp_l[0] -= 2
		g.inventory_dict[raw_m] = tmp_l
		tmp_l = g.inventory_dict[co_raw_m]
		tmp_l[0] += 1
		g.inventory_dict[co_raw_m] = tmp_l
		print("Succesfull, +1 ", co_raw_m)
	else:
		print("Not enough raw materials") 	
def eating(raw_m):
	temp_l = g.inventory_dict[raw_m]
	if temp_l[0] > 0:
		temp_l[0] -= 1
		g.inventory_dict[raw_m] = temp_l
		g.inventory_dict["hunger"] += temp_l[1]
		g.inventory_dict["hp"] += temp_l[2]
		g.inventory_dict["brain"] += temp_l[3]
		print("Cheers")
	else:
		print("Not enough raw materials")
def my_control(action):
		if action == "s" and g.pos_x != g.size_x -1:
			jump_atlas = g.atlas[g.pos_x+1][g.pos_y]
			g.pos_x += 1
			g.atlas[g.pos_x][g.pos_y] = "C"
			where_am_i(jump_atlas)
		elif action == "w" and g.pos_x != 0:
			jump_atlas = g.atlas[g.pos_x-1][g.pos_y]
			g.pos_x -= 1
			g.atlas[g.pos_x][g.pos_y] = "C"
			where_am_i(jump_atlas)
		elif action == "d" and g.pos_y != g.size_y -1: 
			jump_atlas = g.atlas[g.pos_x][g.pos_y+1]
			g.pos_y += 1
			g.atlas[g.pos_x][g.pos_y] = "C"
			where_am_i(jump_atlas)
		elif action == "a" and g.pos_y != 0: 
			jump_atlas = g.atlas[g.pos_x][g.pos_y-1]
			g.pos_y -= 1
			g.atlas[g.pos_x][g.pos_y] = "C"
			where_am_i(jump_atlas)
		elif action == "e":
			where_am_i(jump_atlas)
		elif action == "h":
			helper()
		elif action == "start":
			g.atlas[g.pos_x][g.pos_y] = "C"
			jump_atlas = "E"
			where_am_i(jump_atlas)
		elif action == "m":
			g.atlas[g.pos_x][g.pos_y] == "C"
			part_of_the_day()

		elif action == "cp":
			campfire_placement()
			part_of_the_day()
		elif action == "ea":
			print("b-Berry, c-Carrot, r-Rabbit, br-boiled berry, bc-boiled carrot, br-boiled rabbit")
			activity = input("Enter the action command:")
			if activity == 'b':
				eating("berry")
			elif activity == "c":
				eating("carrot")
			elif activity == "r":
				eating("rabbit")
			elif activity == "bb":
				eating("bb")
			elif activity == "bc":
				eating("bc")
			elif activity == "br":
				eating("br")
		elif action == "co":
			cooking("berry", "boiled_berry")
		elif action == "tr":
			trap_placement()
		elif action == "ma":
			make_tool("tree", "bough", "axe", 2, 3 )
		elif action == "mp":
			make_tool("tree", "grass", "pickaxe", 2, 2 )
		elif action == "mt":
			make_tool("grass", "bough", "trap", 6, 3 )
		elif action == "cf":
			make_tool("tree", "stone", "campfire", 2, 4 )
		elif action == "wr":
			make_tool("flower", "bough", 15, 3 )
		elif action == "in":
			print(g.inventory_dict)
		elif action == "n":
			g.atlas[g.pos_x][g.pos_y] == "C"
		else: 
			print("INVALID character")
		main()

def condition_checker():
	if g.inventory_dict["hp"] < 10 or g.inventory_dict["brain"] < 10 or g.inventory_dict["hunger"] < 10:
		print("eat or die")
	g.inventory_dict["hunger"] -= 0.4
	tmp_l = g.inventory_dict["wreath"]
	if tmp_l and g.part:
		g.inventory_dict["brain"] += 0.5
	elif tmp_l and not g.part:
		g.inventory_dict["brain"] -= 0.3
	tmp_l = g.inventory_dict["trap"]
	if tmp_l[1] != 0:
		for i in range(tmp_l[1]):
			rnd = random.randint(100, dtype = int)
			if rnd == 33:
				tmp_l = g.inventory_dict["rabbit"]
				tmp_l[0] += 1
				g.inventory_dict["rabbit"] = tmp_l
	tmp_l = g.inventory_dict["campfire"]
	if tmp_l[4] > 0 :
		tmp_l[4] -= 1
		g.inventory_dict["campfire"] = tmp_l
		if tmp_l[4] == 0:
			g.atlas[tmp_l[2]][tmp_l[3]] = "E"
	if tmp_l[1] == True and tmp_l[2] == g.pos_x and tmp_l[3] == g.pos_y and tmp_l[4] % 10 != 0: g.inventory_dict["hp"] = 0
def trap_placement():
	tmp_l = g.inventory_dict["trap"]
	if tmp_l[0] > 0:
		tmp_l[0] -= 1
		tmp_l[1] +=1
		g.action_point -= 1
		g.inventory_dict["trap"] = tmp_l
		print("Succesfull")
	else:
		print("Not enough materials")
def campfire_placement():
	tmp_l = g.inventory_dict["campfire"]
	if not tmp_l[1]:
		g.action_point -= 2
		tmp_l[0] -= 1
		tmp_l[1] = True
		tmp_l[2] = g.pos_x
		tmp_l[3] = g.pos_y
		tmp_l[4] = 11
		g.atlas[g.pos_x][g.pos_y] = "P"
def part_of_the_day():
	condition_checker()
	g.circle += 1
	if g.circle % 12 == 0:
		g.part = False
	elif g.circle % 4 == 0: 
		g.part = True
	if not g.part:
		g.inventory_dict["brain"] -= 0.4
		tmp_l = g.inventory_dict["campfire"]
		if tmp_l[0] == 0: 
			print("Make Campfire") 
			main()
		if tmp_l[1] == True:
			for i in range(tmp_l[2]-3,11):
				for j in range(tmp_l[3]-3,11):
					print(g.atlas[i][j], end = ' ' )
				print()
		elif tmp_l[0] > 0 and tmp_l[1] == False:
			print("Make campfire")
			main()		
	else:
		print(g.atlas)

def main():
		if g.inventory_dict["hp"] <= 0 or g.inventory_dict["brain"] <= 0 or g.inventory_dict["hunger"] <= 0:
			print("Game Over")
		else:
			if g.circle == 0: 
				my_control("start")
			print("Enter the action command:  ", end = '')
			action = input()
			my_control(action)
if __name__ == "__main__":
	try:
		my_size_x, my_size_y  = 15 , 15
		my_pos_x , my_pos_y = int((my_size_x -1)  / 2), int((my_size_y -1) / 2)
		my_map = random.choice(['T','G', 'S', 'B', 'F', 'E'],
						p = [0.24, 0.09, 0.15, 0.16, 0.05, 0.31],
						size=(my_size_x, my_size_y))
		g = Game(100,my_size_x,my_size_y,my_pos_x,my_pos_y,
			{
									"hp":9,
									"brain":100,
									"hunger":100,
									"tree": 10,
									"grass": 10,
									"stone": 10,
									"bough": 10,
									"flower": 10,
									"axe": [2,10],
									"pickaxe": [1,10],
									"campfire": [10,False, 0, 0, 0],
									"trap": [10,1],
									"wreath": [10,15, True],
									"berry": [10, 10, -5, 1],  #c/hunger/hp/brain
									"carrot": [10, 10, 0, 1],
									"rabbit": [10, 15, -8, 2],
									"boiled_berry": [10, 8, 0, 2],
									"boiled_carrot": [10, 8, 2, 3],
									"boiled_rabbit": [10, 22, 3, 4],
			},
			my_map,
			1,
			True)
		print(" -h- help")
		main()
	except KeyboardInterrupt:
		print("Interrupted")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
	



