num = input('Insira um número em binário: ')
posini = num.find('1')
num = num[posini:]          #caso os primeiros digitos sejam zero, ele desconsidera e pega o primeiro 1 que tiver
qtd = len(num)
vez = resp = 0
for c in range(qtd):
    elev = 2 ** ((qtd - 1) - vez)
    if c != qtd and num[c] == '1':
        resp += elev
    vez += 1
print(resp)
#fiz em 04/04/2023























'''num = int(input('Insira um número: '))
dec = str(num)
tamanho = len(dec)-1
vez = 0
cu = []
pos = -1
resp = 0
while vez != tamanho+2:
    if dec[0] == '1':
        cu = 2 ** (tamanho - vez)
        pos += 1

        if pos == tamanho + 1:
            break

        if dec[pos] == '1':
            resp += cu
        vez += 1

print(resp)'''