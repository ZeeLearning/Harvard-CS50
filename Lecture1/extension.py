import os 

file_name = input("File name: ")

# Apply case and space insensitivity
file_name = file_name.strip().lower()

# Get the extension from the file 
extention = os.path.splitext(file_name)[1]

#print(extention)

# match suffix (extension) of file name 
match extention:
    case ".gif":
        print("image/gif")
    case ".jpg":
        print("image/jpeg")
    case ".jpeg":
        print("image/jpeg")
    case ".png":
        print("image/png")
    case ".pdf":
        print("application/pdf")
    case ".txt":
        print("text/plain")
    case ".zip":
        print("application/zip")
    case _:
        print("application/octet-stream")