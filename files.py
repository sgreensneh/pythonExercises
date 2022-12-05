from pathlib import Path

# fake_path = Path("c:/cohort/private.img")
cwd_path = Path.cwd() / "Green"


# path = pathlib.Path("c:/cohort/private.img")
# cwd_path = pathlib.Path.cwd()
# print(cwd_path)
# print("parent -", path.parent)
# print(list(path.parents))
# print("Anchor -", path.anchor)
# print("Name -", path.name)
# print("suffix -", path.suffix)

cwd_path.mkdir(exist_ok=True)
print(cwd_path.exists())