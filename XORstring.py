#In this challenge, the task is to debug the existing code to successfully execute all provided test files.Given two strings consisting of digits 0 and 1 only, find the XOR of the two strings.
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res+='0';
        else:
            res+='1';

    return res

s = input()
t = input()
print(strings_xor(s, t))
