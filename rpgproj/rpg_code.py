#!/usr/bin/python3
import sys
import os
# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
RPG Game
========
Commands:
  go [direction]
  get [item]
''')

def showStatus():
  os.system('clear')
  #print the player's current status
  print('---------------------------')
  print('You are in the ' + currentRoom)
  #print the current inventory
  print('Inventory : ' + str(inventory))
  #print an item if there is one
  if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])

def acDeath(room):
    #makes sure you're in the sun room, and that the conditioner status is on
    if room == 'Sun Room' and rooms['Sun Room']['conditioner status'] == 'on':
        #kills you
        print("You froze to death! Best air conditioner ever")
        #exits the application
        sys.exit()

def showRoomOptions():
    #loop over room elements, and print them out for user
    for elem in rooms[currentRoom]:
        if elem != 'item' and elem != 'conditioner status':
            print(f"You can go {elem} to get to {rooms[currentRoom][elem]}")
    print("---------------------------")

#an inventory, which is initially empty
inventory = []

#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {
    "Hall": {
        "north": "Living Room",
        "south": "Kitchen",
        "east": "Dining Room",
        "item": "key",
    },
    "Kitchen": {
        "north": "Hall",
        "item": "monster",
    },
    "Dining Room": {
        "west": "Hall",
        "south": "Garden",
        "item": "potion",
        "north": "Pantry",
    },
    "Garden": {"north": "Dining Room"},
    "Pantry": {
        "south": "Dining Room",
        "item": "cookie",
    },
    "Living Room": {
        "south": "Hall",
        "east": "Sun Room",
    },
    "Sun Room": {
        "item": "air conditioner",
        "conditioner status": "off",
        "west" : "Living Room",
    },
}
#start the player in the Hall
currentRoom = 'Hall'

showInstructions()

#loop forever
while True:

  showStatus()
  showRoomOptions()
  #get the player's next 'move'
  #.split() breaks it up into an list array
  #eg typing 'go east' would give the list:
  #['go','east']
  move = ''
  while move == '':
    move = input('>')

  # split allows an items to have a space on them
  # get golden key is returned ["get", "golden key"]          
  move = move.lower().split(" ", 1)

  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('You can\'t go that way!')

  #if they type 'get' first
  if move[0] == 'get' :
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
        #checks to see if the item is an airconditioner explicitly
        if "item" in rooms[currentRoom] and rooms[currentRoom]['item'] == "air conditioner":
            #changes the status of conditioner so it kills you
            rooms[currentRoom]['conditioner status'] = 'on'
            print(move[1] + ' has been turned on!')
            #calls to acDeath function so you can die
            acDeath(currentRoom)
        else:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #tell them they can't get it
      print('Can\'t get ' + move[1] + '!')
      
  ## Define how a player can win
  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
    break

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break
  ## If a player turns on the A/C in the sun room
  elif currentRoom == 'Sun Room' and rooms[currentRoom]['conditioner status'] == 'on':
    print('You froze to death, best air conditioner ever!')
    break

