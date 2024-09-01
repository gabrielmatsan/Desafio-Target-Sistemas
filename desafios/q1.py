def fibonacci(target):
    if target == 0:
        return 'Faz parte da sequência de Fibonacci'
    if target == 1 or target == 2:
        return 'Faz parte da sequência de Fibonacci'
    
    a, b = 0, 1
    
    while b < target:
        a, b = b, a+b
        if b == target:
            return 'Faz parte da sequência de Fibonacci'
    return 'Não faz parte da sequência de Fibonacci'

result = fibonacci(21) #Deve retornar que faz parte da sequência
print(result,"\n")



result2 = fibonacci(22) #Deve retornar que não faz parte da sequência
print(result2)

