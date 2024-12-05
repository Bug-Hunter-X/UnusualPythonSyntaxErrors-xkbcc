def function(x):
    return x + 1

result = function(5) 
print(result) # Output: 6

#Uncommon error: The function is defined without parenthesis in the call
result2 = function 5
print(result2) # This will raise a SyntaxError