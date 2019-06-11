# bricks

small=1
large=5

list1=list(map(int,(input("Enter the no of small brick, no. of large brick, size of target brick")).split()))

def target_check(list1):
    if(True):
        for no_small in range(0,list1[0]+1):
            for no_large in range(0,list1[1]+1):
                if(list1[2]==(no_small*small + no_large*large)):
                    return True
    return False
    

print(target_check(list1))