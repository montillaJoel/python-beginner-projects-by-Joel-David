while True:
 try:
   first_number= int(input('Enter a number a: '))
   break
 except ValueError:
    print('Is a number no letter')
while True:
  try:
   second_number= int(input('Enter a number b: '))
   break
  except ValueError:
     print('Is a number no letter')
input_operation= input('Choose: +, -, *, / ')

def operation(first, second, chosen_operand):
    while True:
         if chosen_operand == '+': 
             result_number = (first + second) 
             break
         elif chosen_operand == '-': 
             result_number = (first - second)
             break
         elif chosen_operand == '*': 
             result_number = (first *second)
             break
         elif chosen_operand == '/':
              while True: 
                try:
                  result_number = (first / second)
                  break
                except ZeroDivisionError:
                  print("Can't divide by 0")
                  while True:
                     try:
                        second = int(input('Enter a number b but not 0: '))
                        break
                     except ValueError:
                          print('Is a number no letter')
                
              break  

         else: 
            chosen_operand = input('Choose: +, -, *, / ')
    return result_number

result = operation(first_number, second_number, input_operation)
print(result)
