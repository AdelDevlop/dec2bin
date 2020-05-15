def getBits( n ) :
    p = 1
    l = []
    for i in range(n):
        l.append(p)
        p = 2*p
    return l

def decToBin( dec, fmt ) :
    l = getBits(fmt)
    index  = -1
    for i in range(len(l)) :
        if ( l[i] == dec ) :
            index = i
            break
        if ( l[i] > dec ):
            if i > 0 :
                index = i - 1
                break
    if ( index < 0 ):
        index = len(l) - 1
    s = 0
    bits = []
    for k in range(index, len(l)-1):
        bits.append(0)
    for j in range(index, -1, -1) :
        s += l[j]
        if (s <= dec):
            bits.append(1)
        else :
            bits.append(0)
            s -= l[j]

    strg = ""
    for elt in bits :
        strg += str(elt)
    return strg
    

fmt_base 		= 64
dec_number_max 	= 65540 

f = open("bin.txt", "w")
last_converted = ""
i = 0
stop = False
while (not stop) :
    dec_to_bin = decToBin(i, fmt_base) 
    if (dec_to_bin == last_converted) :
    	print("Stoped at ", i-1)
    	stop = True
    	continue
    last_converted = dec_to_bin
    f.write(str(i) + "\t\t\t" + dec_to_bin + "\n")
    i += 1
f.close()