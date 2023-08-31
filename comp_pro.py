def room_2():
    print("welcome to room 2")
    print('would you like to look around?(Y/N)')
    ans=input()
    if (ans=='y' or ans=='Y'):
        print("ARE YOU READY TO TEST YOUR GK?")
        print('ANSWER THE QUESTION TO ADVANCE TO THE NEXT LEVEL/ROOM!!')
        print('would you like to answer a GK question?(Y/N)')
        ans1=input()
        if(ans1=='Y'or ans1=='y'):
            print('what is the capital of karnataka?')
            print('choose from the following options')
            print('1=bengaluru\n2=hyderabad\n3=chennai\n4=none of the above ')
            res=input("Your answer:")
            if(res=='1' ):
                print('YAY u got it right')
                print('you are smart')
                print('do you wish to advance to the next room(Y/N)')
                ans2=input()
            else:
                print('think again you got it wrong')
                print('would you like to restart?(Y/N)')
                ans3=input()
                if(ans3=='y' or ans3=="Y"):
                    room_2()
room_2()           
                
