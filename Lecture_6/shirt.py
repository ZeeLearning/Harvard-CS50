import sys
from PIL import Image, ImageOps

def main():
    # Check for the correct number of command-line arguments
    if len(sys.argv) <= 2:
        sys.exit("Too few command-line argument")
    
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line argument")

    elif len(sys.argv) == 3:

        input_image_path = sys.argv[1]
        output_image_path = sys.argv[2]
        
        # Validate file extensions
        valid_extensions = (".jpg", ".jpeg", ".png")
        if not (input_image_path.lower().endswith(valid_extensions) and 
                output_image_path.lower().endswith(valid_extensions)):
            sys.exit("Invalide input")
        
        # Check if input and output extensions are the same
        if input_image_path.split('.')[-1].lower() != output_image_path.split('.')[-1].lower():
            sys.exit("Input and output have different extensions ")
        
        # Try to open the input image
        try:
            input_image = Image.open(input_image_path)
        except FileNotFoundError:
            sys.exit(f"Input file '{input_image_path}' does not exist")
        
        # Open the shirt image (assuming shirt.png is in the same directory)
        shirt_image = Image.open("shirt.png")
        
        # Resize and crop the input image
        input_image = ImageOps.fit(input_image, shirt_image.size)
        
        # Overlay the shirt on top of the input image
        input_image.paste(shirt_image, (0, 0), shirt_image)
        
        input_image.save(output_image_path)

if __name__ == "__main__":
    main()
