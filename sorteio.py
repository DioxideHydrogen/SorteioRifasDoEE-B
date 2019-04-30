# -*- coding: utf-8; *-
# 10 - 30 x
# 36 x
# 51 - 64 x
# 66 - 70 x
# 81 - 100 x
# 111 - 120 x 
# 131 - 131 x
# 135 - 138 x
# 140 - 143 x
# 147 x
# 161 - 180 x
# 221 - 242 x 
# 261 - 275 x
import random
a = 10;
numeros = [];

while(a<=30):
	numeros.append(a)
	a += 1
numeros.append(36)

a = 51
while(a <= 64):
	numeros.append(a)
	a += 1
a = 66
while(a <= 70):
	numeros.append(a)
	a += 1
a = 81
while(a <= 100):
	numeros.append(a)
	a += 1
a = 111
while(a <= 120):
	numeros.append(a)
	a += 1
a = 135
while(a <= 138):
	numeros.append(a)
	a += 1
a = 140
while(a <= 143):
	numeros.append(a)
	a += 1
numeros.append(147)
a = 161
while(a <= 180):
	numeros.append(a)
	a += 1
a = 221
while(a <= 242):
	numeros.append(a)
	a += 1
a = 261
while(a <= 275):
	numeros.append(a)
	a += 1
x = random.choice(numeros)
y = random.choice(numeros)
print 'Números das Rifas: ', numeros, '\n'
print '1º Ganhador: ',x, '\n2º Ganhador: ', y
