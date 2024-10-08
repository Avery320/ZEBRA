__author__     = ['Avery Tsai']
__email__      = ['n76124052@gs.ncku.edu.tw']

import math
from zebra.core_vertex import Vertex

class Edge:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.face1 = None
        self.face2 = None
    
    def center(self):
        """
        returns the midpoint on an edge as a Vertex() object
        """
        return Vertex((self.v2.x+self.v1.x)/2.0,(self.v2.y+self.v1.y)/2.0,(self.v2.z+self.v1.z)/2.0)