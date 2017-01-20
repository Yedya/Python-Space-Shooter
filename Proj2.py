
import pygame
import random
import math
from Vector_Calc import Vector
from ScoreBoardSprite import ScoreBoard
from random import randrange

pygame.init()
global distance




class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imageMaster = pygame.image.load("laser2B.png").convert_alpha()

        self.image = pygame.image.load("laser2B.png").convert_alpha()
        
        
        self.rect = self.imageMaster.get_rect()
        
        self.rect.center = (-100, -100)
        
        self.dir = 0
        
        self.x = 0
        self.y = 0
        
        self.dx = -100
        self.dy = -100
 

        pygame.mixer.init()
        self.fire = pygame.mixer.Sound("science_fiction_laser_005.ogg")

        
    def update(self):
        """ update the x and y position of the sprite on its path:  see AnglePoints Function below """
        self.x+=self.dx
        self.y+=self.dy
        """ Set the new center of the angled sprite """
        self.rect.center =(self.x , self.y)
        
    def rotate(self):
        # Store the old center of the image"""
        oldCenter = self.rect.center
        #Store the transformed image into the variable image (copy)
        self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        # Get the new size of the transformed image """
        self.rect = self.image.get_rect()
        """ Reset its center to that of the old stored image """
        self.rect.center = oldCenter

    def AnglePoints(self, points, angle, vect):
        """ Set the rotation angle direction of the master image """
        self.dir = angle
        """ Set the center points of the arrow, this is the first click - where the arrow starts """
        self.rect.center = points
        """ The x and y will be used to update the position of the arrow as it travels its path
            Starting with the origion"""
        self.x=points[0]
        self.y = points[1]
        #The change in dx and dy is a scale of the vector it must travel 
        self.dx = vect.x*.1
        self.dy = vect.y*.1
        
        # Rotate the image based on what angle was passed in
        self.rotate()


class ControlData:
    def __init__(self):
        self.moveX = 0
        self.moveY = 0


class StaticCoin(pygame.sprite.Sprite):
    def __init__(self,screen, (x, y), playerShip):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.png").convert()
        self.image = pygame.image.load("coin.png").convert_alpha()
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.StaticCoinX = float(x)
        self.StaticCoinY = float(y)
        self.ship = playerShip
        self.count = 0
        self.screen = screen
        
    


    def update(self):


        
        if self.StaticCoinX > self.screen.get_width():
            self.StaticCoinX = 0
        if self.StaticCoinY < 0:
            self.StaticCoinY = self.screen.get_height()
        ##PatternMovement----------------
        if self.count < 600:

            self.rect.center = (self.StaticCoinX, self.StaticCoinY)
        elif self.count < 600:

            self.rect.center = (self.StaticCoinX, self.StaticCoinY)
        else:
            self.count = 0       





class Coin(pygame.sprite.Sprite):
    def __init__(self,screen, (x, y), playerShip,Speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("coin.png").convert()
        self.image = pygame.image.load("coin.png").convert_alpha()
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.CoinX = float(x)
        self.CoinY = float(y)
        self.ship = playerShip
        self.count = 0
        self.screen = screen
        
    
        ptu = ControlData()
        ptu.moveX = Speed
        ptu.moveY = -1

        ptd = ControlData()
        ptd.moveX = Speed
        ptd.moveY = -1
        
        self.pattern = [ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu,
                        ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd,]
                       
        self.patternIndex = 0

    def update(self):
        ##PatternMovement----------------
       
        posX=self.CoinX
        posY=self.CoinY
        cd=self.pattern[self.patternIndex]
        self.CoinX+=cd.moveX
        self.CoinY+=cd.moveY
        self.patternIndex += 1
        if self.patternIndex >= len(self.pattern):
            self.patternIndex = 0


        self.count += 1


        #So the Coin won't go outside the screen and not come back

        
        if self.CoinX > self.screen.get_width():
            self.CoinX = 0
        if self.CoinY < 0:
            self.CoinY = self.screen.get_height()
        ##PatternMovement----------------
        if self.count < 600:

            self.rect.center = (self.CoinX, self.CoinY)
        elif self.count < 600:

            self.rect.center = (self.CoinX, self.CoinY)
        else:
            self.count = 0    



class Box(pygame.sprite.Sprite): # gives player extra health
    def __init__(self,screen, (x, y), playerShip):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("heart.png").convert()
        self.image = pygame.image.load("heart.png").convert_alpha()
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.boxX = float(x)
        self.boxY = float(y)
        self.ship = playerShip
        self.count = 0
        self.screen = screen
       
    


        ptu = ControlData()
        ptu.moveX = 1
        ptu.moveY = 1

        ptd = ControlData()
        ptd.moveX = 1
        ptd.moveY = -1
        
        self.pattern = [ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu,
                        ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd,]
                       
        self.patternIndex = 0

    def update(self):
        ##PatternMovement----------------
       
        posX=self.boxX
        posY=self.boxY
        cd=self.pattern[self.patternIndex]
        self.boxX+=cd.moveX
        self.boxY+=cd.moveY
        self.patternIndex += 1
        if self.patternIndex >= len(self.pattern):
            self.patternIndex = 0


        self.count += 1
       

        #So the spaceship won't go outside the screen
        if self.boxX > self.screen.get_width():
            self.boxX = 0
        if self.boxY < 0:
            self.boxY = self.screen.get_height()
        ##PatternMovement----------------

        if self.count < 600:
            
            self.rect.center = (self.boxX, self.boxY)
        elif self.count < 600:
            
            self.rect.center = (self.boxX, self.boxY)
        else:
            self.count = 0    
            



class EnemyShip(pygame.sprite.Sprite):
    def __init__(self,screen, (x, y), playerShip):
        pygame.sprite.Sprite.__init__(self)
        image_array = ["space2.png"]
        self.image = pygame.image.load(image_array[0]).convert()
        self.image = pygame.image.load(image_array[0]).convert_alpha()
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.enemyX = float(x)
        self.enemyY = float(y)
        self.ship = playerShip
        self.count = 0
        self.currentState2 = 0
        self.screen = screen
        self.health1 = 100
    
        ptu = ControlData()
        ptu.moveX = 3


        ptd = ControlData()
        ptd.moveX = 3
 
        
        self.pattern = [ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu, ptu,
                        ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd, ptd,]
                       
        self.patternIndex = 0

    def update(self):
        ##PatternMovement----------------
        if self.currentState2 !=1:
            posX=self.enemyX
            posY=self.enemyY
            cd=self.pattern[self.patternIndex]
            self.enemyX+=cd.moveX
            self.enemyY+=cd.moveY
            self.patternIndex += 1
            if self.patternIndex >= len(self.pattern):
                self.patternIndex = 0


        self.count += 1
        x_component = self.ship.rect.centerx-self.enemyX
        y_component = self.ship.rect.centery-self.enemyY
        distance = math.hypot(x_component, y_component)##If player comes within radius of 100,intiate chase state

        #So the spaceship won't go outside the screen

        
        if self.enemyX > self.screen.get_width():
            self.enemyX = 0
        if self.enemyY < 0:
            self.enemyY = self.screen.get_height()
        ##PatternMovement----------------
        if distance > 200 and self.enemyY !=68:
            self.enemyY+=1
            if self.enemyY>self.screen.get_height():                    
                self.enemyY=68
        
        if distance < 200: 
            self.currentState2 = 1

        elif distance > 200:
            self.currentState2 = 0

        if self.count < 600:
            self.caculateNextPosition()
            self.rect.center = (self.enemyX, self.enemyY)
        elif self.count < 600:
            self.caculateNextPositionEvade()
            self.rect.center = (self.enemyX, self.enemyY)
        else:
            self.count = 0    
            
    def caculateNextPosition(self): 
        shipX = self.ship.rect.centerx
        shipY = self.ship.rect.centery
        if self.currentState2==1:
            if self.enemyY < shipY:
                self.enemyY += 3
            elif self.enemyY > shipY:
                self.enemyY -= 3

            if self.enemyX < shipX:
                self.enemyX += 3
            elif self.enemyX > shipX:
                self.enemyX -= 3
        elif self.currentState2==0: 
            if self.enemyY < shipY:
                self.enemyY += 0
            elif self.enemyY > shipY:
                self.enemyY -= 0
               
            if self.enemyX < shipX:
                self.enemyX += 0
            elif self.enemyX > shipX:
                self.enemyX -= 0
            
class EnemyShip2(pygame.sprite.Sprite):
    def __init__(self,screen, (x, y), playerShip):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("enemy.png").convert()
        self.image = pygame.image.load("enemy.png").convert_alpha() 
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.enemy2X = float(x)
        self.enemy2Y = float(y)
        self.ship = playerShip
        self.count = 0
        self.currentState = 0
        self.health2 = 100
        self.screen = screen

    
        
      
        
    def update(self):
        self.count += 1
        x_component = self.ship.rect.centerx-self.enemy2X
        y_component = self.ship.rect.centery-self.enemy2Y
        distance = math.hypot(x_component, y_component)
        if self.health2<25:
            self.currentState = 4
            if self.currentState==4:
                distance=10
                
        if self.health2<50:
            self.currentState = 3
            if self.currentState==3 and self.enemy2Y!=68:
                self.enemy2Y+=1
                if self.enemy2Y>self.screen.get_height() :
                    self.enemy2Y=68
        
        
        if distance < 200:
            self.currentState = 1      
            
        elif distance > 200:
            self.currentState = 2

        if self.count < 600:
            self.caculateNextPosition()
            self.rect.center = (self.enemy2X, self.enemy2Y)
        elif self.count < 600:
            self.caculateNextPositionEvade()
            self.rect.center = (self.enemy2X, self.enemy2Y)
        else:
            self.count = 0    
            
    def caculateNextPosition(self):
        shipX = self.ship.rect.centerx
        shipY = self.ship.rect.centery

        if self.currentState==1: #State 2 chasing state
            if self.enemy2Y < shipY:
                self.enemy2Y += 2
            elif self.enemy2Y > shipY:
                self.enemy2Y -= 2
                
            if self.enemy2X < shipX:
                self.enemy2X += 2
            elif self.enemy2X > shipX:
                self.enemy2X -= 2      
        elif self.currentState==2: #State 1 Idle/guarding state
            if self.enemy2Y < shipY:
                self.enemy2Y += 0
            elif self.enemy2Y > shipY:
                self.enemy2Y -= 0
                
            if self.enemy2X < shipX:
                self.enemy2X += 0
            elif self.enemy2X > shipX:
                self.enemy2X -= 0
        elif self.currentState==3:# State 3 injured,will chase but at a slower rate
            if self.enemy2Y < shipY:
                self.enemy2Y += 1
            elif self.enemy2Y > shipY:
                self.enemy2Y -= 1
                
            if self.enemy2X < shipX:
                self.enemy2X += 1
            elif self.enemy2X > shipX:
                self.enemy2X -= 1   
        elif self.currentState==4:# State 4 fleeing             
            if self.enemy2Y < shipY:
                self.enemy2Y += 1
            elif self.enemy2Y > shipY:
                self.enemy2Y -= 1
                
            if self.enemy2X < shipX:
                self.enemy2X += 1
            elif self.enemy2X > shipX:
                self.enemy2X -= 1                
class PlayerShip(pygame.sprite.Sprite):
    def __init__(self, screen, (x, y)):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.image.load("player.png").convert()
        self.image = pygame.image.load("player.png").convert_alpha()
        transColor = self.image.get_at((1, 1))
        self.image.set_colorkey(transColor)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.Playerhealth = 100
        self.dx =screen.get_width()/2
        self.dy = 400

        self.score = 0
        self.ammo = 0
        self.alive = True
        self.Playerhealth = 100

    def update(self):
        self.rect.center = (self.dx,self.dy)
    
    def returnPosition(self):
        return self.rect.center

    def Get_Score(self):
        return self.score   
    def Get_Ammo(self):
        return self.ammo
    def Get_Playerhealth(self):
        return self.Playerhealth
    def Set_Ammo(self):
        self.ammo+=1
    def Set_Playerhealth(self):
        self.Playerhealth-=20
        
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.centerx -= 4
        if keys[pygame.K_RIGHT]:
            self.rect.centerx += 4
        if keys[pygame.K_UP]:
            self.rect.centery -= 4
        if keys[pygame.K_DOWN]:
            self.rect.centery += 4

        if self.rect.centerx > self.screen.get_width():
            self.rect.centerx = 0
        if self.rect.centerx < 0:
            self.rect.centerx = self.screen.get_width()
        if self.rect.centery > self.screen.get_height():
            self.rect.centery = 0
        if self.rect.centery < 0:
            self.rect.centery = self.screen.get_height()
def updateScoreBoard(RefreshScore):  
    (ship, scoreBoard) = RefreshScore
    scoreBoard.text = ("Score: %d    Fired: %d    Playerhealth: %d" %(ship.Get_Score(),ship.Get_Ammo(),ship.Get_Playerhealth()))


        
def main():



    
    screen = pygame.display.set_mode((1000, 620))
    pygame.display.set_caption("Y2 Python Project")

    background = pygame.Surface(screen.get_size())
    background.fill((0, 0, 0))
    screen.blit(background, (0, 0))


    
    
    playerShip = PlayerShip(screen, (800,600))
    enemyShip1 = EnemyShip(screen,(100, 68), playerShip)
    enemyShip2 = EnemyShip2(screen,(300, 30),playerShip)
    enemyShip3 = EnemyShip2(screen,(70, 80),playerShip)
    enemyShip4 = EnemyShip2(screen,(640, 40),playerShip)
    enemyShip5 = EnemyShip2(screen,(890, 65),playerShip)
    
    Coin1      = Coin(screen,(450, 50),playerShip,2)
    Coin2      = Coin(screen,(40, 210),playerShip,3)
    Coin3      = Coin(screen,(441, 31),playerShip,1)
    Coin4      = Coin(screen,(410, 101),playerShip,2)
    Heart       = Box(screen,(100,40),playerShip)
    StaticCoin1 = StaticCoin(screen,(100,40),playerShip)
    StaticCoin2 = StaticCoin(screen,(165,40),playerShip)
    StaticCoin3 = StaticCoin(screen,(400,20),playerShip)
    StaticCoin4 = StaticCoin(screen,(500,20),playerShip)
    StaticCoin5 = StaticCoin(screen,(830,25),playerShip)
    StaticCoin6 = StaticCoin(screen,(950,35),playerShip)
    StaticCoin7 = StaticCoin(screen,(610,15),playerShip)
    StaticCoin8 = StaticCoin(screen,(780,15),playerShip)
    
    Coins      = pygame.sprite.Group(Coin1,Coin2,Coin3,Coin4,StaticCoin1,StaticCoin2,StaticCoin3,StaticCoin4,StaticCoin5,StaticCoin6,StaticCoin7,StaticCoin8)
    enemySprites = pygame.sprite.Group(enemyShip1)#had to group individually because collision wasn't working
    enemySprites2 = pygame.sprite.Group(enemyShip2)
    enemySprites3 = pygame.sprite.Group(enemyShip3)
    enemySprites4 = pygame.sprite.Group(enemyShip4)
    enemySprites5 = pygame.sprite.Group(enemyShip5)
    HeartGroup         = pygame.sprite.Group(Heart)
   
    allSprites = pygame.sprite.Group(playerShip,enemySprites,enemySprites2,enemySprites3,enemySprites4,enemySprites5,Heart,Coins,)#Coin
    playerGroup = pygame.sprite.Group(playerShip)

    clock = pygame.time.Clock()
    b1 = "space_background.gif" # Scrolling background
    back = pygame.image.load(b1).convert()

    scoreBoard = ScoreBoard()
    scoreBoard.text = ("Score: %d   Fired: %d   Health: %d" %(playerShip.Get_Score(),playerShip.Get_Ammo(),playerShip.Get_Playerhealth()))
    scoreBoard.center = (320,600)
    allSprites.add(scoreBoard)
    
    screenHeight = back.get_rect().height 
    h = 0
   
    laser_list = pygame.sprite.Group()
    keepGoing = True

    pygame.mouse.set_visible(False)
    while keepGoing:
        clock.tick(60)
        if h >= screenHeight:
            h = 0
        screen.blit(back, (0,h))
        screen.blit(back, (0,h-screenHeight))
        h = h + 5 # faster move



        pygame.mouse.set_visible(True)
        # Handle Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False


            if event.type == pygame.MOUSEBUTTONDOWN:
                """ If a mouse event occurs check to see if it is the left click """
                if event.button == 1: 

                    playerShip.Set_Ammo();     
                    shipCenter = playerShip.returnPosition() 
                    
                    mousePos = event.pos # change: you have position in mouse event
                    
                    data= (shipCenter, mousePos)          
                    angle, vect = PlotVector(data)
                    laser = Laser()
                    laser.fire.play()
                    laser.AnglePoints(shipCenter, angle, vect)
                    laser_list.add(laser)
                    allSprites.add(laser)    
        #Update sprites
        allSprites.update()
        if pygame.sprite.spritecollide(playerShip, Coins, False):
            playerShip.score+= 30
            pygame.sprite.spritecollide(playerShip, Coins, True)
        #If player collects health/heart object
        if pygame.sprite.spritecollide(playerShip,HeartGroup,False):
            playerShip.Playerhealth+=50
            pygame.sprite.spritecollide(playerShip,HeartGroup,True)
        
        #If enemy boards playership
        if pygame.sprite.spritecollide(playerShip, enemySprites, False):
                
                playerShip.Playerhealth-= 1
                print playerShip.Playerhealth
                if playerShip.Playerhealth<0:
                    print 'you are DEAD,try again'
                    keepGoung=False
                    break
                    

        #For every laser that was fired
        for laser in laser_list:
            """ Enemies health decrements by 20 each time they're hit by a laser """
            #Collisions with players laser
            
            if pygame.sprite.spritecollide(laser, enemySprites2, False):
                enemyShip2.health2-=20      
                playerShip.score+= 2
                if enemyShip2.health2<0:                    
                    playerShip.score+= 10
                    pygame.sprite.spritecollide(laser, enemySprites2, True)

            if pygame.sprite.spritecollide(laser, enemySprites, False):
                enemyShip1.health1-=20
                print enemyShip1.health1
                playerShip.score+= 2
                if enemyShip1.health1<0:
                    playerShip.score+= 10
                    pygame.sprite.spritecollide(laser, enemySprites, True)
            
            if pygame.sprite.spritecollide(laser, enemySprites3, False):
                enemyShip3.health2-=20
                print enemyShip3.health2
                playerShip.score+= 2
                if enemyShip3.health2<0:
                    playerShip.score+= 10
                    pygame.sprite.spritecollide(laser, enemySprites3, True)
            
            if pygame.sprite.spritecollide(laser, enemySprites4, False):
                enemyShip4.health2-=20
                print enemyShip4.health2
                playerShip.score+= 2
                if enemyShip4.health2<0:
                    playerShip.score+= 10
                    pygame.sprite.spritecollide(laser, enemySprites4, True)

            if pygame.sprite.spritecollide(laser, enemySprites5, False):
                enemyShip5.health2-=20
                print enemyShip5.health2
                playerShip.score+= 2
                if enemyShip5.health2<0:
                    playerShip.score+= 10
                    pygame.sprite.spritecollide(laser, enemySprites5, True)
           

        RefreshScore  = (playerShip, scoreBoard)       
        updateScoreBoard(RefreshScore)       
           
          
               
        # Update the sprite
        # Clear the 'screen' of all of the sprites using the background surface
        allSprites.clear(screen, background)
        # Call all the sprites update methods
        allSprites.update()
        # Draw the sprites to the screen
        allSprites.draw(screen)
        # Update the full display Surface to the screen
        pygame.display.flip()

def PlotVector(PlotVect):
    """
        This PlotVector function handles the calculation of the new
        vector and also the calculation of the angle the arrow/bullet/projectile 
        will be transformed and travel to.  
        REFER TO YOUR NOTES FROM LECTURE 5
    """
    """ Un-bundle the data that is passed into this function """
    (start, dest) = PlotVect
    """ Create a new Vector object and call it vect """
    vect = Vector()
    """ Pass the start and dest coordinates and get back a new vector which the arrow must travel """
    vect = Vector.from_points(start, dest)
    """ Calculate the magnitude (Distance) between the two points """
    mag = vect.get_magnitude()
    """ Get the values for the vector, i.e. the change in x and change in y """
    x = vect.x
    y = vect.y
    """ This variable will be used to calculate and store the angle between points """
    angDEG = (math.atan2(y, x)*(180/math.pi))*-1

    """ Bundle and return the angle and vector which will be used in the TheArrow Sprite """
    return (angDEG, vect)


     

if __name__ == "__main__":
    main()
