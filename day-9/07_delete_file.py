import os

if os.path.exists("demo.txt"):
    os.remove("demo.txt")
    print("File deleted successfully.")
else:
    print("File does not exist.")