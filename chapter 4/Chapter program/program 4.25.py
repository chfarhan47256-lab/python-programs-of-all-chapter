sec = int(input("Enter second:"))
h=sec/3600
sec=sec%3600
m=sec/60
sec=sec%60
print("HH: MM :SS")
print(int(h),":",int(m),":",int(sec))