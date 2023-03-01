from math import hypot
adj = float(input('Digite o cateto adjacente'))
op = float(input('Digite o cateto oposto'))
print('Com adjacente {} e oposto {} a hipotenusa é {:.2f}'.format(adj, op, hypot(adj, op)))
