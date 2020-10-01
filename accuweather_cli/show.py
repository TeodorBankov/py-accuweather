import urllib.request
import json
import time
import os
import random
import textwrap
from arts import *
from forecast import *

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    Red = '\033[91m'
    Green = '\033[92m'
    Blue = '\033[94m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Yellow = '\033[93m'
    Magenta = '\033[95m'
    Grey = '\033[90m'
    Black = '\033[90m'
    Default = '\033[99m'

# Get terminal size for formatting
term_width = os.get_terminal_size()[0]  
term_heigth = os.get_terminal_size()[1] 

def padToCenter(l:list,w:int)->str:
    """Manual centering"""
    padding =  ' '*(w//2) # a 1 char line would need at most w/2 spaces in front
    parts = [ padding[0: (w-len(p))//2+1]+p for p in l]
    return '\n'.join(parts)

def padToCenter2(l:list,w:int)->str:
    return '\n'.join('-'+x.center(w)+'-' for x in l)

def border_msg(msg):
    row = len(msg)
    h = ''.join(['+'] + ['-' *row] + ['+'])
    result= h + '\n'"|"+msg+"|"'\n' + h
    aligned = padToCenter(result.splitlines(), term_width)
    return aligned

welcome = random.choice(welcome_ascii)
welcome_aligned = padToCenter(welcome.splitlines(), term_width)


print(bcolors.OKBLUE + welcome_aligned)
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


#for key1 in day_forecast('51097', api_weather())['DailyForecasts']:
#    print(bcolors.Magenta + "Weather forecast for:"+key1['Date'].center(term_width))
#    print("Min temp: "+str(key1['Temperature']['Minimum']['Value']).center(term_width))
#    print("Max temp: "+str(key1['Temperature']['Maximum']['Value']).center(term_width))
#    print("Forecast: "+str(key1['Day']['ShortPhrase']).center(term_width))
#    print("*****************************************".center(term_width))
    #This has to be centered pretty and also made more beautiful and optimised

fail = gather_json('cache.json')

for key1 in fail['DailyForecasts']:
     print(bcolors.Magenta + "Date:".center(term_width)+"\n"+border_msg(key1['Date']))
