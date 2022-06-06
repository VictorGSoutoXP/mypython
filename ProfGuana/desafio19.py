import math
an = float(input('digite o angulo q deseja?'))
r = math.radians(an)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('se o angulo for {} \n o seno sera {:.3f} \n o coseno sera{:.3f} \n e a trangente sera {:.3f}'.format(an, s, c, t))