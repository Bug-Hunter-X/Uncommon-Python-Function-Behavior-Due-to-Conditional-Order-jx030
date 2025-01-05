def function_with_uncommon_bug_fixed(a, b):
    if b == 0:
        if a == 0:
            return 0  # Handle the case where both a and b are 0.
        else:
            raise ZeroDivisionError("Division by zero")
    else:
        return a / b

result = function_with_uncommon_bug_fixed(10, 0)
#print(result)  # Raises ZeroDivisionError as expected
result2 = function_with_uncommon_bug_fixed(0,5)
print(result2) #Prints 0
result3 = function_with_uncommon_bug_fixed(5,2)
print(result3) # Prints 2.5