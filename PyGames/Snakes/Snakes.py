import pygame
import random
pygame.init()
pygame.mixer.init()
screenWidth = 500
screenHeight = 500
font1 = pygame.font.SysFont("inkfree", 30,True)
font2 = pygame.font.SysFont("inkfree", 80)
font3 = pygame.font.SysFont("inkfree", 40)


def screen_Text(text,colour,posx,posy):
    screenText = font1.render(text, True, colour)
    windowScreen.blit(screenText,[posx,posy])
def plot_Snake(screen,colour,snakeList,l,w):
    for item in snakeList:
        if snakeList.index(item) % 2 == 0:
            pygame.draw.rect(screen,colour,[item[0],item[1],l,w])
        else:
            pygame.draw.rect(screen,(255,0,0),[item[0],item[1],l,w])
def welcome():
    cont = False
    while cont == False:
        windowScreen.fill((100,100,100))
        windowScreen.blit(bgimg1,(0,0))
        windowScreen.blit(bgimg3,(100,100))
        screentext1 = font2.render("nake",True,(230,210,0))
        screentext2 = font3.render("Press Spacebar To Begin!",True,(230,210,0))
        windowScreen.blit(screentext1,[180,120])
        windowScreen.blit(screentext2,[40,250])
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                cont = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
                    cont = True
# Display screen
windowScreen = pygame.display.set_mode((screenWidth, screenHeight)) 
pygame.display.set_caption("Snake")
bgimg1 = pygame.image.load('bg.jpg')
bgimg1 = pygame.transform.scale(bgimg1, (screenWidth, screenHeight)).convert_alpha()
bgimg2 = pygame.image.load('bg1.jpg')
bgimg2 = pygame.transform.scale(bgimg2, (screenWidth, screenHeight)).convert_alpha()
bgimg3 = pygame.image.load('snake.png')
bgimg3 = pygame.transform.scale(bgimg3, (90,130)).convert_alpha()
def gameloop():
    with open ("Highscore(Snakes).txt","r") as f:
        highscore = f.read()
    # Game specific variables
    gameOver = False 
    endGame = False
    white = (255,255,255)
    black = (0,0,0)
    red = (255,0,0)
    blue = (0,0,255)
    xPos = 250
    yPos = 250
    xV = 0
    yV = 0
    length = 10
    width = 10
    clock = pygame.time.Clock()
    fps = 60
    foodX = random.randint(20,480)
    foodY = random.randint(35,480)
    score = 0
    snakeList = [[xPos,yPos]]
    snakeLength = 1
    
    # Game loop
    while endGame == False:
        if gameOver == True:
            windowScreen.fill(white)
            windowScreen.blit(bgimg1,(0,0))
            if score>int(highscore):
                with open ("Highscore(Snakes).txt",'w') as f:
                    f.write(f"{score}")
            screen_Text('Game Over!', red, 150,180)
            screen_Text(f'Your Score: {score}',red,140,220)
            screen_Text('Previous High Score: '+ highscore,red,65,260)
            screen_Text('Press enter to play again',red,60,300)
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()
                        endGame = True
                if event.type == pygame.QUIT:
                    endGame = True
        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        xV = 3
                        yV = 0
                    if event.key == pygame.K_LEFT:
                        xV = -3
                        yV = 0
                    if event.key == pygame.K_UP:
                        yV = -3
                        xV = 0
                    if event.key == pygame.K_DOWN:
                        yV = 3
                        xV = 0
                if event.type == pygame.QUIT:
                    endGame = True
            xPos = xPos + xV
            yPos = yPos + yV
            if abs(xPos-foodX)<11 and abs(yPos-foodY)<11:
                score = score + 1
                foodX = random.randint(20,480)
                foodY = random.randint(40,480)
                snakeLength = snakeLength + 6
                pygame.mixer.music.load('winmusic.mp3')
                pygame.mixer.music.play()

            if xPos<10 or xPos>495 or yPos<35 or yPos>490:
                pygame.mixer.music.load('bgmusic.mp3')
                pygame.mixer.music.play()
                gameOver = True
            if [xPos,yPos] in snakeList[:-1]:
                pygame.mixer.music.load('bgmusic.mp3')
                pygame.mixer.music.play()
                gameOver = True

            snakeList.append([xPos,yPos])
            if len(snakeList)>snakeLength:
                del snakeList[0]
            windowScreen.fill((0,255,0))
            windowScreen.blit(bgimg2,(0,0))
            pygame.draw.rect(windowScreen,black,[1,30,498,470],3)
            pygame.draw.rect(windowScreen,red,[foodX,foodY,length,width])
            plot_Snake(windowScreen,black,snakeList,length,width)
            screen_Text(f"Score: {score}",blue,200,-5)
        clock.tick(fps)
        pygame.display.update()   
welcome()