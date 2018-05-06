from collections import OrderedDict
def a(str):
	return "".join(set(str))
def b(str):
	return "".join(OrderedDict.fromkeys(str)) 
if __name__ == "__main__":
	str = raw_input("enter:")
	print "Without Order = ",a(str)
	print "With Order = ",b(str)
