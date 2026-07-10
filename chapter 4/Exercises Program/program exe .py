h1=int(input("Enter first time hours:"))
m1=int(input("Enter fist time mints:"))
s1=int(input("Enter first time seconds"))
h2=int(input("Enter second time hours:"))
m2=int(input("Enter second time mints:"))
s2=int(input("Enter second time seconds"))
s=s1+s2
s=s%60
m=(s1+s2)/60
m=m+m1+m2
m=m%60
h=(m1+m2)/60
h=h+h1+h2
print("HH : MM : SS")
print(int(h),":",int(m),":",int(s))
