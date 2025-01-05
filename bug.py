def function_with_uncommon_bug(a, b):
    if a == 0:
        return 0
    elif b == 0:
        return 1
    else:
        return a / b

result = function_with_uncommon_bug(10, 0)
print(result) # Raises ZeroDivisionError
result2 = function_with_uncommon_bug(0,5)
print(result2) #Prints 0
result3 = function_with_uncommon_bug(5,2)
print(result3) # Prints 2.5