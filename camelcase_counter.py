def camelcase_token_counter(s):
    count = 0
    
    for ch in s:
        if ch.isupper():
            count += 1
    
    return count + 1  

s = input("Enter CamelCase string: ")

print("Number of words:", camelcase_token_counter(s))