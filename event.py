from pathlib import Path

import pygame
import sys
import os

# path = os.getcwd()
# constants = "pygame_constants.txt"

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
            pass

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
        pass

class ControllerEvent(object):
    """ Controller event class """
    def __init__(
        self,
        event_handler = Event().event_handler
    ):
        pass