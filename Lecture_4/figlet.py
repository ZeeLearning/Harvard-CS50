import sys
from pyfiglet import Figlet
import random

normal_font = input("Input: ")

figlet = Figlet()

if len(sys.argv) == 1:
    fonts = figlet.getFonts()
    font = random.choice(fonts)
    figlet = Figlet(font = font)

    print(f"Output: \n{figlet.renderText(normal_font)}")

elif len(sys.argv) == 3:
        # Check if the first argument is -f or --font
        if sys.argv[1] in ['-f', '--font']:
            font = sys.argv[2]  # The second argument should be the name of the font
            try:
                figlet = Figlet(font=font)
                print(f"Output: \n{figlet.renderText(normal_font)}")
            except:
                sys.exit("Invalid usage")
        else:
             sys.exit("Invalid usage")
            
else:
     if len(sys.argv) > 3 or len(sys.argv) == 2:
        sys.exit("Invalid usage")


