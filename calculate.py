while True:
	db = {"i":[int(input("\x1b[32mEnter a Number > ")),int(input("\x1b[33mEnter a Number > ")),input("\x1b[35m+ - / * ** > ")]}
	def calculate(num,num2,action):
		print("\x1b[36m",end="")
		eval(f'print(db["i"][0],db["i"][2],db["i"][1],"=",{num}{action}{num2},end="")')
		print("\x1b[39m")
	calculate(db["i"][0],db["i"][1],db["i"][2])