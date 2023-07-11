# \r\n -> CRLF (windows)

# \n -> LF (unix/linux)

print(12, 34, sep='-', end='\r\n')
print(56, 78, sep='-')

# sep=''  É o que vai ficar entre os argumentos separando eles....por padrão é um espaço

# end='' É o que vai ficar no final de cada argumento...por padrão é uma quebra de linha \r\n