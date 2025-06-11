def isint(s: str) -> bool:
    digito = "0123456789"
    valido = True
    if s[0] in "+-" or s[0] in digito: 
        for i in range(1, len(s)):
            if s[i] not in digito:
                valido = False
                break
    else:
        valido = False
    
    return valido


# 012345678
# +-1    

print(isint("Edson")) # False
print(isint("45.78")) # False
print(isint("78"))    # True
print(isint("-78"))  # True

