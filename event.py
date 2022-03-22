from pathlib import Path

import pygame
import sys
import os

from assets.characters.character import Character

class Event(object):
    """ Handles application events """
    
    def __init__(
        self,
        event_handler = None
    ):
        self.event_handler = event_handler
        
    def loop(self):
        for e in self.event_handler:
            EngineEvent(self.event_handler)
            MouseEvent(self.event_handler)
            KeyboardEvent(self.event_handler)
            ControllerEvent(self.event_handler)

class EngineEvent(object):
    """ Game engine event class """
    def __init__(
        self,
        event_handler = Event().event_handler
    ):
        self.event_handler = event_handler
        
        for e in event_handler:
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                    
class MouseEvent(object):
    """ Mouse event class """
    def __init__(
        self,
        event_handler = Event().event_handler
    ):
        pass
        
class KeyboardEvent(object):
    """ Keyboard event class """
    def __init__(
        self,
       event_handler = Event().event_handler
    ):
        for e in event_handler:
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_LEFT or e.key == ord('a'):
                    print('left')
                if e.key == pygame.K_RIGHT or e.key == ord('d'):
                    print('right')
                if e.key == pygame.K_UP or e.key == ord('w'):
                    print('jump')

class ControllerEvent(object):
    """ Controller event class """
    def __init__(
        self,
        event_handler = Event().event_handler
    ):
        pass
    
class MovementEvent(object):
    """ Movement logic """
    def __init__(
        self,
        surface,
        sprite
    ):
        self.surface = surface
        self.sprite = sprite
    
    def x(self,x:int,sprite = None):
        """ Moves the player on the X """
        if not sprite:
            Character(self.surface).character.x = Character(self.surface).character.x + x
    
    def y(self,x:int,sprite = None):
        """ Moves the player on the X """
        pass
