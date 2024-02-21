# Criação de DocString

def f(x):
    'Exemplo de Documentação de Funções que será impressa por meio da função help'
    result= x ** 2 + 1
    return result

print(f(10))

help(f)