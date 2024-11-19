if __name__=='__main__':
    # Criando uma tupla
    t1 = (1,2,3)

    # Invocando o built-in sobre o objeto anterior não cria um novo objeto mas retorna a referencia para o mesmo objeto
    t2 = tuple(t1)
    print(f't2 is t1:{t2 is t1}')

    # Idem
    t3 = t1[:]
    print(f't3 is t1:{t3 is t1}')