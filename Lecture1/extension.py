import os 

file_name = input("File name: ")

# Get the extension from the file 
extention = os.path.splitext(file_name)[1]

print(extention)

# match suffix (extension) of file name 
match extention:
    case ".gif":
        print("image/gif")
    case ".jpg":
        print("image/jpeg")
    case ".jpeg":
        print("image/jpeg")
    case ".png":
        print("")
    case ".pdf":
        print("")
    case ".txt":
        print("")
    case ".zip":
        print("")
    case _:
        print("application/octet-stream")