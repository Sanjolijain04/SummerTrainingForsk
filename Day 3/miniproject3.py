#python hangman game

import random
#initialize list
fruits=['apple','banana','mango','litchy','peer','papaya']

#random fruit from system
secret=random.randint(0,len(fruits)-1)
sec_fruit=fruits[secret]
print(sec_fruit)

emp_string="-"*len(sec_fruit)



#guess fuction
#taking character by character guess by user
def find_fruit():
    tries=len(sec_fruit)
    while(True):  #iterate till number of tries>0
        if(tries>0):
            if "-" not in emp_string:
                print("Player Wins...guess was{}".format(sec_fruit))
                break
            else:
                guess=input("Enter a character: ")
                if guess not in sec_fruit:
                    print("Wrong guess.. Try Again")
                    tries-=1
                    print("Number of tries left are {}".format(tries))
                    
                else:
                    for item in sec_fruit:
                        if item==guess:
                            emp_string=emp_string[sec_fruit.find(item)].replace("-",guess)
                        print(emp_string)
                        
                    
                            
                    
        else:
            print("Player looses... You are out of tries")
            break
            
    
find_fruit()





                    