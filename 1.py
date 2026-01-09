def rev(str):
    revS = ""
    for ch in str:
        revS = ch + revS
    return revS

def e_o(num):
    if num%2 == 0:
        return "Even"
    else:
       return "Odd"

print(e_o(6))
print(rev("123"))