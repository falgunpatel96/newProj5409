def fibo( no ):
    if no <= 0:
        raise Exception("Inout not valid...!!!");
    elif no == 1:
        return 1;
    elif no == 2:
        return 1;
    return fibo( no-1 ) + fibo( no-2 );

print(fibo(6));