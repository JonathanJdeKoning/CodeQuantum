#!/bin/python3

# Import library code
from p5 import *
from random import randint, seed
from obstacle import Obstacle
from flag import Flag
from goldenflag import Gold
from BigTree import Big
from time import sleep

score = 0
speed = 2
#highscore = 0
#with open("highscore.txt", "r") as file:
#    highscore = int(file.read())
    

def draw_tree(ob_x,ob_y):
    no_stroke()
    fill(0,255,0)
    triangle(ob_x + 20, ob_y + 20, ob_x + 10, ob_y + 40, ob_x + 30, ob_y + 40)
    triangle(ob_x + 20, ob_y + 30, ob_x + 5, ob_y + 55, ob_x + 35, ob_y + 55)
    triangle(ob_x + 20, ob_y + 40, ob_x + 0, ob_y + 70, ob_x + 40, ob_y + 70)
    fill(150,100,100)
    rect(ob_x + 15, ob_y + 70, 10, 10)

def draw_big(ob_x,ob_y):
    no_stroke()
    fill(0,255,0)
    triangle(ob_x, ob_y, ob_x + 40, ob_y + 80, ob_x -40, ob_y +80)
    triangle(ob_x, ob_y+30, ob_x + 50, ob_y + 110, ob_x -50, ob_y +110)
    triangle(ob_x, ob_y+60, ob_x + 60, ob_y + 140, ob_x -60, ob_y +140)

    fill(150,100,100)
    rect(ob_x -15, ob_y + 140, 30, 30)

def draw_flag(ob_x, ob_y):    
    no_stroke()
    fill(255,0,0)
    triangle(ob_x, ob_y+12, ob_x, ob_y + 40, ob_x + 30, ob_y + 20)
    fill(50)
    rect(ob_x, ob_y+12, 5, 35)
    fill(255,0,0)
    
def draw_gold(ob_x, ob_y):    
    no_stroke()
    fill(255,215,0)
    triangle(ob_x, ob_y+10, ob_x, ob_y + 40, ob_x + 30, ob_y + 20)
    rect(ob_x, ob_y + 37, 5, 10)
    
# The draw_player function goes here
def draw_player():
    global score, speed, skiing, crashed, safe2, safe3, player_x, player_y
    
    player_x = 50
    
    fill(safe)
    
    collide = get(player_x, mouse_y).hex
    fill(255,0,0)
    if collide == safe.hex or collide == safe2.hex or collide == safe3.hex:

        image(skiing, player_x, mouse_y, 30, 30)
        #rect(player_x+13, mouse_y+15, 3,3)

        
    else:
        text("🐓", player_x, mouse_y, 30,30)
        #image(crashed, player_x, mouse_y, 30, 30)
        speed = 0
        fill(255,0,0)
    return player_x+15, mouse_y+10

    
  
def setup(): 
    # Setup your animation here
    size(1080, 720)
    text_size(40)
    text_align(CENTER, TOP)  # position around the centre
    global skiing, crashed, trees, flags, gold, bigs
    skiing = load_image('skiing.png')
    crashed = load_image('fallenover.png')

    trees = []
    for i in range(8):
        tree_x = randint(600,1400)
        tree_y = randint(0,700)
        trees.append(Obstacle(tree_x,tree_y))


    flags = []
    for i in range(5):
        flag_x = randint(600,1400)
        flag_y = randint(0,700)
        flags.append(Flag(flag_x,flag_y))
   
    bigs = []
    for i in range(2):
        big_x = randint(600,1400)
        big_y = randint(0,700)
        bigs.append(Big(big_x,big_y))

    gold = None
    gold_x = randint(600,1400)
    gold_y = randint(0,700)
    gold = Gold(gold_x,gold_y)






def draw():
    # Things to do in every frame
    global score, safe, safe2, safe3, speed, skiing, crashed, trees,\
            flags, gold,bigs,highscore
    safe = Color(255)
    background(safe) 



    
    if speed > 0:
        prevspeed = speed
        speed = (score//20)+2
        if speed != prevspeed:
            
            for tree in trees:
                tree.dx = -speed - randint(1,2)
            for flag in flags:
                flag.dx = -speed - randint(1,2)
            for big in bigs:
                big.dx = -speed - randint(1,2)
            gold.dx = -speed*3 - randint(1,2)
        fill(50)
        text('Score: ' + str(score), width/2, 20)
        player_x, player_y = draw_player()

        draw_gold(gold.x, gold.y)

        for tree in trees:
            draw_tree(tree.x, tree.y)
            newx, newy = tree.update()
            cent_x , cent_y = newx+20, newy+50
            if newx < 0:
                tree.move(randint(1080,1400), randint(0,700))
            x_dist = abs(cent_x - player_x)
            y_dist = abs(cent_y - player_y)
    
            if (x_dist < 35) and (y_dist < 25):
                speed = 0
                tree.move(randint(1080,1400), randint(0,700))

        for big in bigs:
            draw_big(big.x, big.y)
            newx, newy = big.update()
            cent_x , cent_y = newx, newy+80
            if newx < 0:
                big.move(1080, randint(0,700))
            x_dist = abs(cent_x - player_x)
            y_dist = abs(cent_y - player_y)
    
            if (x_dist < 60) and (y_dist < 75):
                speed = 0
                big.move(randint(1080,1400), randint(0,700))
        
        for flag in flags:
            draw_flag(flag.x, flag.y)
            
            newx, newy = flag.update()
            cent_x, cent_y = newx+10, newy+30
            if newx < 0:
                flag.move(randint(1080,1400), randint(0,700))
            x_dist = abs(cent_x - player_x)
            y_dist = abs(cent_y - player_y)

            if (x_dist < 20) and (y_dist < 40):
                score += 5
                flag.move(randint(1080,1400), randint(0,700))
            
        newx, newy = gold.update()
        cent_x, cent_y = newx+10, newy+30
        if newx < 0:
            gold.move(randint(1080,1400), randint(0,700))
        x_dist = abs(cent_x - player_x)
        y_dist = abs(cent_y - player_y)

        if (x_dist < 20) and (y_dist < 40):
            score += 10
            gold.move(1080, randint(0,700))



            
    else:
        #if score > highscore:
        #    highscore = score
        #    with open("highscore", "w") as file:
        #        file.write(highscore)
        
        fill(50,50,50)
        text('Game Over', width/2, 20)
        if score == 0:
            text("You didn't get ANY points! What a loser smh", width/2, 60)
        elif score < 50:
            text(f"Only a novice skier scores {score} points. Do better", width/2,60)
        elif score < 100:
            text(f"{score} points? I'm not impressed", width/2, 60)
        elif score < 150:
            text(f"Finally you make it to the triple digits ", width/2, 60)
            text(f"with {score} points. It's still a meh score though. Try again", width/2, 100)
        elif score < 200:
            text(f"Ooh, {score} points. We're warming up now", width/2, 60)
        elif score < 250:
            text(f"{score} points? Pretty good skiing for a cat.", width/2, 60)
        elif score < 300:
            text(f"Okay buddy, {score} points? You've got some moves.", width/2, 60)
        elif score < 400:
            text(f"{score} points? that's my best score :(", width/2, 60)
        elif score == 420:
            text(f"{score}. Nice", width/2, 60)
        elif score >= 400:
            text(f"{score} POINTS??? You've outclassed the master.", width/2, 60)
        

#text(f'You scored {score} points', width/2, 60)
        #text(f'HIGHSCORE: {highscore}', width/2, 100)



run()
