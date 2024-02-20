def f(x):
    result= x ** 2 + 1
    return result

print(f(10))

def juros(preco, juros):
    res = preco * (1 + (juros/100))
    return res

print (juros(10,50)*2)