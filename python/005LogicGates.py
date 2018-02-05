#!/usr/bin/python3.6

#Begin temp global dictionary, string, and test field
Eqto='is equal to {}.'
indent='     '
#End temp global dictionary, string, and test field

#graphical representation of logic circuit for user
print("A--|``-.")
print("B--|AND :-?---------------------------------------\``-.")
print("C--|..-`                                           |OR :--?")
print("                                             |----/..-`")
print("A--\``-.                                     |")
print("B---|OR :-?-------------------------|``-.    |")
print("C--/..-`                            |AND :--?")
print("                                 |--|..-`")
print("                        |`-._    |")
print("                      |-|NOT_]o--|")
print("A--|``-.              | |.-`")
print("   |AND :---          |")
print("B--|..-`   |          |")
print("           |          |")
print("B--|``-.    --\``-.   |")
print("   |AND :------|OR :--╩ ----------------------------------?")
print("C--|..-`    --/..-`")
print("           |")
print("B--|``-.   |") 
print("   |AND :---")
print("C--|..-`")
print()
print()

#def for cases when [A,B,C] != (1 or 0)
def terminate():
    print('Please input either a 1 or 0 only. The program will now be close. Please relaunch the program')
    input("Please press enter to close the program.")
    quit()

#Input for [A,B,C] with def terminate()
A=int(input("Is A 1 or 0? 1 is True, 0 is False.  "))
if A == 0:
    print(indent + "A " + Eqto.format(A))
else:
    if A == 1:
        print(indent + "A " + Eqto.format(A))
    if A != 1 and A != 0:
        terminate()

B=int(input("Is B 1 or 0? 1 is True, 0 is False.  "))
if B == 0:
    print(indent + "B " + Eqto.format(B))
else:
    if B == 1:
        print(indent + "B " + Eqto.format(B))
    if B != 1 and B != 0:
        terminate()

C=int(input("Is C 1 or 0? 1 is True, 0 is False.  "))
if C == 0:
    print(indent + "C " + Eqto.format(C))
else:
    if C == 1:
        print(indent + "C " + Eqto.format(C))
    if C != 1 and C != 0:
        terminate()
print ()
print ()
print ("A is {}, B is {}, and C is {}.".format(A, B, C))
print("If this is correct please press enter.  If this is not correct,")
input("please close the program and reopen it.")
#Roman script of logic circuit
print()
print()
print("This logic circuit is defined as:")
print(indent + "A and B and C will yeild T2")
print(indent + "A or B or C will yeild T1")
print(indent + "(A and B) or (A and C) or (B and C) will yeild F2")
print(indent + "Not F2 and T1 will yeild T3")
print(indent + "T2 or T3 will yeild F1")
print()
print()

'''
Remove this long comment to create whitespace for logic circuit
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
print()
'''
#Operators for logic table and calculation
print()
print("For the following answers, 1 is True, and 0 is False.")
print()
print()
# AandBandC =T2
if A == 0 or B == 0 or C==0:
    T2=0
else:
    T2=1
#AorBorC =T1
if A==0 and B==0 and C==0:
    T1=0
else:
    T1=1
# (AandB=X) or (AandC=Y) or (BandC=Z)=F2
if A==0 or B==0:
    X=0
else:
    X=1
if A==0 or C==0:
    Y=0
else:
    Y=1
if B==0 or C==0:
    Z=0
else:
    Z=1
if X==0 and Y==0 and Z==0:
    F2=0
else:
    F2=1

# [Not_(AandB)or(AandC)or(BandC)]and(AorBorC)=T3
NF2=not F2
if NF2==0 or T1==0:
    T3=0
else:
    T3=1

#T2orT3 =F1
if T2==0 and T3==0:
    F1=0
else:
    F1=1



#graphical representation of logic circuit
print("{}--|``-.".format(A))
print("{}--|AND :-'{}'-------------------------------------\``-.".format(B, T2))
print("{}--|..-`                                           |OR :--'{}'".format(C, F1))
print("                                             |----/..-`")
print("{}--\``-.                                     |".format(A))
print("{}---|OR :-'{}'-----------------------|``-.    |".format(B, T1))
print("{}--/..-`                            |AND :--'{}'".format(C, T3))
print("                                 |--|..-`")
print("                        |`-._    |")
print("                      |-|NOT_]o--|")
print("{}--|``-.              | |.-`".format(A))
print("   |AND :---          |")
print("{}--|..-`   |          |".format(B))
print("           |          |")
print("{}--|``-.    --\``-.   |".format(B))
print("   |AND :------|OR :--╩ ----------------------------------'{}'".format(F2))
print("{}--|..-`    --/..-`".format(C))
print("           |")
print("{}--|``-.   |".format(B)) 
print("   |AND :---")
print("{}--|..-`".format(C))
print()
print("T2 is {}, T1 is {}, F2 is {}, T3 is {}, and F1 is {}.".format(T2, T1, F2, T3, F1))
print()
exit=input("Press enter to end the program.")
exit(0)
r
x
sys.exit()
