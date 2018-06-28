#celius to fahrenheit converter program
#this example is used decorators

def temperatures(t):
    def celsiustofahrenheit(x):
        y = (x*1.8)+32
        return y

    res = "This is "+str(celsiustofahrenheit(t))+"(F)"
    return res

print(temperatures(float(raw_input("Please enter temperature: "))))
