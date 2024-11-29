import re
import sys

def main():
    # Takes HTML input and prints the parsed shortened YouTube URL
    print(parse(input("HTML: ")))

def parse(s):
    # Regular expression to match YouTube embed URLs in the src attribute of iframe
    pattern = r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_-]+)"'
    
    # Search for the pattern in the input string
    match = re.search(pattern, s)
    
    if match:
        # If found, get the video ID from the first capture group and return the shortened URL
        video_id = match.group(1)
        return f"https://youtu.be/{video_id}"
    
    # If no match is found, return None
    return None

if __name__ == "__main__":
    main()
