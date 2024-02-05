import pygame
import random
pygame.init()
pygame.mixer.init()

SCREENWIDTH = 500
SCREENHEIGHT = 500
WINDOWSCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption('Pong')
CLOCK = pygame.time.Clock()
FPS = 60
bg_img_1 = pygame.image.load('pong img 1.png').convert_alpha()
bg_img_1 = pygame.transform.scale(bg_img_1,(20,500))
FONT = pygame.font.SysFont('inkfree',40,True)
SCORE1 = 0
SCORE2 = 0
pygame.mixer.music.load('Pong Bg Music.mp3')
pygame.mixer.music.play(-1)

def WELCOME(SCORE1,SCORE2):
    ENDGAME = False
    bg_img_2 = pygame.transform.scale(pygame.image.load('pong logo.png').convert_alpha(),(500,500))
    while ENDGAME == False:
        WINDOWSCREEN.blit(bg_img_2,(0,0))
        pygame.display.update()
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ENDGAME = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    GAMELOOP(SCORE1,SCORE2)
                    ENDGAME = True

def GAMELOOP(SCORE1,SCORE2):
    ENDGAME = False
    POSY1 = 200
    POSY2 = 200
    VY1 = 0
    VY2 = 0
    CPOSY = 250
    CPOSX = 250
    CVX = 0
    CVY = 0
    CVX_mod = (random.randint(30,70))/10
    if CVX_mod <= 5:
        CVY_mod = (25-(CVX_mod)**2)**(1/2)
    else:
        CVY_mod = ((CVX_mod)**2-25)**(1/2)
    CVY_decider = random.randint(0,1)
    CVX_decider = random.randint(0,1)

    while ENDGAME == False:

        WINDOWSCREEN.fill((0,0,0))
        WINDOWSCREEN.blit(bg_img_1,(240,0))
        Rect1 = pygame.draw.rect(WINDOWSCREEN,(255,255,255),(20,POSY1,10,100))
        Rect2 = pygame.draw.rect(WINDOWSCREEN,(255,255,255),(470,POSY2,10,100))
        WINDOWSCREEN.blit(FONT.render(f"{SCORE1}",True,(255,255,255)),(120,0))
        WINDOWSCREEN.blit(FONT.render(f"{SCORE2}",True,(255,255,255)),(370,0))
        Ball = pygame.draw.circle(WINDOWSCREEN,(255,0,0),(CPOSX,CPOSY),10)
        pygame.display.update()
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ENDGAME = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    VY2 = -10
                if event.key == pygame.K_DOWN:
                    VY2 = 10
                if event.key == pygame.K_w:
                    VY1 = -10
                if event.key == pygame.K_s:
                    VY1 = 10
                if event.key == pygame.K_SPACE:
                    if CVY_decider == 0:
                        CVY = CVY_mod
                    else:
                        CVY = -CVY_mod
                    if CVX_decider == 0:
                        CVX = CVX_mod
                    else:
                        CVX = -CVX_mod
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    VY2 = 0
                if event.key == pygame.K_DOWN:
                    VY2 = 0
                if event.key == pygame.K_w:
                    VY1 = 0
                if event.key == pygame.K_s:
                    VY1 = 0
        
        if POSY1 > 400:
            POSY1 = 400
        if POSY1 < 0:
            POSY1 = 0
        if POSY2 > 400:
            POSY2 = 400
        if POSY2 < 0:
            POSY2 = 0

        POSY1 = POSY1 + VY1
        POSY2 = POSY2 + VY2

        if CPOSX <= 3 and CPOSX >=-3:
            SCORE2 = SCORE2 + 1
            GAMELOOP(SCORE1,SCORE2)
            ENDGAME = True
        if CPOSY <= 3 and CPOSY >=-3:
            CVY = -CVY
        if CPOSX <= 503 and CPOSX >= 497:
            SCORE1 = SCORE1 + 1
            GAMELOOP(SCORE1,SCORE2)
            ENDGAME = True
        if CPOSY <= 503 and CPOSY >=497:
            CVY = -CVY
        
        if CPOSX <= 35 and CPOSX >=25 and CPOSY>= POSY1 and CPOSY <= POSY1+100:
            CVX = -CVX
        if CPOSX <= 475 and CPOSX >=465 and CPOSY>= POSY2 and CPOSY <= POSY2+100:
            CVX = -CVX

        CPOSX = CPOSX + CVX
        CPOSY = CPOSY + CVY
WELCOME(SCORE1,SCORE2)