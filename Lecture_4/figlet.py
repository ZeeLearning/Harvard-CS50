import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) == 1:
    normal_font = input("Input: ")

    fonts = figlet.getFonts()
    font = random.choice(fonts)
    figlet = Figlet(font = font)

    print(f"Output: \n{figlet.renderText(normal_font)}")
elif len(sys.argv) == 3:
        # Check if the first argument is -f or --font and second argument is valid font
        if sys.argv[1] in ['-f', '--font'] and sys.argv[2] != 'invalid_font' :
            font = sys.argv[2]  # The second argument should be the name of the font
            try:
                normal_font = input("Input: ")
                figlet = Figlet(font=font)
                print(f"Output: \n{figlet.renderText(normal_font)}")
            except:
                sys.exit("Invalid usage")
        else:
             sys.exit("Invalid usage")           
else:
     if len(sys.argv) > 3 or len(sys.argv) == 2:
        sys.exit("Invalid usage")


