name = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letras maiúsculas é: {}'.format(name.upper()))
print('Seu nome em letras minúsculas é: {}'.format(name.lower()))
#print('Seu nome possui um total de {} caracteres'.format(len(name) - name.count(' ')))
print('Seu nome possui um total de {} caracteres'.format(len(name.replace(' ',''))))
print('Seu primeiro nome possui {} letras'.format(len(( name.split() ) [0])))
#print('Seu primeiro nome possui {} letras'.format(name.find(' ')))
