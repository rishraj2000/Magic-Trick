print("Hello There !!! ")
print("crazy engineers!!"
print("\n")

print("This is a MAGIC TRICK which will read your mind !!!")

print("Follow the instructions.")

print("\n")

n = 21

main = [i for i in range(1,n+1)]

print("These are the set of numbers >>")

print("\n")

print(main)

print("\n")

print("Remember a number from the above set of numbers.")

print("\n")

a = main[0:int(n / 7)]

b = main[int(n / 7):int((2 * n) / 7)]

c = main[int((2 * n) / 7):int((3 * n) / 7)]

d = main[int((3 * n) / 7):int((4 * n) / 7)]

e = main[int((4 * n) / 7):int((5 * n) / 7)]

f = main[int((5 * n) / 7):int((6 * n) / 7)]

g = main[int((6 * n) / 7): 21]



aa = []

for i in range(0,1):



    aa.append(a[i])

    aa.append(b[i])

    aa.append(c[i])

    aa.append(d[i])

    aa.append(e[i])

    aa.append(f[i])

    aa.append(g[i])



bb = []

for i in range(1,2):



    bb.append(a[i])

    bb.append(b[i])

    bb.append(c[i])

    bb.append(d[i])

    bb.append(e[i])

    bb.append(f[i])

    bb.append(g[i])



cc = []

for i in range(2,3):



    cc.append(a[i])

    cc.append(b[i])

    cc.append(c[i])

    cc.append(d[i])

    cc.append(e[i])

    cc.append(f[i])

    cc.append(g[i])

print("These are the three sets : ")

print("\n")

print("1st set ; " +  str(aa))

print("2nd set ; " +  str(bb))

print("3rd set ; " +  str(cc))

print("\n")

x = int(input("Enter the  set number in which you remembered number lies >>  "))

if(x == 1):

    main = bb + aa + cc

elif(x == 2):

    main = cc + bb + aa

elif(x == 3):

    main = aa + cc + bb

else:

    print("Invalid input !!!")

    exit()



print("\n")

print("--------------------------------------------------------------------------------------")

print("\n")

a = main[0:int(n / 7)]

b = main[int(n / 7):int((2 * n) / 7)]

c = main[int((2 * n) / 7):int((3 * n) / 7)]

d = main[int((3 * n) / 7):int((4 * n) / 7)]

e = main[int((4 * n) / 7):int((5 * n) / 7)]

f = main[int((5 * n) / 7):int((6 * n) / 7)]

g = main[int((6 * n) / 7): 21]



aa = []

for i in range(0,1):



    aa.append(a[i])

    aa.append(b[i])

    aa.append(c[i])

    aa.append(d[i])

    aa.append(e[i])

    aa.append(f[i])

    aa.append(g[i])



bb = []

for i in range(1,2):



    bb.append(a[i])

    bb.append(b[i])

    bb.append(c[i])

    bb.append(d[i])

    bb.append(e[i])

    bb.append(f[i])

    bb.append(g[i])

cc = []

for i in range(2,3):



    cc.append(a[i])

    cc.append(b[i])

    cc.append(c[i])

    cc.append(d[i])

    cc.append(e[i])

    cc.append(f[i])

    cc.append(g[i])

print("These are the three sets : ")

print("\n")

print("1st set ; " +  str(aa))

print("2nd set ; " +  str(bb))

print("3rd set ; " +  str(cc))

print("\n")

x = int(input("Enter the  set number again in which you remembered number lies >>  "))

if(x == 1):

    main = bb + aa + cc

elif(x == 2):

    main = cc + bb + aa

elif(x == 3):

    main = aa + cc + bb

else:

    print("Invalid input !!!")

    exit()

print("\n")

print("--------------------------------------------------------------------------------------")

print("\n")

a = main[0:int(n / 7)]

b = main[int(n / 7):int((2 * n) / 7)]

c = main[int((2 * n) / 7):int((3 * n) / 7)]

d = main[int((3 * n) / 7):int((4 * n) / 7)]

e = main[int((4 * n) / 7):int((5 * n) / 7)]

f = main[int((5 * n) / 7):int((6 * n) / 7)]

g = main[int((6 * n) / 7): 21]



aa = []

for i in range(0,1):

    aa.append(a[i])

    aa.append(b[i])

    aa.append(c[i])

    aa.append(d[i])

    aa.append(e[i])

    aa.append(f[i])

    aa.append(g[i])



bb = []

for i in range(1,2):

    bb.append(a[i])

    bb.append(b[i])

    bb.append(c[i])

    bb.append(d[i])

    bb.append(e[i])

    bb.append(f[i])

    bb.append(g[i])

cc = []

for i in range(2,3):

    cc.append(a[i])

    cc.append(b[i])

    cc.append(c[i])

    cc.append(d[i])

    cc.append(e[i])

    cc.append(f[i])

    cc.append(g[i])

print("These are the three sets : ")

print("\n")

print("1st set ; " +  str(aa))

print("2nd set ; " +  str(bb))

print("3rd set ; " +  str(cc))

print("\n")

x = int(input("For the last time...enter the  set number in which you remembered number lies >>  "))

if(x == 1):

    main = bb + aa + cc

elif(x == 2):

    main = cc + bb + aa

elif(x == 3):

    main = aa + cc + bb

else:

    print("Invalid input !!!")

    exit()

   
print("\n")

print("--------------------------------------------------------------------------------------")

print("\n")

print("\n" + "The number you remebered is >>   " + str(main[10]))

print("\n")

print("Amazing right !!!")
