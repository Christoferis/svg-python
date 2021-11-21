#convert to hex or to rgb

from functools import reduce
from math import floor

_hex = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

#standard Colors (Hex)
RED = "#FF0000"
PINK = "#FF00FF"
GREEN = "#00FF00"
YELLOW = "#FFFF00"
BLUE = "#0000FF"
LIGHT_BLUE = "#00FFFF"
WHITE = "#FFFFFF"
BLACK = "#000000"
GRAY = "#7F7F7F"
DARK_GRAY = "#474747"
LIGHT_GRAY = "#CCCCCC"


#implement 255 limit
def hex_to_rgb(hex : str) -> tuple:
    hex = hex.removeprefix("#")

    if len(hex) > 6:
        raise ValueError

    rgb = list(hex)

    #convert string to number else 
    for i in range(len(rgb)):        
        try:
            rgb[i] = int(rgb[i])
        except ValueError:
            rgb[i] = _hex.index(rgb[i])
            pass

    return (rgb[0] * 16 + rgb[1], rgb[2] * 16 + rgb[3], rgb[4] * 16 + rgb[5])


def rgb_to_hex(rgb : list, hashtag=True):
    hex = ""
    if hashtag: hex += "#"

    for color in rgb:

        #just replace with F
        try:
            fdigit = _hex[floor(color / 16)]
        except IndexError:
            fdigit = "F"

        #just replace with F
        try:
            sdigit = _hex[color % 16]
        except IndexError:
            sdigit = "F"
            
        hex += fdigit + sdigit

    return hex

#test procedure
if __name__ == "__main__":
    hex1 = "1F89FF"
    hex2 = "474747"

    hex1 = hex_to_rgb(hex1)
    hex2 = hex_to_rgb(hex2)

    print(hex1)
    print(hex2)

    hex1 = rgb_to_hex(hex1)
    hex2 = rgb_to_hex(hex2)

    print(hex1)
    print(hex2)
    
