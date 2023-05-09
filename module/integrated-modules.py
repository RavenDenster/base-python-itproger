import time, sys, os, platform
import datetime as d
from math import sqrt as s, ceil
import myModel as my
from myModel import addThreeNumbers as add
import cowsay

print(cowsay.get_output_string('trex', 'Hello'))
print(my.name)
print(add(5,4,7))

time.sleep(3)
print(d.datetime.now().time())
print(sys.path)
print(os.name, platform.system())
print(ceil(s(25)))