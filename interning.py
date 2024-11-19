if __name__=='__main__':
    # Criando 2 variaveis tuplas com conteudo identico
    t1 = (1,2,3)
    t3 = (1,2,3)

    # Por questão de otimização do interpretador do python por serem objetos imutaveis as duas variaveis fazem referencia ao mesmo objeto
    # tecnica chamada de "interning"
    print(f't3 is t1:{t3 is t1}')

    # Idem. para string
    s1 = 'abc'
    s2 = 'abc'
    print(f's2 is s1:{s2 is s1}')

    # Obs: Essa é uma tecnica de otimização para o python e os criterios para fazerem varias alias refenciarem o mesmo objeto pode variar
    # dessa forma nunca levar essa tecnica em consideração para comparação de objetos sempre usar o operador == no lugar do is para comparar igualdade
    # entre objetos imutaveis.