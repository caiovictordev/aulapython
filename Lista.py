# Sistema Bancário
import time

limite_saque_diario = 500
valor_total_depositado = 0
qnt_saque_diario = 0
qntd_depositos = 0
valor_na_conta = 0


def deposito():
    global valor_total_depositado, valor_na_conta, qntd_depositos
    valor_depositado = float(input("Qual valor desejas depositar? "))
    if valor_depositado <= 0:
        print("Erro, você não pode depositar um valor negativo.")
        return

    valor_total_depositado += valor_depositado
    valor_na_conta += valor_depositado
    qntd_depositos += 1
    print(f'O valor de R$ {valor_depositado:.2f}, foi depositado com sucesso!')
    print('')


def saque():
    global limite_saque_diario, qnt_saque_diario, valor_na_conta
    valor_sacado = float(input("Qual valor desejas sacar? "))

    if qnt_saque_diario >= 3:
        print("Você atingiu seu limite de saques diários.")
        return
    if valor_sacado > limite_saque_diario:
        print(f"Seu valor limite diário é de somente {limite_saque_diario}")
        return
    if valor_sacado > valor_na_conta:
        print("Erro, você não pode sacar um valor que não possue em conta.")
        return
    else:
        print(f"A quantia de R$ {valor_sacado:.2f} foi sacada com sucesso!")

    valor_na_conta -= valor_sacado
    qnt_saque_diario += 1
    print("")


def extrato():
    global valor_na_conta, qntd_depositos, valor_total_depositado, qnt_saque_diario
    if valor_na_conta == 0 and qntd_depositos == 0 and qnt_saque_diario == 0:
        print("Não foram realizados depósitos ou saques.")
        print("")
        return

    print("=== Extrato ===")
    print(f"Valor total depositado: R$ {valor_total_depositado:.2f}")
    print(f"Quantidade de depositos feitos: {qntd_depositos}")
    print(f"Quantidade de saques feitos: {qnt_saque_diario}")
    print("")
    print("-------------------------------------------")
    print(f'R$ {valor_na_conta:.2f}')
    print('')


def main():
    while True:
        print("=== Bem-vindo ao sistema bancário ===")
        print("Seleciosepósito.')
        print('2 - Saque.')
        print('3 - Extrato.')
        print('4 - Sair.')
        opcao = int(input('Qual opção deseja acessar: '))
        print("")
        if opcao < 1 or opcao > 4:
            print("Opção inválida!")
            continue
        elif opcao == 1:
            deposito()
        elif opcao == 2:
            saque()
        elif opcao == 3:
            extrato()
        elif opcao == 4:
            print('Saindo da sua conta...')
            break
        else:
            print("Opção inválida")
            time.sleep(5)
            return

if __name__ == "__main__":
    main()

