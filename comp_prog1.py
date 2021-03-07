def room_5():
    print("welcome to room 5")
    print('would you like to look around?(Y/N)')
    ans=input()
    if (ans=='y' or ans=='Y'):
        print('ANSWER THE QUESTION TO ADVANCE TO THE NEXT LEVEL/ROOM!!')
        print('would you like to answer a question?(Y/N)')
        ans1=input()
        if(ans1=='Y'or ans1=='y'):
            print('What starts with “e” and ends with “e” but only has one letter in it?')
            res=input("Your answer:")
            if(res=='An envelope'  or res=='envelope'):
                print('YAY u got it right')
                print('you are smart')
                print('do you wish to advance to the next room(Y/N)')
                ans2=input()
            else:
                print('think again you got it wrong')
                print('would you like to restart?(Y/N)')
                ans3=input()
                if(ans3=='y' or ans3=="Y"):
                    room_5()
room_5()
