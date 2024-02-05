import pygame
import random
pygame.init()
pygame.mixer.init()

# Window screen
SCREENWIDTH = 480
SCREENHEIGHT = 500
WINDOW = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption('Speed')

GAME_SPRITES = {
    'VEHICLES': ['car1.png','car2.png','car3.png','car4.png','car5.png','car6.png','car7.png','car8.png'],
    'BACKGROUND': ["bg1.jpg",'road.png'],
    'COORDINATES': [54, 54, 54, 54, 54, 54, 54, 54]
}

FONT = pygame.font.SysFont('inkfree',40)
def screen_TEXT(text,colour,posx,posy):
    screenText = FONT.render(text, True, colour)
    WINDOW.blit(screenText,[posx,posy])


def car_GENERATOR(GAME_SPRITES,CAR_DETAILS):
    random_car = random.randint(0,7)
    random_lane = random.randint(0,2)
    IMAGE = pygame.image.load(GAME_SPRITES['VEHICLES'][random_car])
    IMAGE = pygame.transform.scale(IMAGE,(80,160)).convert_alpha()
    CAR_DETAILS.append([IMAGE,random_lane*150 + GAME_SPRITES['COORDINATES'][random_car],-200])
    return CAR_DETAILS

def car_MOVEMENT(CAR_DETAILS,WINDOW,COORDINATES_LIST):
    for i in range(0,len(CAR_DETAILS)):
        WINDOW.blit(CAR_DETAILS[i][0], (CAR_DETAILS[i][1], CAR_DETAILS[i][2] + COORDINATES_LIST[i]))

def collision_DETECTION(POSX,POSY,COORDINATES_LIST,CAR_DETAILS):
    crash = False
    if POSX <= 15 or POSX >= 385:
        crash = True
    else:
        for i in range (0,len(CAR_DETAILS)):
            if CAR_DETAILS[i][1] - POSX >= -65 and CAR_DETAILS[i][1] - POSX <= 65 and CAR_DETAILS[i][2] + COORDINATES_LIST[i] - POSY >= -145 and CAR_DETAILS[i][2] + COORDINATES_LIST[i] - POSY <= 145:
                crash = True
    return crash

def car_SELECTION(WINDOW, GAME_SPRITES):
    bg_img = pygame.transform.scale(pygame.image.load('Bg Img - Speed.png'),(480,540)).convert_alpha()

    img1 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][0]),(80,160)).convert_alpha()
    img2 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][1]),(80,160)).convert_alpha()
    img3 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][2]),(80,160)).convert_alpha()
    img4 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][3]),(80,160)).convert_alpha()
    img5 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][4]),(80,160)).convert_alpha()
    img6 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][5]),(80,160)).convert_alpha()
    img7 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][6]),(80,160)).convert_alpha()
    img8 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][7]),(80,160)).convert_alpha()

    endgame = False
    clock = pygame.time.Clock()
    while endgame == False:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                endgame = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = list(mouse_pos)
                if mouse_pos[0]>=20 and mouse_pos[0] <= 100 and mouse_pos[1] >= 50 and mouse_pos[1]<=210:
                    car_number = 1
                    endgame = True
                if mouse_pos[0]>=140 and mouse_pos[0] <= 220 and mouse_pos[1] >= 50 and mouse_pos[1]<=210:
                    car_number = 2
                    endgame = True
                if mouse_pos[0]>=260 and mouse_pos[0] <= 340 and mouse_pos[1] >= 50 and mouse_pos[1]<=210:
                    car_number = 3
                    endgame = True
                if mouse_pos[0]>=380 and mouse_pos[0] <= 460 and mouse_pos[1] >= 50 and mouse_pos[1]<=210:
                    car_number = 4
                    endgame = True
                if mouse_pos[0]>=20 and mouse_pos[0] <= 100 and mouse_pos[1] >= 250 and mouse_pos[1]<=410:
                    car_number = 5
                    endgame = True
                if mouse_pos[0]>=140 and mouse_pos[0] <= 220 and mouse_pos[1] >= 250 and mouse_pos[1]<=410:
                    car_number = 6
                    endgame = True
                if mouse_pos[0]>=260 and mouse_pos[0] <= 340 and mouse_pos[1] >= 250 and mouse_pos[1]<=410:
                    car_number = 7
                    endgame = True
                if mouse_pos[0]>=380 and mouse_pos[0] <= 460 and mouse_pos[1] >= 250 and mouse_pos[1]<=410:
                    car_number = 8
                    endgame = True

        WINDOW.blit(bg_img,(0,0))
        WINDOW.blit(img1,(20,50))
        WINDOW.blit(img2,(140,50))
        WINDOW.blit(img3,(260,50))
        WINDOW.blit(img4,(380,50))
        WINDOW.blit(img5,(20,250))
        WINDOW.blit(img6,(140,250))
        WINDOW.blit(img7,(260,250))
        WINDOW.blit(img8,(380,250))
        screen_TEXT('Choose a car',(255,70,70),140,420)

        pygame.display.update()
        clock.tick(60)
    return car_number

def WELCOME(WINDOW,GAME_SPRITES):
    img = pygame.transform.scale(pygame.image.load('Speed Logo.png'),(250,125)).convert_alpha()
    bg_img = pygame.transform.scale(pygame.image.load('Bg Img - Speed.png'),(480,540)).convert_alpha()
    logo = pygame.transform.scale(pygame.image.load('Car selection logo.png'),(50,100)).convert_alpha()
    endgame = False
    clock = pygame.time.Clock()
    car_number = 0
    while endgame == False:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                endgame = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = list(mouse_pos)
                if mouse_pos[0]>=215 and mouse_pos[0] <= 265 and mouse_pos[1] >= 285 and mouse_pos[1]<=385:
                    car_number = car_SELECTION(WINDOW,GAME_SPRITES)
                    endgame = True

        WINDOW.blit(bg_img,(0,0))
        WINDOW.blit(img,(120,150))
        WINDOW.blit(logo,(215,285))
        pygame.display.update()
        clock.tick(60)
    return car_number

def after_CRASH(WINDOW,SCORE,highscore):
    bg_img = pygame.transform.scale(pygame.image.load('Bg Img - Speed.png'),(490,540)).convert_alpha()
    img = pygame.transform.scale(pygame.image.load('Retry Speed.png'),(125,125)).convert_alpha()

    endgame = False
    clock = pygame.time.Clock()

    if SCORE>int(highscore):
        with open ("Highscore(Speed).txt","w") as f:
            f.write(f"{SCORE}")
    while endgame == False:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                endgame = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos = list(mouse_pos)
                if mouse_pos[0]>=178 and mouse_pos[0] <= 303 and mouse_pos[1] >= 200 and mouse_pos[1]<=325:
                    GAMELOOP()
                    endgame = True
                
        WINDOW.blit(bg_img,(-5,0))
        screen_TEXT(f'Score: {SCORE}',(255,70,70),170,100)
        screen_TEXT('Previous high score: '+highscore,(255,70,70),60,150)
        WINDOW.blit(img,(178,200))
        pygame.display.update()
        clock.tick(60)

# Gameloop
def GAMELOOP():
    # Game specific variables
    FPS = 60
    ENDGAME = False
    CLOCK = pygame.time.Clock()
    BGV = 0
    VX = 0
    POSY = 330
    CV = 5
    COORDINATES_LIST = [0]
    CRASH = False
    SCORE = 0 
    CAR_DETAILS = []
    random_no = 1
    random_car = random.randint(0,7)
    random_lane = random.randint(0,2)
    IMAGE = pygame.image.load(GAME_SPRITES['VEHICLES'][random_car])
    IMAGE = pygame.transform.scale(IMAGE,(80,160)).convert_alpha()
    CAR_DETAILS.append([IMAGE,random_lane*150 + GAME_SPRITES['COORDINATES'][random_car],-200])

    img = pygame.transform.scale(pygame.image.load(GAME_SPRITES['VEHICLES'][car_number-1]),(80,160)).convert_alpha()
    POSX = GAME_SPRITES['COORDINATES'][car_number-1] + 150

    img2 = pygame.transform.rotate(pygame.image.load(GAME_SPRITES['BACKGROUND'][1]),90)
    img2 = pygame.transform.scale(img2,(int((SCREENWIDTH-30)/3),2*SCREENHEIGHT)).convert_alpha()
    img1 = pygame.transform.scale(pygame.image.load(GAME_SPRITES['BACKGROUND'][0]),(SCREENWIDTH,SCREENHEIGHT)).convert_alpha()

    with open ("Highscore(Speed).txt","r") as f:
        highscore = f.read()

    pygame.mixer.music.load('Speed bg music.mp3')
    pygame.mixer.music.play(-1)

    while ENDGAME == False:
        if CRASH == True:
            pygame.mixer.music.load('speed crash sound.mp3')
            pygame.mixer.music.play()
            after_CRASH(WINDOW,SCORE,highscore)
            ENDGAME = True
        for EVENT in pygame.event.get():
            if EVENT.type == pygame.QUIT:
                ENDGAME = True
            if EVENT.type == pygame.KEYDOWN:
                if EVENT.key == pygame.K_RIGHT:
                    VX = 5
                if EVENT.key == pygame.K_LEFT:
                    VX = -5

        WINDOW.blit(img1,[0,0])
        
        if BGV < 500:
            WINDOW.blit(img2,[15,-500+BGV])
            WINDOW.blit(img2,[165,-500+BGV])
            WINDOW.blit(img2,[315,-500+BGV])
        else:
            WINDOW.blit(img2,[15,-4])
            WINDOW.blit(img2,[165,-4])
            WINDOW.blit(img2,[315,-4])
            BGV = 0
        BGV = BGV + 8

        POSX = POSX + VX
        if ((POSX - 55)>=-1 and (POSX - 55)<=1) or ((POSX - 205)>=-1 and (POSX - 205)<=1) or ((POSX - 355)>=-1 and (POSX - 355)<=1):
            VX = 0
        
        for item in COORDINATES_LIST:
            if item >= 700:
                i = COORDINATES_LIST.index(item)
                COORDINATES_LIST.remove(item)
                CAR_DETAILS.remove(CAR_DETAILS[i])
                SCORE = SCORE + 1
            else:
                i = COORDINATES_LIST.index(item)
                new_item = item + CV
                COORDINATES_LIST.remove(item)
                COORDINATES_LIST.insert(i,new_item)
                                
                if item == 480:
                    random_no = random.randint(1,2)
                    for i in range (0,random_no):
                        CAR_DETAILS = car_GENERATOR(GAME_SPRITES,CAR_DETAILS)
                        COORDINATES_LIST.append(0)

        if len(CAR_DETAILS) > 4:
            CAR_DETAILS = CAR_DETAILS[0:4]
            COORDINATES_LIST = COORDINATES_LIST[0:4]

        if random_no==2:
            if COORDINATES_LIST[-1] == COORDINATES_LIST[-2] and CAR_DETAILS[-1][1] == CAR_DETAILS[-2][1]:
                COORDINATES_LIST.remove(COORDINATES_LIST[-1])
                CAR_DETAILS.remove(CAR_DETAILS[-1])
                random_no = 0
                


        car_MOVEMENT(CAR_DETAILS, WINDOW,COORDINATES_LIST)
        CRASH = collision_DETECTION(POSX,POSY,COORDINATES_LIST,CAR_DETAILS)

        WINDOW.blit(img,[POSX,POSY])
        screen_TEXT(f'{SCORE}',(255,255,255),225,0)
        pygame.display.update()
        CLOCK.tick(FPS)

car_number = WELCOME(WINDOW,GAME_SPRITES)
GAMELOOP()