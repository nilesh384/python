from pathlib import Path

# path = Path("zigya")
# print(path.exists())           #checks if a directory exists

# print(path.mkdir())            #creates a directory

# print(path.rmdir())              #removes a directory

path = Path()

for file in path.glob('*'):
    print(file)
