#display all positions of sub string in string.
#Enter string and sub string below
str=input("Please enter string: ")
sub=input("Please enter sub string: ")

i=0
n=len(str)
flag=False
while i<n:
    pos=str.find(sub, i, n)
    if pos!=-1:
        print("Here is sub string: ", pos+1)
        i=pos+1
        flag=True
    else:
        i=i+1
if flag==False:
    print("sub string not found.")
    
