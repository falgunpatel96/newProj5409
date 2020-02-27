def fibo( no ):
    if no <= 0:
        raise Exception("Inout not valid...!!!");
    elif no == 1:
        return 0;
    elif no == 2:
        return 1;
    return fibo( no-1 ) + fibo( no-2 );

f = open("input.txt","r");
for no in f:
    print("Fibo of "+no+": "+str(fibo(int(no))));