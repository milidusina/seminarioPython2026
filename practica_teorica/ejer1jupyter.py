my_cond = True
def my_op(par1,par2, is_sum=my_cond):
    print(par1 + par2 if is_sum else par1 - par2)

result = my_op(10,4)
result = my_op(10,4, False)
my_cond = False
result = my_op(10,4)
print(result)
