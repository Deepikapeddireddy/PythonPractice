def add(n1,n2):
  return print(f"sum = {n1+n2}")

def sub(n1,n2):
  return  print(f'difference = {n1-n2}')

def mul(n1,n2):
  return print(f'product = {n1*n2}')

def div(n1,n2):
  return print(f'quotient = {n1/n2}')

def mod(n1,n2):
  return print(f'remainder = {n1%n2}')

n1 = int(input('Enter a number : '))
op = input("Choose one of these (+ , -, *, /, %) : ")
n2  = int(input("Enter another number : "))
operations = {
  "+" :add,
  "-": sub,
  "/":div,
  '%':mod,
  '*':mul
  
}
if op not in operations:
  print("You have choosen a wrong operator ...")
else:
  function_name  =operations[op]
  function_name(n1,n2)




# if op == '+':
#   print(f'sum = {add(n1,n2)}')
# elif op == '-':
#   print(f'difference = {sub(n1,n2)}')
# elif op == '*':
#   print(f'product = {mul(n1,n2)}')
# elif op == '/':
#   print(f'quotient = {div(n1,n2)}')
# elif op == '%':
#   print(f'remainder = {mod(n1,n2)}')
# else:
#   print("You have choosen a wrong operator ...")
  