# DESAFIO [DIO](https://web.dio.me/users/giovanakr): Otimizando o Sistema Bancário
[Primeira versao](https://github.com/giovanakrsk/sistema-bancario/tree/main)

## OBJETIVO GERAL
Separar funções existentes de saque, depósito e extrato em funções. Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária (vincular com usuário).

## SAQUE
A função saque deve receber os argumentos apenas por nome (keyword only).

## DEPÓSITO
A função depósito deve receber os argumentos apenas por posição (positional only).

## EXTRATO
Deve receber os argumentos por posição e nome(positional only e keywork only)

## CRIAR USUÁRIO
O programa deve armazenar os usuários em uma lista.
um usuário é composto por: nome, data de nascimento, cpf e endereço.
O endereço é uma string com formato: logradouro, número, bairro, cidade/uf.
Deve ser armazenado somente os números do CPF e não podemos cadastrar dois usuários com o mesmo CPF.

## CRIAR CONTA
O programa deve armazenar contas em uma lista, uma conta é composta por: agência, número de conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta, mas uma conta pertence apenas a um usuário.





