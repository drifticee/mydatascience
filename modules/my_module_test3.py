def func(a):
	print("input num: ", a)

if  __name__ =="__main__":
	print("Only when directly running the module.")
	func(37)
else:
	print("When running the module with importing.")