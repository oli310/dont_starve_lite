from numpy import random
import sys
import os

class Game:
	def __init__(self, action_point,size_x,size_y,pos_x,pos_y,inventory_dict, atlas,circle):
		self.action_point = action_point
		self.size_x = size_x
		self.size_y = size_y
		self.pos_x = pos_x
		self.pos_y = pos_y
		self.inventory_dict = inventory_dict
		self.atlas = atlas
		self.circle = circle
 

def where_am_i(jump_atlas):
	print(my_map)
	if jump_atlas == "T" and g.inventory_dict["axe"] > 0:
			print("Wood cutting? y/n")
			activity_wood(jump_atlas, "axe", "tree")
	elif jump_atlas == "G":
			print("ingathering? y/n")
			activity(jump_atlas, "grass")
	elif jump_atlas == "S":
			print("Stone Mining? y/n")
			activity_stone(jump_atlas, "pickaxe", "stone")
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
			g.atlas[g.pos_x][g.pos_y] = jump_atlas.capitalize()
	helper()
def activity_wood(jump_atlas, tool, raw_m ):
	activity = input("Enter the action command: \n")
	if activity == "y":
		print("OK")
		g.inventory_dict[tool] -= 0.1
		g.inventory_dict[raw_m]+=1
		g.action_point -= 1
		jump_atlas = "E"
		g.atlas[g.pos_x][g.pos_y] = jump_atlas
		print("OK, +1", raw_m)
	elif activity == "n": 
		g.atlas[g.pos_x][g.pos_y] = jump_atlas.capitalize()
		print("OK, EXIT")
	else:
		print("INVALID character")
		where_am_i(jump_atlas)
def activity_stone(jump_atlas, tool, raw_m):
	activity = input("Enter the action command: \n")
	if activity == "y":
		g.inventory_dict[tool] -= 0.2
		g.inventory_dict[raw_m] += 1
		g.action_point -= 1
		jump_atlas = "E"
		g.atlas[g.pos_x][g.pos_y] = jump_atlas
		print("OK, +1", raw_m)
	elif activity == "n":
		g.atlas[g.pos_x][g.pos_y] = jump_atlas.capitalize()
		print("Ok, Exit")
	else:
		print("INVALID character")
		where_am_i(jump_atlas)
def activity(jump_atlas, raw_m):
	activity = input("Enter the action command: \n")
	if activity == "y":
		g.inventory_dict[raw_m] += 1
		g.action_point -= 1
		jump_atlas = "E"
		g.atlas[g.pos_x][g.pos_y] = "E"
		print("OK, +1", raw_m)
	elif activity == "n":
		g.atlas[g.pos_x][g.pos_y] = jump_atlas.capitalize()
		print("OK")
	else:
		print("INVALID character")
		where_am_i(jump_atlas)
def helper():
	print("Control: W,A,S,D\n-m Map\n-ea - Eating\n-cf - Campfire\n-co - Cooking")
	print("-in - Inventory\n-ma - Make Axe\n-mp - Make pickaxe\n-mt - Make Trap")
	print("-n - Nothing")
	main()

def make_trap(raw_m, raw_m1, m_raw_m):
	if g.inventory_dict[raw_m] >= 6 and g.inventory_dict[raw_m1] >= 3:
		g.inventory_dict[raw_m] -= 6
		g.inventory_dict[raw_m1] -= 3
		action_point -= 1
		print("Succesfull, +1 ", m_raw_m)
	else:
		print("Not enough raw materials")
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
		print("Succesfull, +1 " co_raw_m)
	else:
		print("Not enough raw materials") 	
def eating(raw_m):
	print("eating")
def my_control(action, circle):
		condition_chechker()
		if action == "s" and g.pos_x != g.size_x -1:
			jump_atlas = g.atlas[g.pos_x+1][g.pos_y]
			g.pos_x += 1
			g.atlas[g.pos_x][g.pos_y] = "C"
			where_am_i(jump_atlas)
			g.circle += 1
		elif action == "w" and g.pos_x != 0:
			jump_atlas = g.atlas[g.pos_x-1][g.pos_y]
			g.pos_x -= 1
			g.atlas[g.pos_x][g.pos_y] = "C"
			where_am_i(jump_atlas)
			g.circle += 1
		elif action == "d" and g.pos_y != g.size_y -1: #pos_y +1 
			jump_atlas = g.atlas[g.pos_x][g.pos_y+1]
			g.pos_y += 1
			g.atlas[g.pos_x][g.pos_y] = "C"
			where_am_i(jump_atlas)
			g.circle += 1
		elif action == "a" and g.pos_y != 0: #pos_y - 1 
			jump_atlas = g.atlas[g.pos_x][g.pos_y-1]
			g.pos_y -= 1
			g.atlas[g.pos_x][g.pos_y] = "C"
			where_am_i(jump_atlas)
			g.circle += 1
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
			print(g.atlas)
		elif action == "ea":
			eating()
		elif action == "co":
			berry_cooking()
		elif action == "ma":
			make_axe()
		elif action == "mp":
			make_pickeaxe()
		elif action == "mt":
			make_trap()
		elif action == "cf":
			make_camp_fire()
		elif action == "in":
			print(g.inventory_dict)
		else: 
			print("INVALID character")
		main()
def condition_chechker():
	if g.inventory_dict["hp"] < 10 or g.inventory_dict["brain"] < 10 or g.inventory_dict["hunger"] < 10:
		print("eat or die")






def main():
		if g.inventory_dict["hp"] == 0 or g.inventory_dict["brain"] == 0 or g.inventory_dict["hunger"] == 0:
			print("Game Over")
		else:
			action = input("Enter the action command: \n")
			my_control(action, g.circle)
if __name__ == "__main__":
	try:
		my_size_x, my_size_y  = 10 , 10
		my_pos_x , my_pos_y = int((my_size_x -1)  / 2), int((my_size_y -1) / 2)
		my_map = random.choice(['T','G', 'S', 'B', 'F', 'E'],
						p = [0.24, 0.09, 0.15, 0.16, 0.05, 0.31],
						size=(my_size_x, my_size_y))
		g = Game(100,my_size_x,my_size_y,my_pos_x,my_pos_y,
			{
									"hp":100,
									"brain":100,
									"hunger":100,
									"tree": 10,
									"grass": 10,
									"stone": 10,
									"bough": 10,
									"flower": 10,
									"axe": 2,
									"pickaxe": 1,
									"campfire": 10,
									"trap": 10,
									"wreath": 10,
									"berry": [10, 10, -5, 1],  #c/hunger/hp/brain
									"carrot": [10, 10, 0, 1],
									"rabbit": [10, 15, -8, 2],
									"boiled_berry": [10, 8, 0, 2],
									"boiled_carrot": [10, 8, 2, 3],
									"boiled_rabbit": [10, 22, 3, 4],
			},
			my_map,
			0)
		print("Enter the start to start/restart:")
		main()
	except KeyboardInterrupt:
		print("Interrupted")
		try:
			sys.exit(0)
		except SystemExit:
			os._exit(0)
	



