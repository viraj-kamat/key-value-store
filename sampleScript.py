from keyValue import *
import random
test = KeyValueStore()

"""
keys = [ "test"+str(random.randint(20,30)) for _ in range(0,10) ]
for i in range(0,100) :
    value = random.randint(1,100)
    key = random.choice(keys)
    test.put(key,value)
"""
values = [ x for x in range(20,101)]
key = "test"
for v in values :
    test.put(key,v)
    
print(test.get("test"))
print(test.get("test",81))



