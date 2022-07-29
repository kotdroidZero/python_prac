

try :
    name = int(input("Enter a number : "))
except:
    print('Something went wrong! ')
else:
    print('Everything worked')
finally:
    print("Finaly always runs")            

