def fibo( no ):
    a = 0
    b = 1
    if no <= 0:
        raise Exception("Input not valid...!!!")
    elif no == 1 or no == 2:
        print(no-1, end=' ')
    else:
        for i in range(3,no):
            c = a + b
            a = b
            b = c
        print(b, end=' ')

f = open("input.txt","r")
for no in f:
    print("\n\nFibo of "+str(no).strip()+": ", end=' ')
    for i in range(int(str(no).strip())):
        fibo(int(i+1))