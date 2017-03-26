'''this is 1st game i m creating'''
def start():
 print('you are in a dark room')
 print('there are two doors left and right whic will you choose')
 next=input("entre left or right\n>>")
 if("left" in next):
  bear_room()
 elif("right" in next):
  dayanroom()
 else:
  print("you will stumble around the room till you starve")
  exit(0)
def dayanroom():
 print("you entre a room you see a dayan")
 print("what will you do")
 print("run ;r let her eat you")
 next=input("please entre your choice to run or stay \n >>")
 if("run" in next):
  start()
 elif("stay" in next):
  why="you r tasty"
  dead(why)
 else: 
  dayanroom()
def dead(why):
 print("%s \n good job"%why)
def bear_room():
 print("you are in a room")
 print("a bear is standing in front of you in the room")
 print("bear has honey what will you do now")
 bear_moved=False
 while(True):
  next=input("please entre to take honey or to taunt bear")
  if(next=="take honey"):
    dead("The bear looks at you then slaps your face off.")
  elif(next=="taunt bear"is not bear_moved):
    print("The bear has moved from the door. You can go through it now.")
    bear_moved=True
  elif("taunt bear"is next and bear_moved):
    dead("The bear gets pissed off and chews your leg off.")
  elif(next=="open door" and bear_moved):
    gold_room()
  else:
    print("I got no idea what that means.")
def gold_room():
 print("the room is filled with gold")
 print("how many will you take")
 next=input("please entre a value")
 if(next=="0"):
  print("you win")
  exit()
 else:
  dead("you are greedy")
start()