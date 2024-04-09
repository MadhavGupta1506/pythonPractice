s="W3resource Python, Exercises."
import re
l=re.split(r"([, ]+)",s)
print(l[::2],l[1::2])