import string
my_num1 = [n for n in range(10)]
my_num2 = [int(n) for n in string.digits]

print(f"La suma de {my_num1 = } es {sum(my_num1)}")
print(f"La suma de {my_num2 = } es {sum(my_num2)}")
print(sum(my_num2))