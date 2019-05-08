# 8-15. Printing Models: Put the functions for the example
# print_models.py in a separate file called printing_functions.py.
# Write an import statement at the top of print_models.py, and modify
# the file to use the imported functions.

import printing_functions as p_f

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

p_f.print_models(unprinted_designs, completed_models)
p_f.show_completed_models(completed_models)
