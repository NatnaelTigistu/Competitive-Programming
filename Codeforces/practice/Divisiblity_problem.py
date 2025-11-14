testcase = int(input())

for i in range(testcase):
    numbers = input().split()
    a = int(numbers[0])
    b = int(numbers[1])
    if a%b == 0:
        print("0")
    else :
        c = ((((a//b)+1)*b)-a)
        print (c)