def main():
  nome= ""
  opcao = 0
while True: #(enquanto for verdadeiro executa o codigo)
        print("\n MENU PRINCIPAL")
        print("1. cadastrar o produto")
        print("2. ver produto cadastrado")
        print("3.sair do sistema ")
        opcao= int(input("Escolha a opção: "))
        if opcao ==1:
            print ("Cadastrar o produto")
            nome= input("\nDigite seu produto: ")
            print("\n Dados cadastrados com sucesso!")

        elif opcao ==2: #elif(senão se)
            if nome == "":
                print("Nenhum dado cadastrado ainda!\n")
            else:
                print("Produto cadastrado\n")
                print(f"Nome:{nome}\n")

        elif opcao == 3:
            print("Encerrando o sistema...\n")
            break # sai do loop while, terminando o programa
        else: # else (senão)
            print("Opção invalida!Tente novamente")
        # verifica se este script está seno executado diretamente
if _name_ == "_main_":
 main()


