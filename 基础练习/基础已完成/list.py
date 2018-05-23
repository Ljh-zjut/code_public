L= ['hellO', 'WoRLd', 'AppLe']
def normalize(name):
    return name.capitalize()
L2 = list(map(normalize,L))
print(L2)