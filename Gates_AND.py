# This is a Python program to illustrate working of AND gate

def AND (a, b):

	if a == 1 and b == 1:
		return True
	else:
		return False

# Driver code
if __name__=='__main__':
	print(AND(1, 1))

	print("+---------------+----------------+")
	print(" | AND Truth Table | Result |")
	print(" A = False, B = False | A AND B =",AND(False,False)," | ")
	print(" A = False, B = True | A AND B =",AND(False,True)," | ")
	print(" A = True, B = False | A AND B =",AND(True,False)," | ")
	print(" A = True, B = True | A AND B =",AND(True,True)," | ")
