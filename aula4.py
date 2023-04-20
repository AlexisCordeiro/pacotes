while True: # laço de repetição, TRUE enquanto for verdadeiro <>
    try:
        numero = int(input('Entre com um número: ')) 
        print(numero/2) # somente verifica que entrei com um número realmente.
        break # irá parar aqui se for int.
    except:
        print('O número que você entrou não é válido. Tente novamente.') # no caso se fosse string e float etc; somente int.