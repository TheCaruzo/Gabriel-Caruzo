import random 

def enemy1():
    global hp 
    hp = random.randint(10, 100)
    statusm = { "fo" : random.randint(5, 25),
                "de" : random.randint(5, 10)
                }
    print(hp)
    print(statusm["de"])
    print(statusm["fo"])


enemy1()