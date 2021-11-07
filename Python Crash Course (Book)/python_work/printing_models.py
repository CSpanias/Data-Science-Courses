# 8.15
import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs[:], completed_models)
pf.show_completed_models(completed_models)

# 8.16
import printing_functions

printing_functions.print_models(unprinted_designs[:], completed_models)
printing_functions.show_completed_models(completed_models)

from printing_functions import *

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)

from printing_functions import print_models as pm, show_completed_models as scm

pm(unprinted_designs, completed_models)
scm(completed_models)
