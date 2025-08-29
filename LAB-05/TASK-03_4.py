f=open("numbers.txt","r")
nums=f.readlines()
f.close()
squares=[]
for n in nums:
    squares.append(int(n)*int(n))
f2=open("squares.txt","w")
for sq in squares:
    f2.write(str(sq)+"\n")
f2.close()
print("Squares written")