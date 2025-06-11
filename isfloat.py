def isfloat(v: str) -> bool:
    if v[0] == '-' or v[0] == '+':
        v = v.replace("-",'',1)
    v = v.replace(".","",1)
    return v.isdigit()

def isint(s: str) -> bool:
    ...

x = "45"
print(x.isdigit())

# 012345678
# 125    

print(isfloat("Edson")) # False
print(isfloat("45.78")) # True
print(isfloat("78"))    # True
print(isfloat("234."))  # True
print(isfloat("234,67"))# False
print(isfloat("12.345.67"))  # False
print(isfloat("-12.5"))  # True

x = "-45"
print(x.isnumeric())
