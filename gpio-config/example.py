
#file1.py #func
z=x/10
def main_function(z):
    print(z)




#file2.py #rumia
from file1 import main_function
x=10
def dependent_function(x):
    return x #to file1
main_function()



#file3.py #cirno
from file1 import main_function
x=20
def dependent_function(x):
    return x #to file1
main_function()






