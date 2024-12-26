seats = 10
while seats>0:
	text = " seats left"
	banana = input("type sell to sell a seat")
	if banana == "sell":
	    seats = seats - 1
	    print(str(seats) + text )
	elif banana == "add":
		seats = seats + 1
		print(str(seats) + text )
	else:
		print("error")
		break
while seats2 == 0:
	print("seats sold out")