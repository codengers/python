#2 to 10 table matrix

def print_table():
    for i in range(2, 11):
        if i == 11:
             return("11 is not in count")
        for j in range(1, 11):
            q = i*j
            print("{} X {} = {}".format(i,j,q))
            if j==10:
               print("\n")
                


print_table()
