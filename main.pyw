import pygame
from buton import buton
from rendertext import rendertext
def clear():
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
    print("                                                                                        ")
def drawGrid(Surface):
    pygame.draw.line(Surface , (255 , 255 ,255) , (160 , 0) , (160 , 480))
    pygame.draw.line(Surface , (255 , 255 ,255) , (320 , 0) , (320 , 480))
    pygame.draw.line(Surface, (255 , 255 ,255) , (0 , 160) , (480 , 160))
    pygame.draw.line(Surface , (255 , 255 ,255) , (0 , 320) , (480 , 320))

def set_list_of_quadrants(coords , whattodraw , list_of_quadrants):
    #sus stanga
    if coords[0] < 160 and coords[1] < 160:
        if whattodraw == 'X':
            if list_of_quadrants[0] == (0,0):
                list_of_quadrants[0] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[0] == (0,0):
                list_of_quadrants[0] = (0,1)
    #stanga
    if coords[0] < 160 and coords[1] < 320 and coords[1] > 160:
        if whattodraw == 'X':
            if list_of_quadrants[3] == (0,0):
                list_of_quadrants[3] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[3] == (0,0):
                list_of_quadrants[3] = (0,1)
    #jos stanga
    if coords[0] < 160 and coords[1] < 480 and coords[1] > 320:
        if whattodraw == 'X':
            if list_of_quadrants[6] == (0,0):
                list_of_quadrants[6] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[6] == (0,0):
                list_of_quadrants[6] = (0,1)

    #sus
    if coords[0] > 160 and coords[0] < 320 and coords[1] < 160:
        if whattodraw == 'X':
            if list_of_quadrants[1] == (0,0):
                list_of_quadrants[1] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[1] == (0,0):
                list_of_quadrants[1] = (0,1)
    #mijloc
    if coords[0] > 160 and coords[0] < 320 and coords[1] > 160 and coords[1] < 320:
        if whattodraw == 'X':
            if list_of_quadrants[4] == (0,0):
                list_of_quadrants[4] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[4] == (0,0):
                list_of_quadrants[4] = (0,1)
    #jos
    if coords[0] > 160 and coords[0] < 320 and coords[1] >320 and coords[1]< 480:
        if whattodraw == 'X':
            if list_of_quadrants[7] == (0,0):
                list_of_quadrants[7] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[7] == (0,0):
                list_of_quadrants[7] = (0,1)
    #sus dreapta
    if coords[0] > 320 and coords[0] < 480 and coords[1] >0 and coords[1]< 160:
        if whattodraw == 'X':
            if list_of_quadrants[2] == (0,0):
                list_of_quadrants[2] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[2] == (0,0):
                list_of_quadrants[2] = (0,1)
    #dreapta
    if coords[0] > 320 and coords[0] < 480 and coords[1] >160 and coords[1]< 320:
        if whattodraw == 'X':
            if list_of_quadrants[5] == (0,0):
                list_of_quadrants[5] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[5] == (0,0):
                list_of_quadrants[5] = (0,1)
    #jos dreapta
    if coords[0] > 320 and coords[0] < 480 and coords[1] >320 and coords[1]< 480:
        if whattodraw == 'X':
            if list_of_quadrants[8] == (0,0):
                list_of_quadrants[8] = (1,0)
        if whattodraw == 'O':
            if list_of_quadrants[8] == (0,0):
                list_of_quadrants[8] = (0,1)


def drawOnQuadrant(Surface , list_of_quadrants):
    quadrant = 0
    for data in list_of_quadrants:
        if data == (1,0):
            if quadrant == 0:
                pygame.draw.line(Surface , (255,255,255) , (0,0) , (160 , 160))
                pygame.draw.line(Surface , (255,255,255) , (0,160) , (160 , 0))
                #sus stanga
            if quadrant == 1:
                pygame.draw.line(Surface , (255,255,255) , (160,0) , (320,160))
                pygame.draw.line(Surface , (255,255,255) , (160 , 160) , (320 , 0))
                #sus
            if quadrant == 2:
                #dreapta sus
                pygame.draw.line(Surface , (255 , 255 ,255) , (320 , 0) , (480 , 160))
                pygame.draw.line(Surface , (255 , 255 ,255) , (320 , 160) , (480 , 0))
            if quadrant == 3:
                #stanga
                pygame.draw.line(Surface , (255 ,255 ,255) , (0,160) , (160 , 320))
                pygame.draw.line(Surface , (255 ,255 ,255) , (0,320) , (160 , 160))
            if quadrant == 4:
                #mijloc
                pygame.draw.line(Surface , (255,255,255) , (160,160) , (320,320))
                pygame.draw.line(Surface , (255,255,255) , (160 , 320) , (320 , 160))
            if quadrant == 5:
                #dreapta
                pygame.draw.line(Surface , (255 , 255 ,255) , (320 , 160) , (480 , 320))
                pygame.draw.line(Surface , (255 , 255 ,255) , (320 , 320) , (480 , 160))
            if quadrant == 6:
                pygame.draw.line(Surface , (255 ,255 ,255) , (0,320) , (160 , 480))
                pygame.draw.line(Surface , (255 ,255 ,255) , (0,480) , (160 , 320))
                #jos stanga
            if quadrant == 7:
                #jos
                pygame.draw.line(Surface , (255,255,255) , (160,320) , (320,480))
                pygame.draw.line(Surface , (255,255,255) , (160 , 480) , (320 , 320))
            if quadrant == 8:
                #dreapta jos
                pygame.draw.line(Surface , (255 , 255 ,255) , (320 , 320) , (480 , 480))
                pygame.draw.line(Surface , (255 , 255 ,255) , (320 , 480) , (480 , 320))
        if data == (0,1):
            if quadrant == 0:
                pygame.draw.ellipse(Surface , (255 , 255 ,255) , (0 , 0 ,160 , 160) ,1 )
                #sus stanga
            if quadrant == 1:
                pygame.draw.ellipse(Surface , (255 ,255 ,255) , (160 , 0 , 160 , 160) , 1)
                #sus
            if quadrant == 2:
                #dreapta sus
                pygame.draw.ellipse(Surface , (255 , 255 ,255) , (320 , 0 , 160 , 160) , 1)
            if quadrant == 3:
                pygame.draw.ellipse(Surface , (255 , 255 ,255) , (0 , 160 , 160 , 160) ,1 )
                #stanga
            if quadrant == 4:
                pygame.draw.ellipse(Surface , (255 ,255 ,255) , (160 , 160 , 160 , 160) , 1)
                #mijloc
            if quadrant == 5:
                #dreapta
                pygame.draw.ellipse(Surface , (255 , 255 ,255) , (320 , 160 , 160 , 160) , 1)
            if quadrant == 6:
                pygame.draw.ellipse(Surface , (255 , 255 ,255) , (0 , 320 ,160 , 160) ,1 )
                #jos stanga
            if quadrant == 7:
                pygame.draw.ellipse(Surface , (255 ,255 ,255) , (160 , 320 , 160 , 160) , 1)
                #jos
            if quadrant == 8:
                #dreapta
                pygame.draw.ellipse(Surface , (255 , 255 ,255) , (320 , 320 , 160 , 160) , 1)
        quadrant += 1

def isGameOver(list_of_quadrants):
    #pentru x
    if list_of_quadrants[0][0] == list_of_quadrants[1][0] == list_of_quadrants[2][0] == 1:
        return 'X' , True
    elif list_of_quadrants[3][0] == list_of_quadrants[4][0] == list_of_quadrants[5][0] == 1:
        return 'X' , True
    elif list_of_quadrants[6][0] == list_of_quadrants[7][0] == list_of_quadrants[8][0] == 1:
        return 'X' , True
    elif list_of_quadrants[0][0] == list_of_quadrants[3][0] == list_of_quadrants[6][0] == 1:
        return 'X' , True
    elif list_of_quadrants[1][0] == list_of_quadrants[4][0] == list_of_quadrants[7][0] == 1:
        return 'X' , True
    elif list_of_quadrants[2][0] == list_of_quadrants[5][0] == list_of_quadrants[8][0] == 1:
        return 'X' , True
    elif list_of_quadrants[0][0] == list_of_quadrants[4][0] == list_of_quadrants[8][0] == 1:
        return 'X' , True
    elif list_of_quadrants[2][0] == list_of_quadrants[4][0] == list_of_quadrants[6][0] == 1:
        return 'X' , True
    #pentru 0
    elif list_of_quadrants[0][1] == list_of_quadrants[1][1] == list_of_quadrants[2][1] == 1:
          return 'O' , True
    elif list_of_quadrants[3][1] == list_of_quadrants[4][1] == list_of_quadrants[5][1] == 1:
        return 'O' , True
    elif list_of_quadrants[6][1] == list_of_quadrants[7][1] == list_of_quadrants[8][1] == 1:
        return 'O' , True
    elif list_of_quadrants[0][1] == list_of_quadrants[3][1] == list_of_quadrants[6][1] == 1:
        return 'O' , True
    elif list_of_quadrants[1][1] == list_of_quadrants[4][1] == list_of_quadrants[7][1] == 1:
        return 'O' , True
    elif list_of_quadrants[2][1] == list_of_quadrants[5][1] == list_of_quadrants[8][1] == 1:
        return 'O' , True
    elif list_of_quadrants[0][1] == list_of_quadrants[4][1] == list_of_quadrants[8][1] == 1:
        return 'O' , True
    elif list_of_quadrants[2][1] == list_of_quadrants[4][1] == list_of_quadrants[6][1] == 1:
        return 'O' , True
    else:
        numOfEmptyQuadrants = 0
        for data in list_of_quadrants:
            if data == (0,0):
                numOfEmptyQuadrants += 1
        if numOfEmptyQuadrants == 0:
            return 'tie' ,True
        else:
            return 'nobody' , False



def game():
    pygame.init()
    width = 480
    height = 480
    win = pygame.display.set_mode((width , height))
    pygame.display.set_caption("X si 0")



    list_of_quadrants = [(0,0) ,(0,0) ,(0,0)
                        ,(0,0) ,(0,0) ,(0,0)
                        ,(0,0) ,(0,0) ,(0,0)];

    player_turn = True
    run = True
    while run:
        winner,is_game_over = isGameOver(list_of_quadrants)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not is_game_over:
                    if event.button == 1:
                        if player_turn == True:
                            set_list_of_quadrants(event.pos , 'X' , list_of_quadrants)
                        if player_turn == False:
                            set_list_of_quadrants(event.pos , 'O' , list_of_quadrants)
                        player_turn = not player_turn
                    else:
                        #debug ; This prints the list of quadrants for debugging purposes
                        clear()
                        print("{} , {} , {}".format(list_of_quadrants[0] , list_of_quadrants[1] , list_of_quadrants[2]))
                        print("{} , {} , {}".format(list_of_quadrants[3] , list_of_quadrants[4] , list_of_quadrants[5]))
                        print("{} , {} , {}".format(list_of_quadrants[6] , list_of_quadrants[7] , list_of_quadrants[8]))

        win.fill((0,0,0))
        drawOnQuadrant(win , list_of_quadrants)
        drawGrid(win)
        pygame.display.update()
        if not (winner == 'nobody'):
            run = False
    return winner
    pygame.quit()


def entryScreen():
    pygame.init()
    fereastra = pygame.display.set_mode((480 , 480))
    pygame.display.set_caption('X si O')
    castigator = rendertext('' , (255 ,255 ,255) , 'Arial' , 50 , fereastra , (110,60))
    butonul_meu = buton((210 , 260 , 80 , 30) , (255 ,255 , 255) , 'Joaca')
    titlu = rendertext('X si O' , (255 ,255 ,255) , 'Arial' , 150 , fereastra , (40 , 100) , True)
    run = True
    while run:
        fereastra.fill((0,0,0))
        winner = butonul_meu.draw(fereastra , game)
        castigator.draw()
        titlu.draw()
        pygame.display.update()
        if not (winner == None):
            if winner == 'nobody':
                #asta se intampla in cazul in care se inchide fereastra cand esti in joc deci dam exit()
                exit()
        if not (winner == None):
            last_winner = winner
        try:
            if last_winner == 'tie':
                castigator.text = 'A fost egalitate'
                castigator.loc = (90,60)
            else:
                castigator.text = '{} a castigat'.format(last_winner)
                castigator.loc = (115 , 60)
        except:
            continue

entryScreen()
