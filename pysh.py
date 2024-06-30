print("   |Python pyShell")
print("   |pysh")
print("   |The source code is in https://github.com/hellowindowZ/pysh")
while True:
    inp = input(">>>|")
    if 'inp' in inp:
        print("You can't use the variable name 'inp'!\n")
    else:
        try:
            exec(inp)
        except Exception as e:
            print("Error: {e}\n")





