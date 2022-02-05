
# Day 6 Assignment : Floor divison of any two number by using Decorators.


def mod_div(fun):
	def deno(a, b):
		if a < b :
			a, b = b, a
		return fun(a, b)
	return deno
	


a, b = (int(i) for i in input("Enter two Nunbers: ").split())
@mod_div
def div(a, b):
	return  a // b

#div = mod_div(div)
print(div(a, b))