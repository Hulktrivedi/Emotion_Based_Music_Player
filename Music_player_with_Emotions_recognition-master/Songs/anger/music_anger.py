import os
import random

path = "C:\\PycharmProjects\\University_Projects\\Music\\anger"
files = os.listdir(path)
d = random.choice(files)
os.startfile(d)
