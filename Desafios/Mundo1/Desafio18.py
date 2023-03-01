import math
ang = float(input('Digite o angulo'))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ângulo {} tem como seno {:.2f}'.format(ang, seno))
print('O ângulo {} tem como cosseno {:.2f}'.format(ang, cos))
print('O ângulo {} tem como tangente {:.2f}'.format(ang, tan))
