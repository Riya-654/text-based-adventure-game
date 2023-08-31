def room_4():
 print("Welcome to room 4")
 print("Would you like to look around?(Y/N)")
 ans=input()
 if(ans=='Y' or ans=='y'):
    print("Decode the given code to obtain the key to the room!")
    print("would you like to answer the riddle?(Y/N)")
    ans1=input()
    if(ans1=='Y' or ans1=='y'):
        print("In certain code 'TIGER' is written as 'QDFHS'. How is 'FISH' written in that code?",'\n',
                 "1.GERH  2.GRHE  3.GREH  4.GHRE  5.GEHR")
        res=input("Your answer:")
        if(res=='2'):
             print("CONGRATULATIONS!YOU HAVE ANSWERED THE RIDDLE CORRECTLY AND UNLOCKED THE DOOR!")
             print("Proceed to room 5?(Y/N)")
             ans2=input()
        else:
            print("SORRY!you have failed to unlock the door!Better luck next time!")
            print("Would you like to restart?(Y/N)")
            ans3=input()
            if(ans3=='Y' or ans3=='y'):
                room_4()
            else:
                print("Would you like to use a gem to obtain the key?(Y/N)")
                ans4=input()
                if(ans4=='y' or ans4=='Y'):
                    if(gem_count>=0):
                        print("One gem used!")
                        print("CONGRATULATIONS!YOU HAVE UNLOCKED THE DOOR!")
                        gem_count-=1
                    else:
                        print("Sorry!You are out of gems!:(")
                        print("Would you like to restart?(Y/N)")
                        ans5=input()
                        if(ans5=='y' or ans5=='Y'):
                            room_4()
                        else:
                            print("okie")
    else:
        print("okie")
 else:
  print('okie')
room_4()
