""" Useful information about the container e.g. device, game etc...


TO DO LIST:
- Make a folder path system for data
- Log data from console into files in path
- Save gameplay data to a file to be used later e.g. "Save-DD-HH-MM"
- Access Read/Write saved gameplay data via console commands

"""

from datetime import datetime
from io import StringIO
import os
import pygame

pygame.init()

# Enables color support
os.system("")

# ANSI colour Code
pref = "\033["
reset = f"{pref}0m"

class Color:
    """ Colors for ANSI """
    def __init__(self):
        self.black = "30m"
        self.red = "31m"
        self.green = "32m"
        self.yellow = "33m"
        self.blue = "34m"
        self.magenta = "35m"
        self.cyan = "36m"
        self.white = "37m"
        
color = Color()

class Console(object):
    """ Class object to manage console interaction """
    
    def __init__(self):
        now = datetime.now()
        self.time = now.strftime("%H:%M:%S")
        self.font = pygame.font.Font(None,32)
    
    def text(self,text,color,is_bold=False):
        """ Applies ANSI escape code premade colors to string data """
        text = f"{pref}{1 if is_bold else 0};{color}" + text + reset
        return text
    
    def warn_user(self,severity:int,message = None):
        """ Warns the user about an issue """
        data = {
            0:'[OK]',
            1:'[WARNING]',
            2:'[ERROR]'
        }
        
        for key in data.keys():
            if key == severity:
                if key == 0: print(self.time,
                                   self.text(data.get(key),
                                             color.green), message)
                elif key == 1: print(self.time,
                                     self.text(data.get(key),
                                               color.yellow), message)
                elif key == 2: print(self.time,
                                     self.text(data.get(key),
                                               color.red), message)
                
class Command(object):
    def __init__(
        self,
        parser = None,
        state = False,
        
        
    ):
        self.parser = parser
        self.state = state
        
# console = Console()
# test error message
# console.warn_user(
#     severity=2,
#     message=console.text(
#         "This is a test error message",
#         color.white,is_bold=True)
#     )