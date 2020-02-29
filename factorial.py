import time
import json

def fact( no ):
    if no < 0:
        raise Exception("Factorial of negative number is not possible...!!!");
    elif no == 1 or no == 0:
        return 1;
    return no * fact(no-1);


finalLog = [];
f = open("input.txt","r");
for index,no in enumerate(f):
    logNo = {};
    start = time.time()
    result = str(fact(int(no)));
    end = time.time()
    #print("Fact of "+str(no).strip()+": "+result);
    #print("time: "+str(end-start))

    # logNo.append(index+1);
    # logNo.append(str(end-start));
    # logNo.append(no.strip());
    # logNo.append(result);

    logNo['ID'] = index+1;
    logNo['time'] = str(end-start);
    logNo['no'] = no.strip();
    logNo['result'] = result;

    finalLog.append(logNo);
    #print("Log: "+str(logNo));
    #print("\n\n");

#print("finalLog: "+str(finalLog));

json_log = json.dumps(finalLog);
#print("\n\n\n");
print("JSON: "+json_log);
with open("LogFact.json",mode='w',newline="\n") as file:
    file.write(json_log);
file.close();
