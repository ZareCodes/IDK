import sys
jens = 0
while jens == 0:
    Y_N = input("Conitue")
    if Y_N == "n":
    	sys.exit()
    jens =int(input("chand ta jens dari?"))
while jens >0 : 
    command = input("waiting")
    amount = int(input("che ghadr? "))
    jens = jens - amount
    text = " ta jens foorookhtim"
    print(jens + str(text))