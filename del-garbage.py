if __name__=='__main__':
    # Criando um objeto do tipo lista e atribuindo sua referencia a variavel a
    a = [1,2]

    # Criando outro alias para o objeto lista
    b = a

    # Id do objeto
    print(f'ID: {id(a)}')

    # Deletando a referencia de a para a lista
    del a

    # O objeto lista ainda está vivo
    print(f'b:{b}')

    # Id do objeto continua o mesmo
    print(f'ID: {id(b)}')

    # reatribuindo outro objeto ao alias b, logo a lista anterior foi destruida
    b = [3]

    # Id do objeto mudou
    print(f'ID: {id(b)}')