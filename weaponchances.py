import libtcodpy as libtcod



# ##Classes copied from firstrl.py as necessary###

def from_dungeon_level(table):
	# returns a value that depends on level. The table specifies what value occurs after each level, default is 0.
	for (value, level) in reversed(table):
		if dungeon_level >= level:
			return value
	return 0


def eat_food(
		value):  # PUT THIS IN THE ITEM CLASS AND GIVE IT A FOOD_VALUE TO CALL FROM ALSO WITHIN THE ITEM CLASS, then fix save functionality.
	# TODO: Allow system to call objects food value if any, and restore by that amount
	# currently only allows for a fixed rate for one type of food
	global hunger_level
	# Lower their hunger level
	[]
	if hunger_level <= 40:
		message('You are already full!', libtcod.white)
		return 'cancelled'
	else:
		message('Mmm, that was delicious!', libtcod.light_green)
		hunger_level -= value


def random_choice_index(chances):  # choose one option from list of chances, returning its index
	#the dice will land on some number between 1 and the sum of the chances
	dice = libtcod.random_get_int(0, 1, sum(chances))

	#go through all the chances, keeping the sum so far
	running_sum = 0

	choice = 0
	for w in chances:
		running_sum += w

		#see if the dice landed in the part that corresponds to this choice
		if dice <= running_sum:
			return choice
		choice += 1


def random_choice(chances_dict):
	chances = chances_dict.values()  # Pull the integer value of a dict entry (80, 20, 10 etc.)
	strings = chances_dict.keys()  # Pull the string name of a dict entry (Dog/Snake etc)

	return strings[random_choice_index(chances)]  # return names[random function(specific value)]


# ##Finished with firstrl.py classes###



def add_food_and_scrolls(x, y):
	item_chances = {}
	item_chances['nothing'] = 50
	item_chances['heal'] = 15
	item_chances['bread'] = 10  # bread always shows up, even if all other items have 0 chance
	item_chances['lightning'] = from_dungeon_level([[25, 4]])
	item_chances['fireball'] = from_dungeon_level([[25, 6]])
	item_chances['confuse'] = from_dungeon_level([[10, 2]])

	choice = random_choice(item_chances)

	if choice == 'heal':
		#create a healing potion
		item_component = Item(use_function=cast_heal)
		item = Object(x, y, chr(173), 'healing potion', libtcod.dark_green, item=item_component, always_visible=True)

	elif choice == 'nothing':  # Allows a possibility to spawn nothing
		item = item = Object(x, y, chr(0), 'nothing', libtcod.darker_orange, equipment=None, item=None,
							 always_visible=False)

	elif choice == 'lightning':
		#create a lightning bolts scroll (15% chance)
		item_component = Item(use_function=cast_lightning)
		item = Object(x, y, '!', 'scroll of lightning bolt', libtcod.light_blue, item=item_component,
					  always_visible=True)

	elif choice == 'fireball':
		#create a fireball scroll (10% chance)
		item_component = Item(use_function=cast_fireball)
		item = Object(x, y, '#', 'scroll of fireball', libtcod.dark_orange, item=item_component, always_visible=True)

	elif choice == 'confuse':
		#create a confuse scroll (15% chance)
		item_component = Item(use_function=cast_confuse)
		item = Object(x, y, '?', 'scroll of confusion', libtcod.darkest_yellow, item=item_component,
					  always_visible=True)

	elif choice == 'bread':
		#create a piece of bread
		item_component = Item(use_function=(eat_food([200])))
		item = Object(x, y, 'x', 'piece of bread', libtcod.darkest_red, item=item_component, always_visible=True)

	objects.append(item)

	item.send_to_back()  #items appear below other objects


def random_item():  #all item chance totals for a subtype will be self contained
	rand_type = libtcod.random_get_int(0, 0, 2)  # Item types, starts at 0, weapons
	item_chances = {}
	if rand_type == 0:  # Spawn a weapon
		#WEAPON CHANCES - Will have to be called each time for i in range
		rand_weapon_type = libtcod.random_get_int(0, 0, 2)  # Weapon types, starts at 0, Swords,

		if rand_weapon_type == 0:  # Swords
			item_chances['wooden sword'] = from_dungeon_level([[5, 1], [10, 2]])
			item_chances['brass sword'] = from_dungeon_level([[5, 3], [10, 4]])
			item_chances['steel sword'] = from_dungeon_level([[1, 3], [15, 5]])
			item_chances['golden sword'] = from_dungeon_level([[5, 5], [12, 8]])
			item_chances['demon sword'] = from_dungeon_level([[1, 8], [4, 10]])
			item_chances['ares sword'] = from_dungeon_level([[1, 10], [4, 12]])
			item_chances['healing sword'] = from_dungeon_level([[1, 10], [2, 14]])

		if rand_weapon_type == 1:  # Axes

			item_chances['nothing'] = 10
			item_chances['bronze axe'] = from_dungeon_level([[5, 3], [10, 4]])
			item_chances['rusty steel axe'] = from_dungeon_level([[1, 3], [3, 5], [30, 6]])
			item_chances['steel axe'] = from_dungeon_level([[1, 3], [20, 5]])
			item_chances['diamond axe'] = from_dungeon_level([[5, 5], [10, 8]])
			item_chances['ares axe'] = from_dungeon_level([[1, 10], [4, 12]])
			item_chances['godsbane axe'] = from_dungeon_level([[1, 10], [2, 14]])

		if rand_weapon_type == 2:  # War Hammers

			item_chances['nothing'] = 1
			item_chances['stone war hammer'] = from_dungeon_level([[5, 1], [60, 2]])
			item_chances['bronze war hammer'] = from_dungeon_level([[5, 3], [10, 4]])
			item_chances['pig iron war hammer'] = from_dungeon_level([[1, 3], [3, 5]])
			item_chances['steel war hammer'] = from_dungeon_level([[1, 3], [10, 5]])
			item_chances['obsidian war hammer'] = from_dungeon_level([[5, 5], [10, 8]])
			item_chances['unobtanium war hammer'] = from_dungeon_level([[1, 10], [4, 12]])
			item_chances['godsbane war hammer'] = from_dungeon_level([[1, 10], [2, 14]])

	if rand_type == 1:  # Spawn a piece of armor
		#ARMOR CHANCES - Will have to be called each time for i in range
		rand_armor_type = libtcod.random_get_int(0, 0, 1)  # Armor types, starts at 0, gauntlets
		if rand_armor_type == 0:  # gauntlets

			item_chances['nothing'] = 90
			item_chances['silk gauntlets'] = from_dungeon_level([[5, 1], [40, 2]])
			item_chances['wooden gauntlets'] = from_dungeon_level([[5, 3], [10, 4]])
			item_chances['bronze gauntlets'] = from_dungeon_level([[1, 3], [30, 5]])
			item_chances['iron gauntlets'] = from_dungeon_level([[5, 5], [10, 8]])
			item_chances['steel gauntlets'] = from_dungeon_level([[1, 8], [5, 10]])
			item_chances['obsidian gauntlets'] = from_dungeon_level([[1, 10], [4, 12]])
			item_chances['Divine gauntlets'] = from_dungeon_level([[1, 10], [2, 18]])

		if rand_armor_type == 1:  # body armor

			item_chances['nothing'] = 20  #Gives a chance to spawn nothing
			item_chances['wooden ring mail'] = from_dungeon_level([[5, 1], [30, 2]])
			item_chances['bronze ring mail'] = from_dungeon_level([[5, 3], [20, 4]])
			item_chances['steel ring mail'] = from_dungeon_level([[1, 3], [5, 5]])
			item_chances['steel plate armor'] = from_dungeon_level([[1, 3], [10, 5]])
			item_chances['obsidian plate armor'] = from_dungeon_level([[5, 5], [10, 8]])
			item_chances['unobtanium plate armor'] = from_dungeon_level([[0.1, 10], [4, 12]])
			item_chances['hercules armor'] = from_dungeon_level([[1, 10], [2, 14]])

	if rand_type == 2:  # Spawn a wearable item
		#W/Item CHANCES - Will have to be called each time for i in range
		rand_item_type = libtcod.random_get_int(0, 0, 1)  # W/Item types, starts at 0, rings
		if rand_item_type == 0:  # rings

			item_chances['nothing'] = 30
			item_chances['wooden ring of health'] = from_dungeon_level([[5, 1], [20, 5]])
			item_chances['wooden ring of strength'] = from_dungeon_level([[5, 1], [20, 5]])
			item_chances['wooden ring of defense'] = from_dungeon_level([[5, 1], [20, 5]])
			item_chances['steel ring of health'] = from_dungeon_level([[5, 5], [8, 8]])
			item_chances['steel ring of strength'] = from_dungeon_level([[5, 5], [8, 8]])
			item_chances['steel ring of defense'] = from_dungeon_level([[5, 5], [8, 8]])
			item_chances['golden ring of health'] = from_dungeon_level([[3, 8], [6, 12]])
			item_chances['golden ring of strength'] = from_dungeon_level([[3, 8], [6, 12]])
			item_chances['golden ring of defense'] = from_dungeon_level([[3, 8], [6, 12]])
			item_chances['diamond ring of health'] = from_dungeon_level([[1, 12], [3, 15]])
			item_chances['diamond ring of strength'] = from_dungeon_level([[1, 12], [3, 15]])
			item_chances['diamond ring of defense'] = from_dungeon_level([[1, 12], [3, 15]])
			item_chances['glowing ring of health'] = from_dungeon_level([[1, 15]])
			item_chances['glowing ring of strength'] = from_dungeon_level([[1, 15]])
			item_chances['glowing ring of defense'] = from_dungeon_level([[1, 15]])

		if rand_item_type == 1:  # boots

			item_chances['nothing'] = 40
			item_chances['silk boots of health'] = from_dungeon_level([[1, 1], [5, 2]])
			item_chances['bronze boots of strength'] = from_dungeon_level([[1, 4], [5, 6]])
			item_chances['steel boots of health'] = from_dungeon_level([[1, 4], [2, 6]])
			item_chances['obsidian boots of defense'] = from_dungeon_level([[1, 6]])

	return item_chances
	item_chances = {}


def create_item(x, y):
	item_chances = random_item()
	choice = random_choice(item_chances)

	if choice == 'wooden sword':
		#create a wooden sword
		equipment_component = Equipment(slot='left hand', power_bonus=2)
		item = Object(x, y, '/', 'Wooden sword', libtcod.darker_orange, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'brass sword':
		equipment_component = Equipment(slot='left hand', power_bonus=4)
		item = Object(x, y, '/', 'Brass sword', libtcod.orange, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'steel sword':
		equipment_component = Equipment(slot='left hand', power_bonus=6)
		item = Object(x, y, '/', 'Steel sword', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'golden sword':
		equipment_component = Equipment(slot='left hand', power_bonus=10)
		item = Object(x, y, '/', 'Golden sword', libtcod.gold, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'demon sword':
		equipment_component = Equipment(slot='left hand', power_bonus=18)
		item = Object(x, y, '/', 'Demon sword', libtcod.dark_purple, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'ares sword':
		equipment_component = Equipment(slot='left hand', power_bonus=25)
		item = Object(x, y, '/', 'Ares sword', libtcod.yellow, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'healing sword':  #TODO:Needs to have a cast_heal function fire if this is equipped and the player attacks and the dice roll is true
		equipment_component = Equipment(slot='left hand', power_bonus=25)
		item = Object(x, y, '/', 'Brass sword', libtcod.white, equipment=equipment_component, item=None,
					  always_visible=True)

	##AXES##

	elif choice == 'wooden axe':
		equipment_component = Equipment(slot='left hand', power_bonus=2)
		item = Object(x, y, chr(244), 'Wooden axe', libtcod.darker_orange, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'bronze axe':
		equipment_component = Equipment(slot='left hand', power_bonus=4)
		item = Object(x, y, chr(244), 'Bronze axe', libtcod.orange, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'rusty steel axe':
		equipment_component = Equipment(slot='left hand', power_bonus=5)
		item = Object(x, y, chr(244), 'Rusty steel axe', libtcod.darkest_orange, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'steel axe':
		equipment_component = Equipment(slot='left hand', power_bonus=6)
		item = Object(x, y, chr(244), 'Steel axe', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'diamond axe':
		equipment_component = Equipment(slot='left hand', power_bonus=10)
		item = Object(x, y, chr(244), 'Diamond axe', libtcod.light_blue, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'ares axe':
		equipment_component = Equipment(slot='left hand', power_bonus=25)
		item = Object(x, y, chr(244), 'Ares axe', libtcod.gold, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'godsbane axe':
		equipment_component = Equipment(slot='left hand', power_bonus=35)
		item = Object(x, y, chr(244), 'Godsbaneaxe', libtcod.light_blue, equipment=equipment_component, item=None,
					  always_visible=True)

	##WAR HAMMERS##

	elif choice == 'stone war hammer':
		equipment_component = Equipment(slot='left hand', power_bonus=5)
		item = Object(x, y, chr(25), 'Stone war hammer', libtcod.darker_grey, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'bronze war hammer':
		equipment_component = Equipment(slot='left hand', power_bonus=8)
		item = Object(x, y, chr(25), 'Bronze war hammer', libtcod.orange, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'pig iron war hammer':
		equipment_component = Equipment(slot='left hand', power_bonus=12)
		item = Object(x, y, chr(25), 'Pig iron war hammer', libtcod.light_grey, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'steel war hammer':
		equipment_component = Equipment(slot='left hand', power_bonus=15)
		item = Object(x, y, chr(25), 'Steel war hammer', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'obsidian war hammer':
		equipment_component = Equipment(slot='left hand', power_bonus=20)
		item = Object(x, y, chr(25), 'Obsidian war hammer', libtcod.darkest_grey, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'unobtanium war hammer':
		equipment_component = Equipment(slot='left hand', power_bonus=30)
		item = Object(x, y, chr(25), 'Unobtanium war hammer', libtcod.desaturated_green, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'godsbane war hammer':
		equipment_component = Equipment(slot='left hand', power_bonus=45)
		item = Object(x, y, chr(25), 'godsbane war hammer', libtcod.light_grey, equipment=equipment_component,
					  item=None, always_visible=True)

	#######
	#ARMOR#
	#######

	##GAUNTLETS##

	elif choice == 'silk gauntlets':
		equipment_component = Equipment(slot='hands', defense_bonus=1)
		item = Object(x, y, chr(7), 'Silk gauntlets', libtcod.light_purple, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'wooden gauntlets':
		equipment_component = Equipment(slot='hands', defense_bonus=2)
		item = Object(x, y, chr(170), 'Wooden gauntlets', libtcod.darker_orange, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'bronze gauntlets':
		equipment_component = Equipment(slot='hands', defense_bonus=4)
		item = Object(x, y, chr(170), 'Bronze gauntlets', libtcod.orange, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'iron gauntlets':
		equipment_component = Equipment(slot='hands', defense_bonus=5)
		item = Object(x, y, chr(170), 'Iron gauntlets', libtcod.lighter_grey, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'steel gauntlets':
		equipment_component = Equipment(slot='hands', defense_bonus=7)
		item = Object(x, y, chr(170), 'Steel gauntlets', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'obsidian gauntlets':
		equipment_component = Equipment(slot='hands', defense_bonus=9)
		item = Object(x, y, chr(170), 'Wooden gauntlets', libtcod.black, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'divine gauntlets':
		equipment_component = Equipment(slot='hands', defense_bonus=12)
		item = Object(x, y, chr(170), 'Divine gauntlets', libtcod.yellow, equipment=equipment_component, item=None,
					  always_visible=True)

	##BODY ARMOR##

	elif choice == 'nothing':  #Allows a possibility to spawn nothing
		item = item = Object(x, y, chr(0), 'nothing', libtcod.darker_orange, equipment=None, item=None,
							 always_visible=False)

	elif choice == 'wooden ring mail':
		equipment_component = Equipment(slot='body', defense_bonus=2)
		item = Object(x, y, chr(21), 'Wooden ring mail', libtcod.darker_orange, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'bronze ring mail':
		equipment_component = Equipment(slot='body', defense_bonus=4)
		item = Object(x, y, chr(21), 'Bronze ring mail', libtcod.orange, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'steel ring mail':
		equipment_component = Equipment(slot='body', defense_bonus=8)
		item = Object(x, y, chr(21), 'Steel ring mail', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'steel plate armor':
		equipment_component = Equipment(slot='body', defense_bonus=14)
		item = Object(x, y, chr(21), 'Steel plate armor', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'obsidian plate armor':
		equipment_component = Equipment(slot='body', defense_bonus=20)
		item = Object(x, y, chr(21), 'Obsidian plate armor', libtcod.black, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'hercules armor':
		equipment_component = Equipment(slot='body', defense_bonus=30)
		item = Object(x, y, chr(21), "Hercules's armor", libtcod.gold, equipment=equipment_component, item=None,
					  always_visible=True)

	##RINGS##

	elif choice == 'wooden ring of health':
		equipment_component = Equipment(slot='finger', max_hp_bonus=10)
		item = Object(x, y, chr(249), 'Wooden ring of health', libtcod.darker_orange, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'wooden ring of strength':
		equipment_component = Equipment(slot='finger', power_bonus=1)
		item = Object(x, y, chr(249), 'Wooden ring of strength', libtcod.darker_orange, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'wooden ring of defense':
		equipment_component = Equipment(slot='finger', defense_bonus=1)
		item = Object(x, y, chr(249), 'Wooden ring of defense', libtcod.darker_orange, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'steel ring of health':
		equipment_component = Equipment(slot='finger', max_hp_bonus=25)
		item = Object(x, y, chr(249), 'Steel ring of health', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'steel ring of strength':
		equipment_component = Equipment(slot='finger', power_bonus=5)
		item = Object(x, y, chr(249), 'Steel ring of strength', libtcod.silver, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'steel ring of defense':
		equipment_component = Equipment(slot='finger', defense_bonus=3)
		item = Object(x, y, chr(249), 'Steel ring of defense', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'golden ring of health':
		equipment_component = Equipment(slot='finger', max_hp_bonus=50)
		item = Object(x, y, chr(249), 'Golden ring of health', libtcod.gold, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'golden ring of strength':
		equipment_component = Equipment(slot='finger', power_bonus=8)
		item = Object(x, y, chr(249), 'Golden ring of strength', libtcod.gold, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'golden ring of defense':
		equipment_component = Equipment(slot='finger', defense_bonus=5)
		item = Object(x, y, chr(249), 'Golden ring of defense', libtcod.gold, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'diamond ring of health':
		equipment_component = Equipment(slot='finger', max_hp_bonus=80)
		item = Object(x, y, chr(249), 'Diamond ring of health', libtcod.light_blue, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'diamond ring of strength':
		equipment_component = Equipment(slot='finger', power_bonus=15)
		item = Object(x, y, chr(249), 'Diamond ring of strength', libtcod.light_blue, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'diamond ring of defense':
		equipment_component = Equipment(slot='finger', defense_bonus=10)
		item = Object(x, y, chr(249), 'Diamond ring of defense', libtcod.light_blue, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'glowing ring of health':
		equipment_component = Equipment(slot='finger', max_hp_bonus=125)
		item = Object(x, y, chr(249), 'Diamond ring of health', libtcod.yellow, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'glowing ring of strength':
		equipment_component = Equipment(slot='finger', power_bonus=25)
		item = Object(x, y, chr(249), 'Diamond ring of strength', libtcod.yellow, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'glowing ring of defense':
		equipment_component = Equipment(slot='finger', defense_bonus=15)
		item = Object(x, y, chr(249), 'Diamond ring of defense', libtcod.yellow, equipment=equipment_component,
					  item=None, always_visible=True)

	##BOOTS##

	elif choice == 'silk boots of health':
		equipment_component = Equipment(slot='feet', max_hp_bonus=10)
		item = Object(x, y, chr(28), 'Silk boots of health', libtcod.darker_magenta, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'bronze boots of strength':
		equipment_component = Equipment(slot='feet', power_bonus=2)
		item = Object(x, y, chr(28), 'Bronze boots of strength', libtcod.orange, equipment=equipment_component,
					  item=None, always_visible=True)

	elif choice == 'steel boots of health':
		equipment_component = Equipment(slot='feet', max_hp_bonus=20)
		item = Object(x, y, chr(28), 'Steel boots of health', libtcod.silver, equipment=equipment_component, item=None,
					  always_visible=True)

	elif choice == 'obsidian boots of defense':
		equipment_component = Equipment(slot='feet', defense_bonus=10)
		item = Object(x, y, chr(28), 'Obsidian boots of defense', libtcod.black, equipment=equipment_component,
					  item=None, always_visible=True)

	objects.append(item)
	item.send_to_back()
	item_chances = {}

	# TODO: implement food and scrolls rolling, and add more items
	# - Make sure item 'nothing' is always sent to back otherwise it covers other objects
	# - Fix eat_food being applied to the player every time a new map is made. Use debug on the eat)hunger function toi figure out why it's being called
	#- levels 1-4 very easy
	#