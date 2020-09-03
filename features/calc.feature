# language: pt
Funcionalidade: testar a calculadora com os operadores basicos 

    Contexto: 
        Dado que o valor mostrado seja 0

    Esquema do Cenario: Testar a soma
        Dado que o primeiro valor seja <primeiro>
        E o segundo valor seja <segundo>
        Quando executar a operação "somar"
        Entao o resultado da operação deve ser <resultado>

    Exemplos:
        | primeiro | segundo | resultado |
        | 1        | 3       | 4         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        | 1        | 5       | 6         |
        