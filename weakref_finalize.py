import weakref

if __name__=='__main__':
    # Criando um objeto to tipo set
    s1 = {1,2,3}

    # Criando outra referencia ao mesmo objeto
    s2 = s1

    # callback
    def bye():
        print('...like tears in the rain.')

    # Weak Reference para s1 registrando o callback
    ender = weakref.finalize(s1,bye)

    # A referencia de s1 ainda permanece True
    print(f'ender.alive:{ender.alive}')
    
    # Deletando a primeira referencia
    del s1

    # A referencia de s1 ainda permanece True pois ainda existe s2 apontando para o objeto set
    print(f'ender.alive:{ender.alive}')

    # Atribuindo outro objeto a variavel s2, logo todas as referencias ao objeto set acabaram e o objeto será então destruido chamando o callback
    s2 = 'spam'

    # A referencia de s1 morreu False
    print(f'ender.alive:{ender.alive}')