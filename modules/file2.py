#If module import module.function_or_var
import file1
file1.fun() #Inside file 1 > fun method

# If from module import func_or_var , directly use it
from file1 import fun
fun()  #Inside file 1 > fun method

#If from module import * Means all imported directly
from file3 import *
fun_file_3() #Inside file 3 > fun_file_3 function 
