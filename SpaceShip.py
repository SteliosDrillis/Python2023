import pygame
import random
from sqlite3 import Error
from random import randint

pygame.init()

# ΔΙΑΣΤΑΣΕΙΣ ΔΙΑΣΤΗΜΟΠΛΟΙΟΥ
SPACESHIP_WIDTH = 50
SPACESHIP_HEIGHT = 50

# ΔΙΑΣΤΑΣΕΙΣ ΠΛΑΝΗΤΩΝ
PLANET_WIDTH = 50
PLANET_HEIGHT = 50

# ΔΙΑΣΤΑΣΕΙΣ ΔΙΑΜΑΝΤΙΩΝ
DIAMOND_WIDTH = 25
DIAMOND_HEIGHT = 25

# ΔΙΑΣΤΑΣΕΙΣ ΟΘΟΝΗΣ
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# ΧΡΩΜΑΤΑ
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)

# ΔΙΑΜΑΝΤΙΑ 
DIAMOND_START_Y = -25
DIAMOND_SPEED = 3
DIAMOND_WIDTH = 25

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH,DISPLAY_HEIGHT))
pygame.display.set_caption('ΒΟΛΤΑ ΣΤΟ ΔΙΑΣΤΗΜΑ.')
clock = pygame.time.Clock()

# ΕΙΚΟΝΑ ΟΧΗΜΑΤΟΣ - ΠΑΙΧΝΙΔΙΟΥ - ΠΛΑΝΗΤΩΝ - ΔΙΑΜΑΝΤΙΩΝ
SpaceShipImg = pygame.image.load('SpaceShip.PNG')
DEFAULT_SpaceShipImg_SIZE = (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
SpaceShipImg = pygame.transform.scale(SpaceShipImg, DEFAULT_SpaceShipImg_SIZE)

planetImg = pygame.image.load('planet1.gif')
DEFAULT_planetImg_SIZE = (PLANET_WIDTH, PLANET_HEIGHT)
planetImg = pygame.transform.scale(planetImg, DEFAULT_planetImg_SIZE)

diamondImg = pygame.image.load('diamond_image.png')
DEFAULT_diamondImg_SIZE = (DIAMOND_WIDTH, DIAMOND_HEIGHT)
diamondImg = pygame.transform.scale(diamondImg, DEFAULT_diamondImg_SIZE)

gameIcon = pygame.image.load('SpaceShip.PNG')
pygame.display.set_icon(gameIcon)

# ΕΙΚΟΝΑ ΦΟΝΤΟΥ
bg_img = pygame.image.load('bg_img.jpg')
bg_img = pygame.transform.scale(bg_img,(DISPLAY_WIDTH,DISPLAY_HEIGHT))

# ΗΧΟΣ
crash_sound = pygame.mixer.Sound("crash_sound.wav")
get_diamond_sound = pygame.mixer.Sound("get_diamond_sound.mp3")

pygame.mixer.music.load('back_music.wav')
pygame.mixer.music.play(-1)

pause = False

# ΚΕΙΜΕΝΟ ΠΟΝΤΩΝ
def score(count):
    font = pygame.font.SysFont(None, 20)
    text = font.render("ΠΟΝΤΟΙ: "+str(count), True, RED)
    gameDisplay.blit(text,(0,0))

# ΚΕΙΜΕΝΟ ΡΕΚΟΡ
def highscore(score):
    font = pygame.font.SysFont(None, 20)
    text = font.render("ΡΕΚΟΡ: "+str(score), True, RED)
    gameDisplay.blit(text,(700,0))    

# ΠΛΑΝΗΤΕΣ
def planet(planetx, planety, planetw, planeth):
    gameDisplay.blit(planetImg, [planetx, planety, planetw, planeth])   

# ΔΙΑΜΑΝΤΙΑ
def diamond(diamondx, diamondy, diamondw, diamondh):
    gameDisplay.blit(diamondImg, [diamondx, diamondy, diamondw, diamondh])       

def rocket(x,y):
    gameDisplay.blit(SpaceShipImg, (x,y))  
 
# ΠΑΥΣΗ ΠΑΙΧΝΙΔΙΟΥ
def paused():
    pygame.mixer.music.pause()

    font = pygame.font.SysFont ("Verdana", 55)
    text = font.render ("ΠΑΥΣΗ", True, RED)
    text_rect = text.get_rect(center=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3))
    gameDisplay.blit (text, text_rect)
    
    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button("ΣΥΝΕΧΙΣΕ",100,450,150,50,GREEN,GREEN,unpause)
        button("ΕΞΟΔΟΣ",550,450,150,50,RED,RED,quitgame)

        pygame.display.update()
        clock.tick(15)      
    
# ΚΕΙΜΕΝΟ ΤΡΑΚΑΡΙΣΜΑ
def crash():
    pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()

#    if current_score > high_score:
#        font = pygame.font.SysFont ("Arial", 55)
 #       text = font.render ("ΜΠΡΑΒΟ ΝΕΟ ΡΕΚΟΡ", True, RED)
 #       text_rect = text.get_rect(center=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3))
 #       gameDisplay.blit (text, text_rect)
        

    font = pygame.font.SysFont ("Verdana", 55)
    text = font.render ("ΤΡΑΚΑΡΕΣ", True, RED)
    text_rect = text.get_rect(center=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/3))
    gameDisplay.blit (text, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        button("ΠΑΙΞΕ ΞΑΝΑ!",100,450,150,50,GREEN,GREEN,game_loop)
        button("ΕΞΟΔΟΣ.",550,450,150,50,RED,RED,quitgame)

        pygame.display.update()
        clock.tick(15)  

# ΑΡΧΙΚΗ ΟΘΟΝΗ
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        gameDisplay.blit(bg_img, (0, 0))
        font = pygame.font.SysFont ("Verdana", 55)
        text = font.render ("ΒΟΛΤΑ ΣΤΟ ΔΙΑΣΤΗΜΑ.", True, RED)
        text_rect = text.get_rect(center=(DISPLAY_WIDTH/2, DISPLAY_HEIGHT/2))
        gameDisplay.blit (text, text_rect)

        button("ΞΕΚΙΝΑ!",100,450,150,50,GREEN,GREEN,game_loop)
        button("ΕΞΟΔΟΣ",550,450,150,50,RED,RED,quitgame)

        pygame.display.update()
        clock.tick(15)

# ΠΑΙΡΝΩ ΡΕΚΟΡ ΑΠΟ ΑΡΧΕΙΟ
def get_high_score():
    high_score = 0
 
    high_score_file = open("high_score.txt", "r")
    high_score = int(high_score_file.read())
    high_score_file.close()
 
    return high_score  

# ΣΩΖΩ ΡΕΚΟΡ
def save_high_score(new_high_score):
    high_score_file = open("high_score.txt", "w")
    high_score_file.write(str(new_high_score))
    high_score_file.close()
    
# ΚΟΥΜΠΙΑ
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))

    font = pygame.font.SysFont ("Verdana", 20)
    text = font.render (msg, True, BLACK)
    text_rect = text.get_rect(center=(x+(w/2), y+(h/2)))
    gameDisplay.blit (text, text_rect)

def quitgame():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.music.unpause()
    pause = False    

def game_loop():
    global pause

    # ΜΟΥΣΙΚΗ ΦΟΝΤΟΥ
    pygame.mixer.music.load('back_music.wav')
    pygame.mixer.music.play(-1)

    # ΘΕΣΗ ΔΙΑΣΤΗΜΟΠΛΟΙΟΥ
    x = (DISPLAY_WIDTH/2 - SPACESHIP_WIDTH/2)
    y = (DISPLAY_HEIGHT - 2*SPACESHIP_WIDTH)

    x_change = 0

    # ΠΛΑΝΗΤΕΣ 
    planet_startx = random.randrange(0, DISPLAY_WIDTH-50)
    planet_starty = -50
    planet_speed = 4
    planet_width = 50
    planet_height = 50

    # ΔΙΑΜΑΝΤΙΑ 
    diamond_startx = random.randrange(0, DISPLAY_WIDTH-25)
    DIAMOND_START_Y = -25
    DIAMOND_SPEED = 3
    DIAMOND_WIDTH = 25
    DIAMOND_HEIGHT = 25

    current_score = 0
    high_score = 0

    high_score = get_high_score()

    gameExit = False

    while not gameExit:
        # ΚΙΝΗΣΗ ΔΙΑΣΤΗΜΟΠΛΟΙΟΥ
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_p:
                    pause = True
                    paused()    

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0    

        x += x_change

        # ΦΟΝΤΟ ΕΙΚΟΝΑ
        gameDisplay.blit(bg_img,(0,0))

        # SAVE HIGH SCORE
        if current_score > high_score:
            save_high_score(current_score)

        rocket(x,y)
        score(current_score)
        highscore(high_score)

        # ΤΡΑΚΑΡΙΣΜΑ ΔΕΞΙΑ ΑΡΙΣΤΕΡΑ
        if x > DISPLAY_WIDTH - SPACESHIP_WIDTH or x < 0:
            crash()

        # ΔΗΜΙΟΥΡΓΙΑ ΠΛΑΝΗΤΩΝ
        planet(planet_startx, planet_starty, planet_width, planet_height)
        planet_starty += planet_speed

        if planet_starty > DISPLAY_HEIGHT:
            planet_starty = 0 - planet_height
            planet_startx = random.randrange(0,DISPLAY_WIDTH-50)
            planet_speed += 0.2 

        # ΔΗΜΙΟΥΡΓΙΑ ΔΙΑΜΑΝΤΙΩΝ
        diamond(diamond_startx, DIAMOND_START_Y, DIAMOND_WIDTH, DIAMOND_HEIGHT)
        DIAMOND_START_Y += DIAMOND_SPEED

        if DIAMOND_START_Y > DISPLAY_HEIGHT:
            diamondImg.set_alpha(255)
            DIAMOND_START_Y = 0 - DIAMOND_HEIGHT
            diamond_startx = random.randrange(0,DISPLAY_WIDTH-25)
            DIAMOND_SPEED += 0.1       


        # ΤΡΑΚΑΡΙΣΜΑ ΜΕ ΠΛΑΝΗΤΗ
        if y < planet_starty+planet_height and y>planet_starty-planet_height:
            if x > planet_startx and x < planet_startx + planet_width or x+SPACESHIP_WIDTH > planet_startx and x + SPACESHIP_WIDTH < planet_startx+planet_width:
                crash()

        # ΜΑΖΕΥΩ ΔΙΑΜΑΝΤΙΑ
        if y < DIAMOND_START_Y+DIAMOND_HEIGHT and y>DIAMOND_START_Y-DIAMOND_HEIGHT:     
            if x > diamond_startx-DIAMOND_WIDTH and x+DIAMOND_WIDTH/2 < diamond_startx + DIAMOND_WIDTH or x+SPACESHIP_WIDTH > diamond_startx and x + SPACESHIP_WIDTH < diamond_startx+DIAMOND_WIDTH:
                DIAMOND_START_Y = 10000
                diamondImg.set_alpha(0)
                current_score += 1    
                pygame.mixer.Sound.play(get_diamond_sound)
                pygame.mixer.music.stop()

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()