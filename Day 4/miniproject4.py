# Python Dungeon game

import random
#make grid list
CELLS = [
(0,0),(0,1),(0,2) ,
(1,0),(1,1),(1,2) ,
(2,0),(2,1),(2,2)
]


#get location of monster, player and door
def get_location():
    monster=random.choice(CELLS)
    player=random.choice(CELLS)
    door=random.choice(CELLS)
    if monster==door or monster==player or player==door:
        return get_location()
    return monster, player, door


#draw map
def draw_map(player):
    print(" _ _ _ ")
    tile='|{}'
    for idx,cell in enumerate(CELLS) :
        if idx in(0,2,3,4,6,7):
            if(cell==player):
                print(tile.format("X"), end="")
            else:
                print(tile.format("_"), end="")
        else:
            if(cell==player):
                print(tile.format("X|"))
            else:
                print(tile.format("_|"))
        
            
        
                
    
#get moves from user
def get_moves(player):
    moves=['UP','DOWN','LEFT','RIGHT']
    x,y=player 
    if(x==0):
        moves.remove('LEFT')
    if(x==2):
        moves.remove('RIGHT')
    if(y==0):
        moves.remove('UP')
    if(y==2):
        moves.remove('DOWN')
    return moves

#mover player defination
def move_player(player,move):
    x,y=player
    if(move=="RIGHT"):
        x+=1
    if(move=="LEFT"):
        x-=1
    if(move=="UP"):
        y-=1
    if(move=="DOWN"):
        y+=1
    return x,y
        
    

# game start 
def game_loop():
    monster,door,player=get_location()
    
    while(True):
        draw_map(player)
        valid_move=get_moves(player)
        
        print("You are currently in room {}".format(player))
        print("You can move {}".format(",".join(valid_move)))
        print("Enter 'quit' to quit the game")
        
        move=input(">").upper()
        if(move=='QUIT'):
            break
        elif move not in ['LEFT','RIGHT','UP','DOWN']:
            input("Please Enter the correct move: ")
            continue
        elif move in valid_move:
            player=move_player(player,move)
        else:
            input(" You hit the boundry, Enter choice again: ")
game_loop()


    
    


