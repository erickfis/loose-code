import os


data = []
for root, dirs, files in os.walk("your dir"):
    for filename in files:
        data.append((filename, root)) # or print()
