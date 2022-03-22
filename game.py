""" Main file for running the game
- reload command for live updates

"""

from screeninfo import get_monitors
from container import Console, Command, Color
from event import Event
from assets.characters.character import Character

import pygame
import os
import sys

# Console variables
console = Console()
command = Command()
color = Color()

# Engine variables
engine_icon = r'C:\\Programming\\GitHub\\platform_game\\assets\\images\\cat.jpeg'

class Engine:
    """ Platform Game """
    
    def __init__(self):
        """ Game initalisation process """
        console.warn_user(1, message=console.text("Your Systems Monitors: ", color.white, is_bold=True))
        
        for i in get_monitors():
            # print(console.text(f"{i}",color.white,is_bold=True))
            str_display = str(i).replace(")","").replace("name=","").replace("\\","").replace(".","")
            display_list = str_display.split()
            display_width = display_list[2]
            display_height = display_list[3]
            display_name = display_list[6]
            is_primary = display_list[7]
            print(console.text(text=f"{display_name} {display_width} {display_height} {is_primary}",color=color.white,is_bold=True))
            
        print("\n")
        input_monitor = int(input(console.text("Select a Display to run the game: ", color.white, is_bold=True)))        
        int_display = [input_monitor if type(input_monitor) == int else 0]
        pygame.init()
        pygame.display.set_caption("Platform Game")
        
        self.clock = pygame.time.Clock()
        self.terminated = False
        self.engine = pygame.display.set_mode((1270,720), display=int_display[0], flags=pygame.RESIZABLE)
        self.icon = pygame.image.load(f'{engine_icon}')
        pygame.display.set_icon(self.icon)
        self.engine_wh = (self.engine.get_width(),self.engine.get_height())        

    def render(self, surface, x:int = None, y:int = None, image_position = None):
        """ Renders the graphic to display
        
        surface:
        - surface: image to render to screen
        x,y:
        - (x,y): places image to the display location
        
        image_position:
        - 'center' takes screen size and image size and locates the center
        
        """
        
        if image_position is None:
            self.engine.blit(source=surface,dest=(x,y))
        elif image_position == "center":
            self.engine.blit(surface,(
                ((self.engine.get_width()/2)-(surface.get_width()/2)),
                                      ((self.engine.get_height()/2)-(surface.get_height()/2)))
                             )
            
        pygame.display.update()
        
    def engine_resize(self,engine = None, x:int = None, y:int = None):
        """ Resizes the engine to initalisation conditions """
        dimensions = (self.engine.get_width(),self.engine.get_height())
        
        if dimensions[0]<self.engine_wh[0]/2:
            console.warn_user(1,
                              message=console.text(
                                  "It seems you have made the window height smaller than expected, changing now...",
                                  color.yellow,
                                  is_bold=True))
            
            pygame.display.set_mode((1270, 720), pygame.RESIZABLE)
            
        elif dimensions[1]<self.engine_wh[1]/2:
            console.warn_user(1,
                              message=console.text(
                                  "It seems you have made the window width than expected, changing now...",
                                  color.yellow,
                                  is_bold=True))
            pygame.display.set_mode((1270, 720), pygame.RESIZABLE)
          
    def run(self):
        """ Runs the game UI """
        e = Event(event_handler=pygame.event.get())
        while not self.terminated:
            self.clock.tick(60)
            self.engine_resize()
            self.event = Event(event_handler=pygame.event.get())
            self.event.loop()
            
            pygame.display.update()


if __name__ == '__main__':
    game = Engine().run()