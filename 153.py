while 1:
	print ("\n\nE N T E R  V A L U E S:")
	ax = raw_input("A(x): ")
	bx = raw_input("B(x): ")
	px = raw_input("P(x): ")
	choice = raw_input ("\n[1] A(x) + B(x)\n[2] A(x) - B(x)\n[3] A(x) x B(X)\n[4] A(x) / B(x) \n[5] Exit \nEnter choice of operation: ")


	ax = [int(a) for a in ax.split(" ")]
	bx = [int(b) for b in bx.split(" ")]
	px = [int(p) for p in px.split(" ")]
	cx = [0 for c in range (0, max(len(ax),len(bx)))]

	#defining length of a&b
	lena = len(ax)
	lenb = len(bx)

	#defining exponent
	if lena > lenb:	exponent = lena
	elif lenb > lena: exponent = lenb

	#input_validation
	def error_printing(r, s):
		for r in s:
			if r < 0:	
				print "\nERROR no negative coefficient."

			elif r > 2**exponent-1:	
				print "\nERROR Beyond maximum coefficient in "

		
			#elif r.isdigit() == False:
			#	print "\nERROR A(x) should be digits only"

	error_printing(a, ax)
	error_printing(b, bx)
	error_printing(p, px)


	#stuffing
	i=0
	if lena > lenb:	
		lendiff = lena-lenb
		while i < lendiff:
			bx.insert(0,0)
			i+=1

	elif lenb > lena:	
		lendiff = lenb-lena
		while i < lendiff:
			ax.insert(0,0)
			i+=1

	#printing
	print ("\n\nP R I N T I N G  V A L U E S")
	print "A(x): ", ax
	print "B(x): ", bx
	print "choice", choice

	def print_given(p):
		power = len(p)-1
		for k in p:
			if power > 0:
				print int(k),"x^",power,"+",
				power-=1
			else:	print (k)

	print "A(x):",
	print_given(ax)

	print "B(x):",
	print_given(bx)


	#working with choice
	#addition
	if (choice == "1"):
		for x in range (0, len(ax)) :
			cx[x] = ax[x]^bx[x]
			x+=1
		print "\nS O L U T I O N:"

		print " ",
		for m in ax:
			print m, " ",
		print "\n+",
		for m in bx:
			print m, " ",
		print "\n"
		print " ",
		for m in cx:
			print m, " ",
		print "\n\nA(x)+B(x) = ", print_given(cx)

	#subtraction
	elif (choice == "2"):
		for x in range (0, len(bx)) :
			cx[x] = ax[x]^bx[x]
			x+=1
		print "\nS O L U T I O N:"

		print " ",
		for m in ax:
			print m, " ",
		print "\n+",
		for m in bx:
			print m, " ",
		print "\n"
		print " ",
		for m in cx:
			print m, " ",
		print "\n\nA(x) - B(x) = ", print_given(cx)

	#multiplication
	#elif (choice == "3"):

	#division
	#elif (choice == "4"):

	elif (choice == "5"):	exit(0)
