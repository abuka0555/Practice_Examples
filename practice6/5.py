#os
import os

print(os.getcwd())
print(os.listdir())

#shutil
import shutil

shutil.copy("file.txt", "copy.txt")

print("Файл скопирован")

#pathlib
from pathlib import Path

p = Path("file.txt")

print(p.exists())
print(p.name)