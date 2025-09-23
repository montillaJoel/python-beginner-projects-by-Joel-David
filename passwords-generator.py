import random
import string
import secrets

while True:
    try:
        user = int(input('How many characters do you want? '))
        break
    except ValueError: 
        print('Must choose a number')
        
def password(length):
    
    pool = string.ascii_letters + string.digits + string.punctuation
    storage = random.choices(pool, k=length)
    new_password = "".join(storage)
    
    is_letter = False
    is_digit = False
    is_symbol = False


def password(length):
    
    pool = string.ascii_letters + string.digits + string.punctuation
    storage = random.choices(pool, k=length)
    new_password = "".join(storage)
    
    is_letter = False
    is_digit = False
    is_symbol = False

    while True:
        is_letter, is_digit, is_symbol = False, False, False
        for letter in new_password:
            if letter in string.ascii_letters:
                is_letter = True
                break
    
        for number in new_password:
            if number in string.digits:
                is_digit = True
                break
    
        for symbol in new_password:
            if symbol in string.punctuation:
                is_symbol = True
                break
            
           
       # print(is_letter, is_digit, is_symbol)    
        if is_letter and is_digit and is_symbol:
            break
        else:
            storage = random.choices(pool, k=length)
            new_password = "".join(storage)
            print('checked',new_password)
    return new_password
    

result = password(user)
print(result)

# length = 8
# pool = string.ascii_letters + string.digits + string.punctuation
# storage = random.choices(pool, k=length)
# new_password = "".join(storage)

    
# is_letter = False
# is_digit = False
# is_symbol = False

# while True:
#     for letter in new_password:
#         if letter in string.ascii_letters:
#             is_letter = True
#             break
    
#     for number in new_password:
#         if number in string.digits:
#             is_digit = True
#             break
    
#     for symbol in new_password:
#         if symbol in string.punctuation:
#             is_symbol = True
#             break
#     print(is_letter, is_digit, is_symbol)     
#     if is_letter == is_digit == is_symbol:
#             break
#     else:
#             storage = random.choices(pool, k=length)
#             new_password = "".join(storage)
#             print(new_password)