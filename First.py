month1 = raw_input("Enter month:")
month = str(month1)

if month=="January" or month=="February" or month=="March" or month=="April":
	print("Winter is here")
elif month=="May" or month=="June":
	print("Spring is here")
elif month=="June" or month=="August":
	print("Summer is here")
elif  month=="September" or month=="October" or month=="November" or month=="December":
	print("Fall is here")
else:
	print("quit your jibberish!")