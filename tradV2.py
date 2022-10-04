##############
#     By     #
#  Tomichau  #
##############



def db(dec):
    itsNull = 0
    numbers = []
    number = 0
    nbBoites = dec
    nbReste = 0
    print("Q -> Quotient , R -> Reste , / -> division euclidienne")
    while itsNull < 1 :
        boites = nbBoites
        nbReste = nbBoites % 2
        nbBoites = nbBoites // 2

        if nbReste > 0 :
            number = 1
        else:
            number = 0
        
        numbers.append(str(number))
        print("On divise", boites, "par 2 donc :")
        print(boites,"/2 Q=", nbBoites, "R=", nbReste)
        if nbBoites == 0:
            itsNull = 1
        else:
            itsNull = 0
    print("Q = 0 donc on arrete")
    print("on recupere tous les Restes que nous avons obtenue")
    print("ce qui nous donne pour l'instant : ", " ".join(numbers))
    print("Puis on inverse ce qui nous donne le resultat final :")
    numbers.reverse()
    print("("+str(dec)+")10 -> ("+ "".join(numbers)+")2")
    
def bd(binaire):
    binaire = str(binaire)
    binaire = reverses(binaire)
    
    calculate = 0
    calculates = []
    n = 0 
    print("^ -> puissance ")
    for i in binaire:
        if i == '1':
           calculate = calculate + 2**n
           calculates = calculates + ["2^"+str(n)]
           print("le rang",n,"est egal    1 donc on le prend")
        else:
            calculate = calculate + 0
            print("le rang",n,"est egal    0 donc on le vire")
        n += 1
    print("On prend tous les rang qui son egal    1")
    print("On fait la somme tout en utillisant leur rang en puissance")
    print("donc : ")
    print(" + ".join(calculates),"=",calculate)
    print("("+reverses(binaire)+")2 -> ("+str(calculate)+")10")

def dh(dec):
    itsNull = 0
    numbers = []
    number = 0
    nbBoites = dec
    nbReste = 0
    print("Q -> Quotient , R -> Reste , / -> division euclidienne")
    while itsNull < 1 :
        boites = nbBoites
        nbReste = nbBoites % 16
        nbBoites = nbBoites // 16
        print("On divise", boites, "par 16 donc :")
        print(boites,"/16 Q=", nbBoites, "R=", nbReste)
        if nbReste >= 10:
            if nbReste ==  10:
                number = "A"
            elif nbReste == 11:
                number = "B"
            elif nbReste == 12:
                number = "C"
            elif nbReste == 13:
                number = "D"
            elif nbReste == 14:
                number = "E"
            elif nbReste == 15:
                number = "F"
            print("sachant que",nbReste,"en hexadecimal cela fait",number)
        else:
            number = nbReste
        
        numbers.append(str(number))

        if nbBoites == 0:
            itsNull = 1
        else:
            itsNull = 0
    print("Q = 0 donc on arr  te")
    print("on recupere tous les Restes que nous avons obtenue")
    print("ce qui nous donne pour l'instant : ", " ".join(numbers))
    print("Puis on inverse ce qui nous donne le r  sultat final :")
    numbers.reverse()
    print("("+str(dec)+")2 -> ("+"".join(numbers)+")16")

def hd(hex):
    hex= str(hex)
    hex = reverses(hex)
    
    calculate = 0
    calculates = []
    n = 0 
    print("^ -> puissance")
    for i in hex:
        if hex[n] == "A" or hex[n] == "a":
            calculate = calculate + 10*16**n
            calculates = calculates + ["10*16^"+str(n)]
            print("sachant que",hex[n],"en decimal donne 10")
        elif hex[n] == "B" or hex[n] == "b":
                calculate = calculate + 11*16**n
                calculates = calculates + ["11*16^"+str(n)]
                print("sachant que",hex[n],"en decimal donne 11")
        elif hex[n] == "C" or hex[n] == "c":
            calculate = calculate + 12*16**n
            calculates = calculates + ["12*16^"+str(n)]
            print("sachant que",hex[n],"en decimal donne 12")
        elif hex[n] == "D" or hex[n] == "d":
            calculate = calculate + 13*16**n
            calculates = calculates + ["13*16^"+str(n)]
            print("sachant que",hex[n],"en decimal donne 13")
        elif hex[n] == "E" or hex[n] == "e":
            calculate = calculate + 14*16**n
            calculates = calculates + ["14*16^"+str(n)]
            print("sachant que",hex[n],"en decimal donne 14")
        elif hex[n] == "F" or hex[n] == "f":
            calculate = calculate + 15*16**n
            calculates = calculates + ["15*16^"+str(n)]
            print("sachant que",hex[n],"en decimal donne 15")
        else:
            calculate = calculate + int(hex[n])*16**n
            calculates = calculates + [str(hex[n])+"*16^"+str(n)]
        n += 1
    print("On fait la somme en multipliant la valeur par 16 avec la puissance de son rang :")
    print(" + ".join(calculates),"=",calculate)
    print("donc :")
    print("("+hex+")16 -> ("+str(calculate)+")10")

def hb(hex):
    return db(hd(hex))

def bh(bin):
    return dh(bd(bin))

def reverses(s):
    new_string = ''
    index = len(s)
    while index:
        index -= 1                   
        new_string += s[index] 
    return new_string
