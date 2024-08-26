import random

def roll():
    minum_val=1
    max_val=6
    roll=random.randint(minum_val,max_val,)
    return roll
value=roll()
print(value)
