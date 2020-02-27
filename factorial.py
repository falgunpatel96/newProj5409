def fact( no ):
    if no < 0:
        raise Exception("Factorial of negative number is not possible...!!!");
    elif no == 1 or no == 0:
        return 1;
    return no * fact(no-1);

print(fact(5));