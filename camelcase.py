#Camel Case is a naming style common in many programming languages. In Java, method and variable names typically start with a lowercase letter, with all subsequen words starting with a capital letter (example: startThread). Names of classes follow the same pattern, except that they start with a capital letter (example: BlueCar).Your task is to write a program that creates or splits Camel Case variable, method, and class names.
while True:
    try:
        q = input().rstrip()
    except EOFError:
        break
    op = q[0]
    ot = q[2]
    string = list(q[4:])
    
    if op == "S":
        temp = ""
        
        if ot == "M":
            for s in string[:-2]:
                if s.islower():
                    temp += s
                else:
                    temp += f' {s.lower()}'
            print(temp)
        elif ot == "V":
            for s in string:
                if s.islower():
                    temp +=s
                else:
                    temp += f' {s.lower()}'
            print(temp)
        elif ot == "C":
            temp += string[0].lower()
            for s in string[1:]:
                if s.islower():
                    temp +=s
                else:
                    temp += f' {s.lower()}'
            print(temp)
    if op == "C":
        temp = string.copy()
        
        for i in range(len(string)):
            if string[i] == " ":
                temp[i+1] = temp[i+1].upper()
        if ot == "M":
            temp = "".join(temp)
            temp = temp.replace(" ","")
            print(temp+"()")
        elif ot == "V":
            temp = "".join(temp)
            print(temp.replace(" ",""))
        elif ot == "C":
            temp[0]= temp[0].upper()
            temp = "".join(temp)
            print(temp.replace(" ",""))    
     