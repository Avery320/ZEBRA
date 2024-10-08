__author__     = ['Avery Tsai']
__email__      = ['n76124052@gs.ncku.edu.tw']

import math 

class Vertex:
    
    '''
    A vertex defines a point in 3D space.
    '''
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.fix = False
        self.generation = 0
        self.edges = []