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


	#input_validation
	def error_printing(r, s):
		#defining exponent
		if lena > lenb:	exponent = lena
		elif lenb > lena: exponent = lenb
		elif lenb == lena: exponent = lena

		for r in s:
			if r < 0:	
				print "\nERROR no negative coefficient."
				exit(0)

			elif r > 2**exponent-1:	
				print "\nERROR Beyond maximum coefficient."
				exit(0)

	error_printing(a, ax)
	error_printing(b, bx)
	for p in px:
		if p < 0:	
			print "\nERROR no negative coefficient."
		elif (len(px) == 1):
			print "ERROR invalid power input in P(x)."
			exit(0)

		elif (int(p) != 1 and int(p) != 0):
			print "\nERROR Only binary input are accepted in P(x)."
			exit(0)

	#stuffing  0s
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

	def mult(b, a, p_int, p_string):
		print "\n", a, "x", b
		b_binary = bin(b)[2:]
		a_binary = bin(a)[2:]
		b_int = int(b_binary)
		a_int = int(a_binary)
		product = b_int*a_int
		#product = int(bin(a)[2:])*int(bin(b)[2:])
		prod_string = str(product)
		modulo = ""
		xor = ""

		print "x: ", a_binary
		print "y: ", b_binary
		
		for i in prod_string:
			if int(i) > 1:
				modulo += str(int(i)%2)
			else:
				modulo += i

		prod_string = modulo
		print "x*y", prod_string

		if (len(prod_string) >= len(p_string)):
			p_list = [0 for i in range(0,len(prod_string))]
			prod_list = [0 for i in range(0,len(prod_string))]
			if prod_string[0] == "0":
				prod_string = prod_string[1:]
				print "prod_str: ", prod_string
				for j in range(0,len(prod_string)):
					xor += str(int(prod_string[j])^int(p_string[j]))

			else:
				for i in range(0, len(prod_string)-len(p_string)):
					p_string = p_string + "0"
				for j in range(0,len(prod_string)):
					xor += str(int(prod_string[j])^int(p_string[j]))
		else:
			xor = prod_string

		#print "Product: ", int(xor, 2)
		return int(xor, 2)

	#printing
	print ("\n\nP R I N T I N G  V A L U E S")
	print "A(x): ", ax
	print "B(x): ", bx

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
		print "\n-",
		for m in bx:
			print m, " ",
		print "\n"
		print " ",
		for m in cx:
			print m, " ",
		print "\n\nA(x) - B(x) = ", print_given(cx)

	#multiplication
	elif (choice == "3"):
		add = [0 for i in range(0, len(ax)+len(bx)-1)]
		p_string = ""

		for i in px:
			p_string += str(i)
		print "p_string: ", p_string

		p_int = int(p_string, 2)
		print "p_int: ", p_int

		ctrb = -1
		for i in bx:
			ctrb += 1
			ctra = ctrb - 1
			for j in ax:
				ctra += 1
				add[ctra] = add[ctra]^mult(i, j, p_int, p_string)

		print "\n\n"		
		print " ",
		for m in ax:
			print m, " ",
		print "\nx",
		for m in bx:
			print m, " ",
		print "\n"
		print " ",
		for m in add:
			print m, " ",
		print "\n\nA(x) - B(x) = ", print_given(add)
	

	elif (choice == "4"):
		print "Module not available."	
		exit(0)		

	elif (choice == "5"):	exit(0)
