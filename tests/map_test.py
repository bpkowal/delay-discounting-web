from nose.tools import *
from discounting.map import *

def test_room():
    gold = Room("$5","Today", "$10", "in 1 DAY")
    assert_equal(gold.ss_a, "$5")
    assert_equal(gold.paths, {})

def test_room_paths():
	gold = Room("$5","Today", "$10", "in 1 DAY") 
	up_one = Room("$7.5", "Today", "$10", "IN 1 DAY")
	down_one = Room("$2.5", "Today", "$10", "IN 1 DAY")

	gold.add_paths({'up_one': up_one, 'down_one': down_one})
	assert_equal(gold.go('up_one'), up_one)
	assert_equal(gold.go('down_one'), down_one)

#def test_map():
#    start = Room("Start", "You can go west and down a hole.")
#    west = Room("Trees", "There are trees here, you can go east.")
#    down = Room("Dungeon", "It's dark down here, you can go up.")

#    start.add_paths({'west': west, 'down': down})
#    west.add_paths({'east': start})
#    down.add_paths({'up': start})

 #   assert_equal(start.go('west'), west)
 #   assert_equal(start.go('west').go('east'), start)
 #   assert_equal(start.go('down').go('up'), start)

#def test_gothon_game_map():
#    assert_equal(START.go('shoot!'), generic_death)
#    assert_equal(START.go('dodge!'), generic_death)

#    room = START.go('tell a joke')
#    assert_equal(room, laser_weapon_armory)
