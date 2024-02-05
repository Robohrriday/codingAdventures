import pygame
from pygame.constants import MOUSEBUTTONDOWN
pygame.init()

SCREENWIDTH = 500
SCREENHEIGHT = 500
WINDOWSCREEN = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
pygame.display.set_caption("Conway's Game of Life")
LIVE_LIST = []
DEAD_LIST = []
NEIGHBOURS = {}
DEAD_NEIGHBOURS = {}
IMG = pygame.image.load("Conway's GOL BG.png").convert_alpha()
CLOCK = pygame.time.Clock()

def start_Simulation():
    ENDPROG = False
    while ENDPROG == False:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ENDPROG = True
        for item in LIVE_LIST:
            count = 0
            if [item[0]+10,item[1]+10] in LIVE_LIST:
                count = count + 1
            else:
                DEAD_LIST.append([item[0]+10,item[1]+10])
            
            if [item[0]+10,item[1]] in LIVE_LIST:
                count = count + 1
            else:
                DEAD_LIST.append([item[0]+10,item[1]])
            
            if [item[0]+10,item[1]-10] in LIVE_LIST:
                count = count + 1
            else:
                DEAD_LIST.append([item[0]+10,item[1]-10])
            
            if [item[0],item[1]+10] in LIVE_LIST:
                count = count + 1
            else:
                DEAD_LIST.append([item[0],item[1]+10])
            
            if [item[0],item[1]-10] in LIVE_LIST:
                count = count + 1
            else:
                DEAD_LIST.append([item[0],item[1]-10])

            if [item[0]-10,item[1]+10] in LIVE_LIST:
                count = count + 1
            else:
                DEAD_LIST.append([item[0]-10,item[1]+10])

            if [item[0]-10,item[1]] in LIVE_LIST:
                count = count + 1
            else:
                DEAD_LIST.append([item[0]-10,item[1]])

            if [item[0]-10,item[1]-10] in LIVE_LIST:
                count = count + 1
            else:
                DEAD_LIST.append([item[0]-10,item[1]-10])

            NEIGHBOURS.update({str(item[0])+"-"+str(item[1]):count})
        
        for item in LIVE_LIST:
            if NEIGHBOURS[str(item[0])+"-"+str(item[1])] <= 1:
                LIVE_LIST.remove(item)
                NEIGHBOURS.pop(str(item[0])+"-"+str(item[1]))
            elif NEIGHBOURS[str(item[0])+"-"+str(item[1])] == 2 or NEIGHBOURS[str(item[0])+"-"+str(item[1])] == 3:
                pass
            elif NEIGHBOURS[str(item[0])+"-"+str(item[1])] >= 4:
                LIVE_LIST.remove(item)
                NEIGHBOURS.pop(str(item[0])+"-"+str(item[1]))

        for item in DEAD_LIST:
            dead_count = DEAD_LIST.count(item)
            if dead_count == 3:
                DEAD_NEIGHBOURS.update({str(item[0])+"-"+str(item[1]):None})
        
        for item in list(DEAD_NEIGHBOURS.keys()):
            Index = item.index("-")
            LIVE_LIST.append([int(item[:Index]),int(item[Index+1:])])

        DEAD_NEIGHBOURS.clear()
        DEAD_LIST.clear()

        WINDOWSCREEN.blit(IMG,(0,0))
        for item in LIVE_LIST:
            pygame.draw.rect(WINDOWSCREEN,(255,0,0),(item[0],item[1],9,9))
        pygame.display.update()
        CLOCK.tick(1)

def initiation():
    ENDPROG = False
    while ENDPROG == False:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                ENDPROG = True
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    for item in LIVE_LIST:
                        NEIGHBOURS.update({str(item[0])+"-"+str(item[1]):None})
                    start_Simulation()
                    ENDPROG = True
            if e.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                mouse_pos_x = int(mouse_pos[0]/10)*10
                mouse_pos_y = int(mouse_pos[1]/10)*10
                if [mouse_pos_x,mouse_pos_y] in LIVE_LIST:
                    LIVE_LIST.remove([mouse_pos_x,mouse_pos_y])
                else:
                    LIVE_LIST.append([mouse_pos_x,mouse_pos_y])
        WINDOWSCREEN.blit(IMG,(0,0))
        for item in LIVE_LIST:
            pygame.draw.rect(WINDOWSCREEN,(255,0,0),(item[0],item[1],9,9))
        pygame.display.update()
        CLOCK.tick(60)

initiation()