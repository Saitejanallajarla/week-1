import random
from datetime import datetime

def introduction():
    greet=["Hey there!This is conversion bot",
    "Its pleasure seeing you here .I am conversion  bot..."]
    print(random.choice(greet))
def greeting():
    curr_time=datetime.now()
    curr_hour=curr_time.hour
    if(curr_hour<11 and curr_hour>=4):
    	print("Good Morning !")
    elif(curr_hour>11 and curr_hour<17):
        print("Good Afternoon! ")
    elif(curr_hour>=17 and curr_hour<22):
        print( "Good Evening! ")
    elif(curr_hour>=22 and curr_hour<=24):
        print("Its already late now .but it doesnt matter to learn something")
    else:
        print("oh God! u are searching at midnight...it's tell me")
        
        
def input_data():
     print("choose the option","1.binary","2.octa","3.Hexa",sep='\n')
     option=int(input("enter the choice-"))
     if option==1:
       num=int(input("enter the number-"))
       print(bin(num))
     elif option==2:
       num=int(input("enter the number-"))
       print(oct(num))
     elif option==3:
       num=int(input("enter the number-"))
       print(hex(num))
     else:
      print("enter right choice")

def bot():
    introduction()
    greeting()
    name=input("ur good name plz-")
    print("Hey",name,"Do u want to know any conversions.....")
    print("here we go")
    input_data()
    print("do you want to know something else","1.yes","2.no",sep='\n')
    choice=int(input("enter the option-")) 
    while choice == 1:
    	input_data()
    	print("do you want to know something else","1.yes","2.no",sep='\n')
    	choice=int(input("enter the option-"))
    
bot()