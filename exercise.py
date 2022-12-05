import pathlib
from pathlib import Path

file = pathlib.Path.home() / "My_folder"
file.mkdir(exist_ok=True)
new_file = file / "My_file.txt"
new_file.touch(exist_ok=True)

print(file.name)
print(new_file.name)
print(new_file.parent)




print(file.exists())





