layer = int(input())

for i in range(layer):
    if i%2 == 0:
        print("I hate", end=" ")
    else:
        print("I love", end=" ")
    if i < layer-1 : print("that", end=" ")
print("it")