my_var= """Manuelita vivia en pehuajo
pero un dia se marcho.
Nadie supo bien por que 
a Paris ella se fue,
un poquito caminando
y otro poquito a pie""".split()

my_var1 = [word for word in my_var if word[0].isupper()]
print(my_var1)