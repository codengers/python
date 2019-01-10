#this is used to print multiplication table upto 10.

for i in range(1, 11):
    for j in range(1, 11):
        print('{} * {} = {} \t'.format(j, i, i*j), end=' ')
    print()