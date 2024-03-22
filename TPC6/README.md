# TPC6

**Título:** Gramática independente de contexto 
**Autor:** Martim Quintelas Pinto Félix, A100647

## Resumo

Este documento apresenta o desenvolvimento de uma gramática independente de contexto para uma linguagem de programação que permite efetuar operações aritméticas simples e atribuições. O objetivo principal é assegurar que a gramática definida seja do tipo LL(1), respeitando a precedência dos operadores e facilitando o cálculo dos conjuntos Look Ahead para cada regra de produção.


Exemplo da linguagem:

    ?a
    b=a*2/(27-3)
    !a+b
    c=a*b/(a/b)

Ter em conta:

Aspectos chave a considerar incluem a prioridade entre os operadores e a confirmação de que a gramática é de fato LL(1), além da derivação dos conjuntos Look Ahead pertinentes a todas as regras de produção.

## Resolução

A gramática é composta pelos seguintes elementos:

    T =  {'?', '!', '=', '+', '-', '*', '/', '(', ')', id, num}

    N= {S, Exp1, Exp2, Exp3, Op1, Op2}

    S = S

    P = {
    
        S -> '?' id             LA = {'?'}
        | '!' Exp1              LA = {'!'}
        | id '=' Exp1           LA = {id}

        Exp1 -> Exp2 Op1        LA = {'(', num, id}

        Op1 -> '+' Exp1         LA = {'+'}
            | '-' Exp1          LA = {'-'}
            | &                 LA = {')', $}

        Exp2 -> Exp3 Op2        LA = {'(', num, id}

        Op2 -> '*' Exp1         LA = {'*'}
            | '/' Exp1          LA = {'/'}
            | &                 LA = {'+', '-', ')', $}

        Exp3 -> '(' Exp1 ')'    LA = {'('}
            | num               LA = {num}
            | id                LA = {id}

    }