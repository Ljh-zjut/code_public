def createCounter():
    n = 0
    def counter():
        nonlocal n
        n += 1
        return n
    return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA()) 
counterB = createCounter()
print([counterB(), counterB(), counterB(), counterB()])