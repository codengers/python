#Program to create a pyramid which is right angled triangle shape.

#create a row
for i in range(1, 11):
    for j in range(1, i+1):
        print('*', end='')
    print()
	
#another type using single
for i in range(1, 11):
    print('*'*i)
