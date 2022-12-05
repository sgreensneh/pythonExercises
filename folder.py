import pathlib

green = pathlib.Path.home() / "sunny_folder"
green.mkdir(exist_ok=True)
sony = green / "Practice"
sony.touch()

print("Name -", green.name)
print("Parent -", green.parent)
print("Name -", sony.name)
print("Parent -", sony.parent)
print(sony.exists())
print(green.exists())
