print('\033[1;33;44m Ola Mundo\033[m')
adjetivo = 'Lindo'
cores = {'azul':'\033[34m'}

print('O céu é \033[34m azul \033[m e {}{}'.format(cores['azul'], adjetivo))

#codigo para cor = \033[m
# \033[0;30;40m
#1 linha= 0; 1; 4; 7
#2 linha= 30 a 37
#3 linha= 40 a 47