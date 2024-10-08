import math as m

# layer height
h = 10
# width of the layer
w = 24

# d = 上下層疊合比例
d = 1- (h* m.tan(m.pi/12))/ w
'''
目前先使用弧度，之後再改成角度。
'''

print(d)