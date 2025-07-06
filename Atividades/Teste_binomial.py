def fatorial(n):				# Definição da função que calcula o fatorial
	if (n < 0):
		return (0)
	if (n == 1) or (n == 0):
		return (1)
	else:
		i = fat = 1
		while i <= n:
			fat = fat * i
			i = i + 1
		return(fat)
		
def test():
	assert fatorial (0) == 1
def test():
	assert fatorial (1) == 1	
def test():
	assert fatorial (2) == 2
def test():
	assert fatorial (3) == 6
def test():
	assert fatorial (4) == 24
def test():
	assert fatorial (5) == 120