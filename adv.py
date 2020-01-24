from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()

# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

'''
Notes:

Example room graph:
room_graph = {
    0: [(3, 5), {'n': 1}], 
    1: [(3, 6), {'s': 0, 'n': 2}], 
    2: [(3, 7), {'s': 1}]
}

room_graph[room_id] = list[Tuple (3, 5), dict w/ possible exits {'n': 1}] # reference to the first room
room_graph[0] = [(3, 5), {'n': 1}] # reference to the first room
room_graph[0][0] = (3, 5) # x,y coords?
room_graph[0][1] = {'n': 1} # list of possible exits

Useful commands: 
# Returns the current room's id ('int')
    - player.current_room.id
    # 0
# Returns the current room's exits ('list')
    - player.current_room.get_exits()
    # ['n', 's', 'w', 'e']
# Moves the player in the direction passed (direction = 'str')
    - player.travel(direction)
'''


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
