import pygame

class Character(object):
    """ Top level for character """
    def __init__(self,surface):
        self.surface = surface
        self.walk_left = []
        self.walk_right = []
        self.standing = []
        
        self.character = pygame.draw.rect(surface,(176, 113, 59), pygame.Rect(0,0,25,25))
    
            
            
            