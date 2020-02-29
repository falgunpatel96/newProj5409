import time
import json

def fibo( no ):
    result = "";
    a = 0
    b = 1
    if no <= 0:
        raise Exception("Input not valid...!!!")
    elif no == 1 or no == 2:
        #print(no-1, end=' ')
        result += str(no-1)+" ";

    else:
        for i in range(3,no):
            c = a + b
            a = b
            b = c
        #print(b, end=' ')
        result += str(b)+" ";
    return result;

finalLog = [];

f = open("input.txt","r")
for index,no in enumerate(f):
    logNo = {};
    resultFinal = "";
    #print("\n\nFibo of "+str(no).strip()+": ", end=' ')
    start = time.time()
    for i in range(int(str(no).strip())):
        resultFinal += fibo(int(i+1));
    end = time.time()
    #print("time: "+str(end-start))


    logNo['ID'] = index+1;
    logNo['time'] = str(end-start);
    logNo['no'] = no.strip();
    logNo['result'] = resultFinal;

    finalLog.append(logNo);
    #print("Log: "+str(logNo));
    #print("\n\n");

#print("finalLog: "+str(finalLog));

json_log = json.dumps(finalLog);
#print("\n\n\n");
print("JSON: "+json_log);

with open("LogFibo.json",mode='w',newline="\n") as file:
    file.write(json_log);
file.close();
