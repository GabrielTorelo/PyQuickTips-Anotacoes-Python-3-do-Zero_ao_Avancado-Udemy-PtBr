a = 'A'
b = 'B'
c = 1.12

string = 'a={}, b={}, c={}'
formatado = string.format(a, b, c)
print(formatado)

msg_BA = 'b={1}, c={0}'.format(c, b)
print(msg_BA)

msg_par_nomeado = 'a={letra_a}, c={letra_c:.2f}'.format(letra_a=a, letra_c=c)
print(msg_BA)
