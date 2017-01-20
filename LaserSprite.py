import pygame
# LaserSprite.py
from Proj import PlayerShip
pygame.mixer.init()

class Laser(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        """ Load the arrow image into the variable imageMaster """
        self.imageMaster = pygame.image.load("laser2B.png").convert_alpha()
        """ Load the arrow image into the variable image - This is a copy """
        self.image = pygame.image.load("laser2B.png").convert_alpha()
        
        """ Convert image to a rectangle """
        self.rect = self.imageMaster.get_rect()
        """ Set its center to be off the screen """
        self.rect.center = (-100, -100)
        """ This sets the angle in degrees """
        self.dir = 0
        """ Set the x and y positions to be 0 initially """
        self.x = 0
        self.y = 0
        """ Set the dx and dy positions to be off the screen initially """
        self.dx = -100
        self.dy = -100
        """ This adds a delay to the flight path of the arrow,
            This was covered in lecture 8
        """
        if not pygame.mixer:
            print "problem with sound"
        else:
            pygame.mixer.init()
            self.fire = pygame.mixer.Sound("science_fiction_laser_005.ogg")

        
    def update(self):
        """ update the x and y position of the sprite on its path:  see AnglePoints Function below """
        self.x+=self.dx
        self.y+=self.dy
        """ Set the new center of the angled sprite """
        self.rect.center =(self.x , self.y)
    
    def rotate(self):
        """ Store the old center of the image"""
        oldCenter = self.rect.center
        """ Store the transformed image into the variable image (copy) """
        self.image = pygame.transform.rotate(self.imageMaster, self.dir)
        """ Get the new size of the transformed image """
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
        """ The change in dx and dy is a scale of the vector it must travel """
        self.dx = vect.x*.1
        self.dy = vect.y*.1
        print "dx & dy: %.2f %.2f " %(self.dx, self.dy)
        """ Rotate the image based on what angle was passed in """
        self.rotate()
