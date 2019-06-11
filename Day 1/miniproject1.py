#Python Mini Project 1

import random
secret_number= random.randint(1,10)
guess_number=int(input("Enter a number between 1 and 10 : "))


#checking the input is integer
'''
if(type(guess_number)!=int):
    print("Enter an integer value")
    '''
#challange 6
#(catching when a user submit a non integer value)


#challange 2
#using format function

'''
if(secret_number==guess_number):
    print("Player Wins... and Computer looses...")
elif(secret_number<guess_number):
    print("TOO HIGH Computer wins.. and Player looses...Number was {}.format(secret_number)")
else:
    print("TOO LOW Computer wins.. and Player looses...Number was {}.format(secret_number)")
'''


#restricting number of tries by 6
numberoftries=6
while(True):
    if(numberoftries>=1):
         if(secret_number!=guess_number):
            guess_number=int(input("Enter a number between 1 and 10 : "))
            if(secret_number==guess_number):
                print("Player Wins... and Computer looses...")
                
                #play again
                choice=input("Do you want to play again? Yes/No : ")
                if(choice=='Yes'):
                    secret_number= random.randint(1,10)   #taking random number
                    guess_number=int(input("Enter a number between 1 and 10 : "))
                    #restricting number of tries
                    numberoftries=6
                    while(True):
                        if(numberoftries>=1):
                            #when user input is not equal to secret number
                            if(secret_number!=guess_number):
                                guess_number=int(input("Enter a number between 1 and 10 : "))
                                if(secret_number==guess_number):
                                    print("Player Wins... and Computer looses...")    #player wins

                                elif(secret_number<guess_number):
                                    print("TOO HIGH Computer wins.. and Player looses...")
                                else:
                                    print("TOO LOW Computer wins.. and Player looses...")
                                numberoftries-=1
                                print("Number of tries left: ", numberoftries)
                        else:
                            print("Sorry you are out of tries")
                            break
                    #end of play again
            elif(secret_number<guess_number):
                print("TOO HIGH Computer wins.. and Player looses...")
            else:
                print("TOO LOW Computer wins.. and Player looses...")
            numberoftries-=1
            print("Number of tries left: ", numberoftries)
    else:
        print("Sorry you are out of tries")
        break
    