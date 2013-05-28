from codejam.utils.codejamrunner import CodeJamRunner
import codejam.utils.graphing as graphing
import networkx as nx
from decimal import *
import codejam.utils.polynomials as pol

class Dynam(object):pass


factors = [2,2,5,5]

def solver(data):

    hcf = 1
    pd_temp = data.Pd
    
    for fac in factors:
        if pd_temp % fac == 0:
            pd_temp = pd_temp / fac
            hcf *= fac

    if 100 / hcf > data.N:
        return 'Broken'

    if data.Pg == 100 and not data.Pd == 100:
        return 'Broken'

    if data.Pg == 0 and not data.Pd == 0:
        return 'Broken'

    return 'Possible'


def data_builder(f):

    data = Dynam()

    data.N, data.Pd, data.Pg = f.get_ints()

    return data


cjr = CodeJamRunner()
cjr.run(data_builder, solver, problem_name = "A", problem_size='large-practice')
