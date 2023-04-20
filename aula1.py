try:
    value = int(input('Entre com um número: ')) # função TRY tenta execrutar o codigo, caso der algum erro, executa o EXCEPT
    print('O valor: ', value, 'dividido por um é: ', 1/value)
except:
    print('Erro. Verifique o valor fornecido.')