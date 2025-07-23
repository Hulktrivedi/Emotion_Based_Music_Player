import os
import random
path="C:\\PycharmProjects\\University_Projects\\Music\\happy"
files=os.listdir(path)
d=random.choice(files)
os.startfile(d)