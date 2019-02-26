# 8-16. Imports: Using a program you wrote that has one function in it,
# store that function in a separate file. Import the function into
# your main program file, and call the function using each of these
# approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

import simple_message
simple_message.display_message()
print('-----------------------------')

from simple_message import display_message
display_message()
print('-----------------------------')

from simple_message import display_message as fn
fn()
print('-----------------------------')

import simple_message as mn
mn.display_message()
print('-----------------------------')

from simple_message import *
display_message()
print('-----------------------------')
