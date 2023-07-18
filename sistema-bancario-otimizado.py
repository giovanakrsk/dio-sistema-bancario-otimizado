import textwrap

def menu():
    menu = """======== MENU ========

    [1] DEPÓSITO
    [2] SAQUE
    [3] EXTRATO
    [4] NOVA USUÁRIO
    [5] NOVA CONTA
    [6] LISTAR CONTAS
    [0] SAIR 

    QUAL AÇÃO DESEJA REALIZAR?
    """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
            saldo += valor
            extrato += f"DEPÓSITO: R$ {valor:.2f}\n"
            print("\nDepósito realizado com sucesso!")

    else:
        print("Valor inválido.")

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = numero_saques >= limite_saques

    if saldo_excedido:
        print("SALDO INSUFICIENTE.")

    elif limite_excedido:
        print("LIMITE DO VALOR DO SAQUE EXCEDIDO.")

    elif saque_excedido:
        print("LIMITE DE SAQUES EXCEDIDO.")

    elif valor > 0:
        saldo -= valor
        extrato += f'SAQUE: R$ {valor:.2f}\n'
        numero_saques += 1

    else:
        print("Valor inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n======= EXTRATO =======")
    print("Não foi indetificado movimentações" if not extrato else extrato)
    print(f"\nSALDO: R$ {saldo:.2f}")
    print("=======================\n")

def novo_usuario(usuarios):
    cpf = input("Informe CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("JÁ EXISTE USUÁRIO COM O CPF INFORMADO.")
        return
    nome = input("Nome completo do usuário: ")
    data_nasc = input("Data de nascimento (DD/MM/AAAA):")
    endereco = input("Endereço (logradouro, número - bairro - cidade/uf): ")

    usuarios.append({"nome": nome, "data_nasc": data_nasc, "cpf": cpf, "endereco": endereco})
    
    print("USUÁRIO CRIADO COM SUCESSO!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def nova_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe CPD do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("CONTA CRIADA COM SUCESSO!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("USUÁRIO NÃO ENCONTRADO.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            AGÊNCIA:{conta['agencia']}
            C/C:{conta['numero_conta']}
            TITULAR:{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    while True:
        opcao = menu
    
        if opcao == "1":
            valor = float(input("VALOR DO DEPÓSITO: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("VALOR DO SAQUE: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            novo_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = nova_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao =="6":
            listar_contas(contas)

        elif opcao == "0":
            break

    else:
        print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE.")