import random
import sys
import pymysql
import os
import time

try:

# Função para verificar se o usuário continuara a usar o programa

    def continuar(operacao):
        continuar = input("Deseja fazer outra operação no programa? (Sim/Não): ")

        if continuar.lower() == "s" or continuar.lower() == "sim":
            os.system('cls')
            programa(operacao)
        else:
            print("\nPrograma finalizado. Obrigado por utilizar.")
            time.sleep(2)

# Função usada se tiver algum dado inserido incorretamente durante uma operação

    def voltarComeco(operacao):
        print("\n---------------------------------------------")
        print("Valor incorreto, se necessário leia o manual do programa para mais informações.\nIniciando nova operação...")
        print("---------------------------------------------")
        time.sleep(4)
        os.system('cls');
        programa(operacao)

# Função da opcao == 6 - Simulação completa (Não-oficial)

    def totalPrecoSimu(quantJogos,precoJogo):
        total = quantJogos * precoJogo
        premioBruto = total * 43.35 / 100
        
        print("Arrecadação total:",total,"\n")
        print("Prêmio Bruto:",premioBruto,"\n")
        print("---------------------------------------------\n")

        return(premioBruto)

# Função do programa em si

    def programa(operacao):
        finalizar = 0
        operacao += 1
        
        print("\n------- Operação",operacao,"-------\n")

        print("1 - Gerar números aleatórios;\n2 - Fazer a probabilidade de cair o mesmo sorteio;\n3 - Registro de jogos (Oficiais)\n4 - Registro de sorteios (Oficiais)\n5 - Verificação de jogos (Oficiais)\n6 - Simulação completa (Não-oficial)\n\n0 - Manual do Programa\n")
        opcao = input("Qual função deseja utilizar (Digite o número): ")
        opcao = opcao[0]
        opcao = int(opcao)

        # Se o número for inválido

        if (opcao > 6):
            voltarComeco(operacao);
        
        print("--------------------------\n")

    # 1 - Gerar números aleatórios (Todos os jogos)
    
        if (opcao == 1):
            print("1 - Sorteador Automático (Mega-Sena);\n2 - Sorteador Automático (Lotofácil);\n")
            sorteioEscolhido = int(input("Digite o número do sorteador a ser utilizado: "))

            print("--------------------------------------------")

            if sorteioEscolhido < 1 or sorteioEscolhido > 2:
                voltarComeco(operacao)

            quantJogos = input("Quantos jogos você vai fazer: ")
            quantJogos = quantJogos[:2]
            quantJogos = int(quantJogos)
            print("--------------------------------------------")

            if quantJogos <= 0:
                voltarComeco(operacao)
                
            quantNum = input("Quantos números vai marcar no(s) jogo(s): ")
            quantNum = quantNum[:2]
            quantNum = int(quantNum)
            print("--------------------------------------------")

            if sorteioEscolhido == 1:
                nomeJogo = "Mega-Sena"
                minimo = 6
                maximo = 15

                limiteMin = 1
                limiteMax = 61
            elif sorteioEscolhido == 2:
                nomeJogo = "LotoFácil"
                minimo = 15
                maximo = 20

                limiteMin = 1
                limiteMax = 26

            if quantNum < minimo or quantNum > maximo:
                print("\nQuantidade de números para",nomeJogo,"incorreta.\nO mínimo são",minimo,"números e o máximo são",maximo,"números.")
                voltarComeco(operacao)

            contador = quantJogos
            quantJogos = quantNum * quantJogos
            jogo = 1
            ListaNum = []

            for i in range(1,quantJogos,1):
                if contador == 0:
                    break
                
                num = random.randrange(limiteMin,limiteMax)

                if ListaNum == []:
                    ListaNum.append(num)

                while num in ListaNum:
                    num = random.randrange(limiteMin,limiteMax)
                                
                ListaNum.append(num)

                if len(ListaNum) == quantNum:
                    ordem = 1
                    print("Jogo",jogo,"\n")
                    ListaNum = sorted(ListaNum)
                    for j in range(len(ListaNum)):
                        print("Número",ordem,":",ListaNum[j])
                        ordem += 1
                    print("-----------------------")
                    jogo +=1
                    ListaNum = []
                    contador -= 1

            print("Boa sorte!!!")
            print("-----------------------")
            continuar(operacao)

    # 2 - Fazer a probabilidade de cair o mesmo sorteio
    
        if (opcao == 2):

            print("1 - Probabilidade (Mega-Sena)\n2 - Probabilidade (LotoFácil)\n")
            sorteioEscolhido = int(input("Digite o número do jogo a ser feita a probabilidade: "))

            print("-----------------------")

        # 1 - Probabilidade (Mega-Sena)
            
            if sorteioEscolhido == 1:
                num1Sorteado = int(input("Primeiro número sorteado:"))
                print("--------------------------------------------")
                if num1Sorteado < 1 or num1Sorteado > 60:
                    print("Número digitado incorreto, tente novamente.")
                    sys.exit()
                        
                num2Sorteado = int(input("Segundo número sorteado:"))
                print("--------------------------------------------")
                if num2Sorteado < 1 or num2Sorteado > 60 or num2Sorteado == num1Sorteado:
                    print("Número digitado incorreto ou já sorteado, tente novamente.")
                    sys.exit()
                        
                num3Sorteado = int(input("Terceiro número sorteado:"))
                print("--------------------------------------------")
                if num3Sorteado < 1 or num3Sorteado > 60 or num3Sorteado == num1Sorteado or num3Sorteado == num2Sorteado:
                    print("Número digitado incorreto, tente novamente.")
                    sys.exit()
                        
                num4Sorteado = int(input("Quarto número sorteado:"))
                print("--------------------------------------------")
                if num4Sorteado < 1 or num4Sorteado > 60 or num4Sorteado == num1Sorteado or num4Sorteado == num2Sorteado or num4Sorteado == num3Sorteado:
                    print("Número digitado incorreto, tente novamente.")
                    sys.exit()
                        
                num5Sorteado = int(input("Quinto número sorteado:"))
                print("--------------------------------------------")
                if num5Sorteado < 1 or num5Sorteado > 60 or num5Sorteado == num1Sorteado or num5Sorteado == num2Sorteado or num5Sorteado == num3Sorteado or num5Sorteado == num4Sorteado:
                    print("Número digitado incorreto, tente novamente.")
                    sys.exit()
                        
                num6Sorteado = int(input("Sexto número sorteado:"))
                print("--------------------------------------------")
                if num6Sorteado < 1 or num6Sorteado > 60 or num6Sorteado == num1Sorteado or num6Sorteado == num2Sorteado or num6Sorteado == num3Sorteado or num6Sorteado == num4Sorteado or num6Sorteado == num5Sorteado:
                    print("Número digitado incorreto, tente novamente.")
                    sys.exit()

                num1 = random.randrange(1,61)
                num2 = random.randrange(1,61)
                num3 = random.randrange(1,61)
                num4 = random.randrange(1,61)
                num5 = random.randrange(1,61)
                num6 = random.randrange(1,61)

                contador = 0

            # Verifica se o sorteio foi feito de novo diretamente
                    
                if num1 == num1Sorteado or num1 == num2Sorteado or num1 == num3Sorteado or num1 == num4Sorteado or num1 == num5Sorteado or num1 == num6Sorteado:
                    if num2 == num1Sorteado or num2 == num2Sorteado or num2 == num3Sorteado or num2 == num4Sorteado or num2 == num5Sorteado or num2 == num6Sorteado:
                        if num3 == num1Sorteado or num3 == num2Sorteado or num3 == num3Sorteado or num3 == num4Sorteado or num3 == num5Sorteado or num3 == num6Sorteado:
                            if num4 == num1Sorteado or num4 == num2Sorteado or num4 == num3Sorteado or num4 == num4Sorteado or num4 == num5Sorteado or num4 == num6Sorteado:
                                if num5 == num1Sorteado or num5 == num2Sorteado or num5 == num3Sorteado or num5 == num4Sorteado or num5 == num5Sorteado or num5 == num6Sorteado:
                                    if num6 == num1Sorteado or num6 == num2Sorteado or num6 == num3Sorteado or num6 == num4Sorteado or num6 == num5Sorteado or num6 == num6Sorteado:
                                        contador += 1
                                        print("-----------------------")
                                        print("Sorteado!!!")
                                        print("Foram necessários",contador,"sorteios para sair o mesmo resultado!")
                                        print(num1)
                                        print(num2)
                                        print(num3)
                                        print(num4)
                                        print(num5)
                                        print(num6)
                                        print("-----------------------")
                                        continuar(operacao)

            # Faz sorteios até sair o mesmo resultado e contabiliza
                    
                while num1 != num1Sorteado or num1 != num2Sorteado or num1 != num3Sorteado or num1 != num4Sorteado or num1 != num5Sorteado or num1 != num6Sorteado or num2 != num1Sorteado or num2 != num2Sorteado or num2 != num3Sorteado or num2 != num4Sorteado or num2 != num5Sorteado or num2 != num6Sorteado or num3 != num1Sorteado or num3 != num2Sorteado or num3 != num3Sorteado or num3 != num4Sorteado or num3 != num5Sorteado or num3 != num6Sorteado or num4 != num1Sorteado or num4 != num2Sorteado or num4 != num3Sorteado or num4 != num4Sorteado or num4 != num5Sorteado or num4 != num6Sorteado or num5 != num1Sorteado or num5 != num2Sorteado or num5 != num3Sorteado or num5 != num4Sorteado or num5 != num5Sorteado or num5 != num6Sorteado or num6 != num1Sorteado or num6 != num2Sorteado or num6 != num3Sorteado or num6 != num4Sorteado or num6 != num5Sorteado or num6 != num6Sorteado:
                    num1 = random.randrange(1,61)
                    num2 = random.randrange(1,61)
                    if num2 == num1:
                        while num2 == num1:
                            num2 = random.randrange(1,61)
                    num3 = random.randrange(1,61)
                    if num3 == num1 or num3 == num2:
                        while num3 == num1 or num3 == num2:
                            num3 = random.randrange(1,61)
                    num4 = random.randrange(1,61)
                    if num4 == num1 or num4 == num2 or num4 == num3:
                        while num4 == num1 or num4 == num2 or num4 == num3:
                            num4 = random.randrange(1,61)
                    num5 = random.randrange(1,61)
                    if num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
                        while num5 == num1 or num5 == num2 or num5 == num3 or num5 == num4:
                            num5 = random.randrange(1,61)
                    num6 = random.randrange(1,61)
                    if num6 == num1 or num6 == num2 or num6 == num3 or num6 == num4 or num6 == num5:
                        while num6 == num1 or num6 == num2 or num6 == num3 or num6 == num4 or num6 == num5:
                            num6 = random.randrange(1,61)
                                
                    contador += 1

                    if num1 == num1Sorteado or num1 == num2Sorteado or num1 == num3Sorteado or num1 == num4Sorteado or num1 == num5Sorteado or num1 == num6Sorteado:
                        if num2 == num1Sorteado or num2 == num2Sorteado or num2 == num3Sorteado or num2 == num4Sorteado or num2 == num5Sorteado or num2 == num6Sorteado:
                            if num3 == num1Sorteado or num3 == num2Sorteado or num3 == num3Sorteado or num3 == num4Sorteado or num3 == num5Sorteado or num3 == num6Sorteado:
                                if num4 == num1Sorteado or num4 == num2Sorteado or num4 == num3Sorteado or num4 == num4Sorteado or num4 == num5Sorteado or num4 == num6Sorteado:
                                    if num5 == num1Sorteado or num5 == num2Sorteado or num5 == num3Sorteado or num5 == num4Sorteado or num5 == num5Sorteado or num5 == num6Sorteado:
                                        if num6 == num1Sorteado or num6 == num2Sorteado or num6 == num3Sorteado or num6 == num4Sorteado or num6 == num5Sorteado or num6 == num6Sorteado:
                                            Lista = []
                                            Lista.extend((num1,num2,num3,num4,num5,num6))
                                            print("-----------------------")
                                            print("Sorteado!!!")
                                            print("Foram necessários",contador,"sorteios para sair o mesmo resultado!")
                                            print(Lista)
                                            print("-----------------------")
                                            continuar(operacao)
                                            break

        # 2 - Probabilidade (LotoFácil)

            if sorteioEscolhido == 2:
                ListaNumSorteado = []
                for i in range(15):
                    numSorteado = int(input("Número sorteado: "))

                    if numSorteado <= 0 or numSorteado > 25:
                        print("-----------------------")
                        print("Este número não existe na LotoFácil.")
                        voltarComeco(operacao)
                        
                    if ListaNumSorteado == []:   
                        ListaNumSorteado.append(numSorteado)
                        
                    if len(ListaNumSorteado) >= 2:  
                        for j in range(len(ListaNumSorteado)):
                            if numSorteado == ListaNumSorteado[j]:
                                print("-----------------------")
                                print("Número já digitado para o sorteio. Cuidado.")
                                voltarComeco(operacao)

                    ListaNumSorteado.append(numSorteado)

            # Faz sorteios até sair o mesmo resultado e contabiliza
                    
                sorteador = 0
                contador = 0
                    
                while sorteador == 0:
                    contador += 1
                    num = random.randrange(1,26)
                    ListaSorteador = []
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        while num in ListaSorteador:
                            num = random.randrange(1,26)
                    if num in ListaNumSorteado:
                        ListaSorteador.append(num)
                        sorteador = 1
                        print("Sorteado!!")
                        print("Foram necessários",contador,"sorteios para sair o mesmo resultado!")
                        ListaSorteador = sorted(ListaSorteador)
                        print(ListaSorteador)
                        print("-----------------------")
                        continuar(operacao)
                        break

    # 3 - Registro de jogos (Oficiais)

        if (opcao == 3):

        # Registra os jogos oficiais (todos os tipos)
            
            print("1 - Registrar jogo oficial (Mega-Sena)\n2 - Registrar jogo oficial (LotoFácil)\n")
            tipoJogo = input("Qual o jogo a ser registrado: ")
            tipoJogo = tipoJogo[:1]
            tipoJogo = int(tipoJogo)
            print("--------------------------------------------")

            if tipoJogo < 1 or tipoJogo > 2:
                voltarComeco(operacao)
            
            numConcurso = input("Número do concurso: ")
            numConcurso = numConcurso[:4]
            print("--------------------------------------------")

            if len(numConcurso) != 4:
                print("\nNúmero do concurso digitado de maneira incorreta, deve-se ter 4 números.\nEm caso de dúvida, leia o manual.")
                voltarComeco(operacao)

            numConcurso = int(numConcurso)
            
            codigoAposta = input("Código da aposta (Cod. Pagamento): ")
            codigoAposta = codigoAposta[:25]
            print("--------------------------------------------")

            if len(codigoAposta) != 25:
                print("\nCodigo da aposta digitado de maneira incorreta, deve-se ter 25 caracteres.\nEm caso de dúvida, leia o manual.")
                voltarComeco(operacao)

            diaAposta = input("Dia da aposta (XX/XX/XXXX): ")
            diaAposta = diaAposta[:10]
            print("--------------------------------------------")

            if len(diaAposta) != 10:
                print("\nData digitada de maneira incorreta, digite como está exemplificado.\nEm caso de dúvida, leia o manual.")
                voltarComeco(operacao)

            quantJogos = input("Quantos jogos foram feitos: ")
            quantJogos = quantJogos[:2]
            quantJogos = int(quantJogos)
            print("--------------------------------------------")

            if quantJogos <= 0:
                voltarComeco(operacao)

            quantNum = int(input("Quantos números foram marcados: "))
            print("--------------------------------------------")

            if tipoJogo == 1:
                nomeJogo = "Mega-Sena"
                maisNum = 15
                delNum = 15

                minimoMarca = 6

                ListaTeimo = [2,4,8]

                numJogoMin = 1
                numJogoMax = 60
            elif tipoJogo == 2:
                nomeJogo = "LotoFácil"
                maisNum = 20
                delNum = 20

                minimoMarca = 15

                ListaTeimo = [3,6,9,12]

                numJogoMin = 1
                numJogoMax = 25

            if quantNum < minimoMarca or quantNum > maisNum:
                print("\nQuantidade de números para",nomeJogo,"incorreta.\nO mínimo são",minimoMarca,"números e o máximo são",maisNum,"números.")
                voltarComeco(operacao)

            surpresinha = input("Você utilizou a surpresinha? Se sim, quantas apostas fez: ")
            surpresinha = surpresinha[:3]
            print("--------------------------------------------")

            try:
                surpresinha = int(surpresinha)
                
                if surpresinha < 1 or surpresinha > 7:
                    print("\nValor inserido na surpresinha da",nomeJogo,"está incorreto.\nVerifique os números no volante ou consulte no manual do programa.")
                    voltarComeco(operacao)
            except ValueError:
                if surpresinha.lower() != "não" and surpresinha.lower() != "nao" and surpresinha.lower() != "n":
                    print("\nValor da surpresinha da",nomeJogo,"incorreto.\nVerifique os números no volante ou consulte no manual do programa.")
                    voltarComeco(operacao)
            
            teimosinha = input("Você utilizou a teimosinha? Se sim, quantos concursos colocou: ")
            teimosinha = teimosinha[:3]
            print("--------------------------------------------")

            try:
                teimosinha = int(teimosinha)
                
                if teimosinha in ListaTeimo:
                    utilizaTeimo = teimosinha
                else:
                    print("\nValor inserido na teimosinha da",nomeJogo,"está incorreto.\nVerifique os números no volante ou consulte no manual do programa.")
                    voltarComeco(operacao)
            except ValueError:
                if teimosinha.lower() == "não" or teimosinha.lower() == "nao" or teimosinha.lower() == "n":
                    utilizaTeimo = 0
                else:
                    print("\nValor da teimosinha da",nomeJogo,"incorreto.\nVerifique os números no volante ou consulte no manual do programa.")
                    voltarComeco(operacao)

            print("\n-----------------------")
            print("Agora, coloque os números do seu jogo:")
            print("-----------------------")

        # Guarda os números a serem gravados
            
            ListaNumJogo = []
            ordem = 0
            contador = 1
            contadorJogos = quantJogos
            alteracao = 0
            comecoAdici = -maisNum
            finalAdici = 0
            while contador != 0:
                for i in range(0,contadorJogos,1):
                    ordem += 1
                    print("\n------- Jogo",ordem,"-------\n")
                    comecoAdici += maisNum
                    finalAdici += maisNum

                    if alteracao == 0:
                        for j in range(0,quantNum,1):
                            numJogo = int(input("Número marcado: "))

                            if numJogo < numJogoMin or numJogo > numJogoMax:
                                print("---------------------------------------------")
                                print("\nEste número não existe na",nomeJogo,". Tome cuidado e tente novamente.")
                                voltarComeco(operacao)
                            elif numJogo in ListaNumJogo[comecoAdici:finalAdici]:
                                print("---------------------------------------------")
                                print("\nNúmero já digitado neste jogo, tome cuidado e tente novamente.")
                                voltarComeco(operacao)

                            ListaNumJogo.append(numJogo)

                        maisNum = maisNum - quantNum
                        for k in range(0,maisNum,1):
                            ListaNumJogo.append(0)
                        maisNum = delNum
                    else:

                    # A alteração acontece aqui
                        comecoInsert = comeco

                        for l in range(0,quantNum,1):
                            numJogo = int(input("Número marcado: "))

                            if numJogo < numJogoMin or numJogo > numJogoMax:
                                print("---------------------------------------------")
                                print("\nEste número não existe na",nomeJogo,". Tome cuidado e tente novamente.")
                                voltarComeco(operacao)
                            elif numJogo in ListaNumJogo[comecoInsert:comeco]:
                                print("---------------------------------------------")
                                print("\nNúmero já digitado neste jogo, tome cuidado e tente novamente.")
                                voltarComeco(operacao)
                            
                            ListaNumJogo.insert(comeco,numJogo)
                            comeco += 1

            # Mostra os números para verificação e se necessário faz alteração do jogo
                comeco = 0
                ultimo = quantNum
                ordem = 1
                for i in range(quantJogos):
                    print("\nJogo",ordem,":",ListaNumJogo[comeco:ultimo],"\n")
                    ordem += 1
                    comeco += maisNum
                    ultimo += maisNum
                verifi = input("Todos os números estão corretos (Sim/Não): ")

                if verifi.lower() == "sim" or verifi.lower() == "s":
                    contador = 0
                else:
                    verifiFalso = int(input("Qual jogo deseja alterar (Número pela ordem cadastrada): "))
                    verifiFalso = verifiFalso - 1
                    
                    comeco = maisNum * verifiFalso
                    ultimo = comeco + quantNum
                    del(ListaNumJogo[comeco:ultimo])
                    
                    contadorJogos = 1
                    ordem = verifiFalso
                    alteracao = 1

            # Faz o conexão
            db = pymysql.connect(host="localhost", user="root", password="", db="Loteria")

            # Posiciona o cursor
            cursor = db.cursor()
                
            # Executa o comando no banco de dados
            cursor.execute("INSERT INTO MeusJogos (tipoJogo,numConcurso,codigoAposta,diaAposta,quantJogos,quantNum,surpresinha,teimosinha,utilizaTeimo) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (tipoJogo,numConcurso,codigoAposta,diaAposta,quantJogos,quantNum,surpresinha,teimosinha,utilizaTeimo))
            db.commit()
            
            cursor.execute("SELECT codigo FROM MeusJogos ORDER BY codigo DESC limit 1")
            codigo = cursor.fetchall()

            insert = "INSERT INTO "
            
            if tipoJogo == 1:
                tabela = "MegaSena "
                campos = "(codJogo,Num1,Num2,Num3,Num4,Num5,Num6,Num7,Num8,Num9,Num10,Num11,Num12,Num13,Num14,Num15) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                comando = insert + tabela + campos

            elif tipoJogo == 2:
                tabela = "LotoFacil "
                campos = "(codJogo,Num1,Num2,Num3,Num4,Num5,Num6,Num7,Num8,Num9,Num10,Num11,Num12,Num13,Num14,Num15,Num16,Num17,Num18,Num19,Num20) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                comando = insert + tabela + campos

            for j in range(quantJogos):
                i = 0
                if tipoJogo == 1:
                    valores = (codigo,ListaNumJogo[i],ListaNumJogo[i+1],ListaNumJogo[i+2],ListaNumJogo[i+3],ListaNumJogo[i+4],ListaNumJogo[i+5],ListaNumJogo[i+6],ListaNumJogo[i+7],ListaNumJogo[i+8],ListaNumJogo[i+9],ListaNumJogo[i+10],ListaNumJogo[i+11],ListaNumJogo[i+12],ListaNumJogo[i+13],ListaNumJogo[i+14])
                elif tipoJogo == 2:
                    valores = (codigo,ListaNumJogo[i],ListaNumJogo[i+1],ListaNumJogo[i+2],ListaNumJogo[i+3],ListaNumJogo[i+4],ListaNumJogo[i+5],ListaNumJogo[i+6],ListaNumJogo[i+7],ListaNumJogo[i+8],ListaNumJogo[i+9],ListaNumJogo[i+10],ListaNumJogo[i+11],ListaNumJogo[i+12],ListaNumJogo[i+13],ListaNumJogo[i+14],ListaNumJogo[i+15],ListaNumJogo[i+16],ListaNumJogo[i+17])
                cursor.execute(comando,valores)
                db.commit()
                for k in range(0,delNum,1):
                    del(ListaNumJogo[0])

            db.close()
            print("\nJogo cadastrado com sucesso!!")
            print("-----------------------")
            continuar(operacao)

    # 4 - Registro de Sorteios (Oficiais)
        
        if (opcao == 4):

        # Registra os sorteios oficiais (todos os tipos)
            
            print("1 - Sorteio Oficial (Mega-Sena)\n2 - Sorteio Oficial (LotoFácil)\n")
            tipoJogo = input("Digite o número do tipo de jogo a ser registrado o sorteio: ")
            tipoJogo = tipoJogo[0:1]
            tipoJogo = int(tipoJogo)
            print("--------------------------------------------")

            if tipoJogo == 1:
                quantNum = 6
                
                numSorteadoMin = 1
                numSorteadoMax = 60
                
                nomeJogo = "Mega-Sena"
            elif tipoJogo == 2:
                quantNum = 15
                
                numSorteadoMin = 1
                numSorteadoMax = 25
                
                nomeJogo = "LotoFácil"
            else:
                voltarComeco(operacao)

            concurso = input("Digite o número do concurso: ")
            concurso = concurso[:4]
            print("--------------------------------------------")

            if len(concurso) != 4:
                print("\nNúmero do concurso incorreto, deve-se ter 4 números.\nEm caso de dúvida, leia o manual.")
                voltarComeco(operacao)
            
            concurso = int(concurso)

            dataSorteio = input("Digite a data em que ocorreu o sorteio (XX/XX/XXXX): ")
            dataSorteio = dataSorteio[:10]
            print("--------------------------------------------")

            if len(dataSorteio) != 10:
                print("\nData digitada de maneira incorreta, digite como está exemplificado.\nEm caso de dúvida, leia o manual.")
                voltarComeco(operacao)

            print("\n-----------------------")
            print("Agora, coloque os números do sorteio:")
            print("-----------------------")

        # Guarda os números a serem gravados
            
            contador = 1
            while contador != 0:
                ListaNumSorteio = []
                print("\n------- Sorteio",nomeJogo,"/ Concurso:",concurso,"-------\n")

                for j in range(0,quantNum,1):
                    numSorteado = int(input("Número sorteado: "))

                    if numSorteado < numSorteadoMin or numSorteado > numSorteadoMax:
                        print("---------------------------------------------")
                        print("\nEste número não existe na",nomeJogo,". Tome cuidado e tente novamente.")
                        voltarComeco(operacao)
                    elif numSorteado in ListaNumSorteio:
                        print("---------------------------------------------")
                        print("\nNúmero já digitado neste sorteio, tome cuidado e tente novamente.")
                        voltarComeco(operacao)
                    
                    ListaNumSorteio.append(numSorteado)

            # Mostra os números para verificação e se necessário faz alteração
            
                print("\n------- Sorteio",nomeJogo,"/ Concurso:",concurso,"-------\n")
                print("Números sorteados:",ListaNumSorteio)
    
                verifi = input("\nTodos os números estão corretos (Sim/Não): ")

                if verifi.lower() == "sim" or verifi.lower() == "s":
                    contador = 0
                elif verifi.lower() == "não" or verifi.lower() == "nao" or verifi.lower() == "n":
                    del(ListaNumSorteio)
                else:
                    voltarComeco(operacao)

            # Faz o conexão
            db = pymysql.connect(host="localhost", user="root", password="", db="Loteria")

            # Posiciona o cursor
            cursor = db.cursor()

            # Insere os dados no banco
            if tipoJogo == 1:
                for i in range(0,1,1):
                    i = 0
                    cursor.execute("INSERT INTO SorteiosOficialMegaSena (tipoJogo,concurso,dataSorteio,Num1,Num2,Num3,Num4,Num5,Num6) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (tipoJogo,concurso,dataSorteio,ListaNumSorteio[i],ListaNumSorteio[i+1],ListaNumSorteio[i+2],ListaNumSorteio[i+3],ListaNumSorteio[i+4],ListaNumSorteio[i+5]))
                    db.commit()

            if tipoJogo == 2:
                for i in range(0,1,1):
                    i = 0
                    cursor.execute("INSERT INTO SorteiosOficialLotoFacil (tipoJogo,concurso,dataSorteio,Num1,Num2,Num3,Num4,Num5,Num6,Num7,Num8,Num9,Num10,Num11,Num12,Num13,Num14,Num15) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (tipoJogo,concurso,dataSorteio,ListaNumSorteio[i],ListaNumSorteio[i+1],ListaNumSorteio[i+2],ListaNumSorteio[i+3],ListaNumSorteio[i+4],ListaNumSorteio[i+5],ListaNumSorteio[i+6],ListaNumSorteio[i+7],ListaNumSorteio[i+8],ListaNumSorteio[i+9],ListaNumSorteio[i+10],ListaNumSorteio[i+11],ListaNumSorteio[i+12],ListaNumSorteio[i+13],ListaNumSorteio[i+14]))
                    db.commit()

            # Fecha a conexão com o banco
            db.close()

            print("\nSorteio cadastrado com sucesso!!")
            print("--------------------------------------------")
            continuar(operacao)

    # 5 - Verificação de jogos (Oficiais)

        if (opcao == 5):
            print("1 - Verificar jogo(s) (Mega-Sena)\n2 - Verificar jogo(s) (LotoFácil)\n")
            tipoJogo = input("Digite o número de qual jogo será verificado: ")
            tipoJogo = tipoJogo[:1]
            tipoJogo = int(tipoJogo)
            print("--------------------------------------------")

            if tipoJogo < 1 or tipoJogo > 2:
                voltarComeco(operacao)

            concurso = input("Digite o número do concurso que será verificado: ")
            concurso = concurso[:4]
            print("------------------------------------------------------")

            if len(concurso) != 4:
                print("\nNúmero do concurso incorreto, deve-se ter 4 números.\nEm caso de dúvida, leia o manual.")
                voltarComeco(operacao)
            
            concurso = int(concurso)
            
            # Faz o conexão
            db = pymysql.connect(host="localhost", user="root", password="", db="Loteria")

            # Posiciona o cursor
            cursor = db.cursor()

            cursor.execute("SELECT codigo FROM MeusJogos WHERE numConcurso = (%s) AND tipoJogo = (%s)", (concurso,tipoJogo))
            resultado = cursor.fetchall()
            numrows = int(cursor.rowcount)

            if resultado == ():
                print("\n[X] Você não possui nenhum jogo cadastrado com o concurso",concurso,". [X]\n")
                print("------------------------------------------------------")
                voltarComeco(operacao)

            if tipoJogo == 1:
                cursor.execute("SELECT * FROM SorteiosOficialMegaSena WHERE concurso = (%s)", (concurso))
                resultadoSorteio = cursor.fetchall()
                numrowsSorteio = int(cursor.rowcount)
                tamanhoListaSorteio = 6
                nomeJogo = "Mega-Sena"
                tabela = "MegaSena "
            elif tipoJogo == 2:
                cursor.execute("SELECT * FROM SorteiosOficialLotoFacil WHERE concurso = (%s)", (concurso))
                resultadoSorteio = cursor.fetchall()
                numrowsSorteio = int(cursor.rowcount)
                tamanhoListaSorteio = 15
                nomeJogo = "LotoFácil"
                tabela = "LotoFacil "

            if resultadoSorteio == ():
                print("\n[X] O sorteio do concurso",concurso,"não está cadastrado no banco. [X]\n")
                print("------------------------------------------------------")
                voltarComeco(operacao)
            else:
                contador = 4
                ListaSorteio = []
                for i in range(0,tamanhoListaSorteio,1):
                    for j in resultadoSorteio:
                        ListaSorteio.append(j[contador])
                        contador += 1

            contador = 0
            ListaCodJogos = []
            for j in resultado:
                ListaCodJogos.append(j[contador])

            ListaCodMeuJogo = []
            contador = 0

            if tipoJogo == 1:
                select = "SELECT codigo FROM "
                where = "WHERE codJogo = (%s)"
                comando = select + tabela + where

                maximoNum = 15

                selectNums = "SELECT Num1,Num2,Num3,Num4,Num5,Num6,Num7,Num8,Num9,Num10,Num11,Num12,Num13,Num14,Num15 FROM "
                whereNums = "MegaSena WHERE codigo = (%s)"
                comandoNums = selectNums + tabela + whereNums

            elif tipoJogo == 2:
                select = "SELECT codigo FROM "
                where = "WHERE codJogo = (%s)"
                comando = select + tabela + where

                maximoNum = 20

                selectNums = "SELECT Num1,Num2,Num3,Num4,Num5,Num6,Num7,Num8,Num9,Num10,Num11,Num12,Num13,Num14,Num15,Num16,Num17,Num18,Num19,Num20 FROM "
                whereNums = "WHERE codigo = (%s)"
                comandoNums = selectNums + tabela + whereNums

            for i in range(0,len(ListaCodJogos),1):
                    cursor.execute(comando,(ListaCodJogos[i]))
                    resultadoCodMeuJogo = cursor.fetchall()
                    for k in resultadoCodMeuJogo:
                        ListaCodMeuJogo.append(k[contador])
            print("\nCódigo do(s) jogo(s):",ListaCodMeuJogo)

            ListaNumJogos = []
            for i in range(0,len(ListaCodMeuJogo),1):
                contadorNumJogos = -1
                cursor.execute(comandoNums,ListaCodMeuJogo[i])
                resultadoNumJogos = cursor.fetchall()
                for j in range(0,maximoNum,1):
                    contadorNumJogos += 1
                    for k in resultadoNumJogos:
                        ListaNumJogos.append(k[contadorNumJogos])

            print("\n------- Jogo(s) da",nomeJogo,"/ Concurso:",concurso,"-------\n")
            for i in range(0,len(ListaCodMeuJogo),1):
                List = []
                contador = 0
                for j in range(0,maximoNum,1):
                    List.append(ListaNumJogos[j])
                for k in range(0,maximoNum,1):
                    if List[k] != 0:
                        if List[k] in ListaSorteio:
                            contador += 1
                    del(ListaNumJogos[0])

                print("--------------------------------------------")
                print("Jogo do codigo",ListaCodMeuJogo[i],"teve:",contador,"acertos!")
            print("--------------------------------------------\n")

            contador = 1
            while contador != 0:
                analiseJogo = input("Deseja ver detalhes sobre alguns dos jogos acima? (Sim/Não): ")
                
                if analiseJogo.lower() == "s" or analiseJogo.lower() == "sim":
                    print("\n",ListaCodMeuJogo,"\n")
                    cod = int(input("Qual dos jogos você deseja ver: "))

                    select = "SELECT codJogo FROM "
                    where = "WHERE codigo = (%s)"
                    comando = select + tabela + where

                    cursor.execute(comando,(cod))
                    result = cursor.fetchall()

                    cursor.execute("SELECT * FROM MeusJogos WHERE codigo = (%s)", (result))
                    result = cursor.fetchall()

                    for i in result:
                        print ("\n------------------------------------------------------------------")
                        print ("|   Jogo     Concurso         Código            Data da Aposta   |")
                        print ("------------------------------------------------------------------")
                        print (" ",nomeJogo," ",i[2]," ",i[3]," ",i[4])
                        print ("------------------------------------------------------------------\n")

                elif analiseJogo.lower() == "n" or analiseJogo.lower() == "nao" or analiseJogo.lower() == "não":
                    contador = 0
                    print("-----------------------")
                else:
                    voltarComeco(operacao)

            continuar(operacao)
            
    # 6 - Simulação completa (Não-oficial)

        if (opcao == 6):
            print("1 - Simulação (Mega-Sena)\n2 - Simulação (LotoFácil)\n")
            tipoJogo = input("Digite o número de qual jogo será feito a simulação: ")
            tipoJogo = tipoJogo[:1]
            tipoJogo = int(tipoJogo)
            print("---------------------------------------------")

            if tipoJogo < 1 or tipoJogo > 2:
                voltarComeco(operacao)

            quantJogos = int(input("Quantos jogos deseja usar na simulação: "))
            print("---------------------------------------------")

            quantNumJogos = input("Digite quantos números deseja que tenham marcados nos jogos: ")
            quantNumJogos = quantNumJogos[:2]
            quantNumJogos = int(quantNumJogos)
            print("---------------------------------------------")

            if tipoJogo == 1:
                nomeJogo = "Mega-Sena"
                numMarcMin = 6
                numMarcMax = 15
                sorteio = 6
                minimo = 1
                maximo = 61
                ListaSena = []
                ListaQuina = []
                ListaQuadra = []
                contadorSena = 0
                contadorQuina = 0
                contadorQuadra = 0
            elif tipoJogo == 2:
                nomeJogo = "LotoFácil"
                numMarcMin = 15
                numMarcMax = 20
                sorteio = 15
                minimo = 1
                maximo = 26
                ListaQuinze = []
                ListaQuatorze = []
                ListaTreze = []
                ListaDoze = []
                ListaOnze = []
                contadorQuinze = 0
                contadorQuatorze = 0
                contadorTreze = 0
                contadorDoze = 0
                contadorOnze = 0

            if quantNumJogos < numMarcMin or quantNumJogos > numMarcMax:
                print("\nQuantidade de números para",nomeJogo,"incorreta.\nO mínimo são",numMarcMin,"números e o máximo são",numMarcMax,"números.")
                voltarComeco(operacao)

            ListaJogosCompleta = []
            for i in range(0,quantJogos,1):
                ListaJogosBase = []
                for j in range(0,quantNumJogos,1):
                    num = random.randrange(minimo,maximo)
                    while num in ListaJogosBase:
                        num = random.randrange(minimo,maximo)
                    ListaJogosBase.append(num)
                ListaJogosCompleta += sorted(ListaJogosBase)

            ListaSorteio = []
            for i in range(0,sorteio,1):
                num = random.randrange(minimo,maximo)
                while num in ListaSorteio:
                    num = random.randrange(minimo,maximo)
                ListaSorteio.append(num)
            ListaSorteio = sorted(ListaSorteio)

            print("\nSorteio:",ListaSorteio,"\n")
            for i in range(0,quantJogos,1):
                contador = 0
                j = 0
                for j in range(0,quantNumJogos,1):
                    if ListaJogosCompleta[j] in ListaSorteio:
                        contador += 1
                if tipoJogo == 1:
                    if contador == 4:
                        ListaQuadra += ListaJogosCompleta[:quantNumJogos]
                        contadorQuadra += 1
                    elif contador == 5:
                        ListaQuina += ListaJogosCompleta[:quantNumJogos]
                        contadorQuina += 1
                    elif contador == 6:
                        ListaSena += ListaJogosCompleta[:quantNumJogos]
                        contadorSena += 1
                elif tipoJogo == 2:
                    if contador == 11:
                        ListaOnze += ListaJogosCompleta[:quantNumJogos]
                        contadorOnze += 1
                    elif contador == 12:
                        ListaDoze += ListaJogosCompleta[:quantNumJogos]
                        contadorDoze += 1
                    elif contador == 13:
                        ListaTreze += ListaJogosCompleta[:quantNumJogos]
                        contadorTreze += 1
                    elif contador == 14:
                        ListaQuatorze += ListaJogosCompleta[:quantNumJogos]
                        contadorQuatorze += 1
                    elif contador == 15:
                        ListaQuinze += ListaJogosCompleta[:quantNumJogos]
                        contadorQuinze += 1 
                del(ListaJogosCompleta[:quantNumJogos])

            if tipoJogo == 1:

                if quantNumJogos == 6:
                    precoJogo = 4.50
                elif quantNumJogos == 7:
                    precoJogo = 31.50
                elif quantNumJogos == 8:
                    precoJogo = 126.0
                elif quantNumJogos == 9:
                    precoJogo = 378.0
                elif quantNumJogos == 10:
                    precoJogo = 945.0
                elif quantNumJogos == 11:
                    precoJogo = 2079.0
                elif quantNumJogos == 12:
                    precoJogo = 4158.0
                elif quantNumJogos == 13:
                    precoJogo = 7722.0
                elif quantNumJogos == 14:
                    precoJogo = 13513.50
                elif quantNumJogos == 15:
                    precoJogo = 22522.50

                premioBruto = totalPrecoSimu(quantJogos,precoJogo)
                
                print("Ganhadores com Sena:",contadorSena,"\n")
                print("Ganhadores com Quina:",contadorQuina,"\n")
                print("Ganhadores com Quadra:",contadorQuadra,"\n")

                print("---------------------------------------------")

                acertadorSena = premioBruto * 35 / 100
                acertadorQuina = premioBruto * 19 / 100
                acertadorQuadra = round(premioBruto * 19 / 100)

                if contadorSena == 0:
                    print("Sena - Não houve acertadores\n")
                else:
                    acertadorSena = acertadorSena / contadorSena
                    print("Sena -",contadorSena,f"apostas ganharam R$ {acertadorSena:.2f} !\n")

                if contadorQuina == 0:
                    print("Quina - Não houve acertadores\n")
                else:
                    acertadorQuina = acertadorQuina / contadorQuina
                    print("Quina -",contadorQuina,f"apostas ganharam R$ {acertadorQuina:.2f} !\n")

                if contadorQuadra == 0:
                    print("Quadra - Não houve acertadores\n")
                else:
                    acertadorQuadra = acertadorQuadra / contadorQuadra
                    print("Quadra -",contadorQuadra,f"apostas ganharam R$ {acertadorQuadra:.2f} !\n")

            elif tipoJogo == 2:

                if quantNumJogos == 15:
                    precoJogo = 2.50
                elif quantNumJogos == 16:
                    precoJogo = 40.0
                elif quantNumJogos == 17:
                    precoJogo = 340.0
                elif quantNumJogos == 18:
                    precoJogo = 2040.0
                elif quantNumJogos == 19:
                    precoJogo = 9690.0
                elif quantNumJogos == 20:
                    precoJogo = 38760.0

                premioBruto = totalPrecoSimu(quantJogos,precoJogo)
                
                print("Ganhadores com Quinze acertos:",contadorQuinze,"\n")
                print("Ganhadores com Quatorze acertos:",contadorQuatorze,"\n")
                print("Ganhadores com Treze acertos:",contadorTreze,"\n")
                print("Ganhadores com Doze acertos:",contadorDoze,"\n")
                print("Ganhadores com Onze acertos:",contadorOnze,"\n")

                print("---------------------------------------------")
                
                premioBruto = premioBruto - ((contadorOnze * 4) + (contadorDoze * 8) + (contadorTreze * 20))
                acertadorQuinze = premioBruto * 65 / 100
                acertadorQuatorze = premioBruto * 20 / 100
                
                if contadorQuinze == 0:
                    print("15 acertos - Não houve acertadores\n")
                else:
                    acertadorQuinze = acertadorQuinze / contadorQuinze
                    print("15 acertos -",contadorQuinze,f"apostas ganharam R$ {acertadorQuinze:.2f} !\n")

                if contadorQuatorze == 0:
                    print("14 acertos - Não houve acertadores\n")
                else:
                    acertadorQuatorze = acertadorQuatorze / contadorQuatorze
                    print("14 acertos -",contadorQuatorze,f"apostas ganharam R$ {acertadorQuatorze:.2f} !\n")

                if contadorTreze == 0:
                    print("13 acertos - Não houve acertadores\n")
                else:
                    print("13 acertos -",contadorTreze,"apostas ganharam R$ 20,00 !\n")

                if contadorDoze == 0:
                    print("12 acertos - Não houve acertadores\n")
                else:
                    print("12 acertos -",contadorDoze,"apostas ganharam R$ 8,00 !\n")

                if contadorOnze == 0:
                    print("11 acertos - Não houve acertadores\n")
                else:
                    print("11 acertos -",contadorOnze,"apostas ganharam R$ 4,00 !\n")

            print("---------------------------------------------\n")
            print("Simulação concluida com sucesso!!\n")
            continuar(operacao)

        # Manual do Programa
            
        if (opcao == 0):
            print("-----------------------")
            print("| Manual do Programa |")
            print("-----------------------\n")
            print("Programa desenvolvido por: Gustavo Cesar.\nGitHub: https://github.com/GustavoSouza13\nData da última atualização: 18/07/2019 --> 20/10/2020.\n")
            print("[X] 1 - O que é? [X]\n")
            print("Este programa foi feito para facilitar a vida dos apostadores da loteria. Aqui é possível:\n- Gerar números para seus jogos;\n- Fazer a probabilidade de quantos jogos seriam necessário para cair o mesmo sorteio;\n- Registrar seus jogos;\n- Registrar os sorteios;\n- Fazer a verificação de seus jogos automaticamente;\n- Fazer uma simulação como se estivesse ocorrendo um sorteio.\n")
            print("[X] 2 - Como funciona? [X]\n")
            print("O programa foi desenvolvido para ser o mais claro e objetivo possível, somente\né necessário a atenção no momento de preencher todos os campos, pois em algumas\nsituações pode acabar ocorrendo um erro e será necessário fechar o programa.\nTome Cuidado!\n")
            print("Informações adicionais:\n[] Este programa foi desenvolvido para atendender os tipos de jogos da\n'Mega-Sena' e 'Loto-Fácil'.\n\n[] No momento do uso será perceptível que não há limite para escrever em uma\noperação, mas o programa possui um sistema que pega somente os primerios\ncaracteres digitados de seu interesse, a quantidade que será utilizada dependerá\ndo que você estiver fazendo no programa, exemplo:\n\nDigite o número do concurso: 123456\n\nNote: Só serão lidos os números '1234', pois neste programa só possui os jogos\nda 'Mega-Sena' e da 'LotoFácil'. Isto se aplica a qualquer outro campo do\nprograma, e será utilizado o número de caracteres necessário para a ação.\n\n[] Ao final de cada operação você poderá iniciar uma nova operação se responder\n'Sim' ou finalizar o programa se responder 'Não'.\n")
            print("--- OPERAÇÕES DO PROGRAMA ---\n")
            print("[X] 1 - Gerar números aleatórios [X]\n")
            print("Nesta operação é possivel gerar números aleatórios para seus jogos, sendo somente necessário informar:\n- O tipo de jogo que irá fazer;\n- A quantidade de jogos que irá fazer;\n- Quantos números irá marcar nos jogos.\n")
            print("[X] 2 - Fazer a probabilidade de cair o mesmo sorteio [X]\n")
            print("Nesta operação é informado a quantidade de números sorteados, dependendo do tipo de sorteio escolhido, logo serão\nfeitos N sorteios até que o resultado seja igual ao informado anteriormente. No final mostra a quantidade N de sorteios realizados.\n")
            print("[X] 3 - Registro de jogos (Oficiais) [X]\n")
            print("Aqui são armazenados os jogos realizados pelo usuário na vida real. São cadastrados aqui para futuramente serem\nfeitas verificações tanto sobre os próprios jogos quanto a eles relacinados a um determinado sorteio.\n")
            print("[X] 4 - Registro de sorteios (Oficiais) [X]\n")
            print("Aqui são registrados os sorteios realizados na vida real.\n")
            print("[X] 5 - Verificação de jogos (Oficiais) [X]\n")
            print("Aqui é onde será feita a verificação dos 'Sorteios Oficiais' em relação aos 'Jogos Oficiais' e mostrará todas\nas informações (conclusões) finais.\n")
            print("[X] 6 - Simulação completa (Não-oficial) [X]\n")
            print("Nesta operação é realizado um sorteio completo que incluirá:\n- O sorteio de qual jogo será realizado;\n- A quantidade de jogos que serão feitos para o sorteio;\n- A quantidade de números marcados em cada jogo.\nAo final das verificações é exibido todos os valores e a quantidade de jogos premiados.\n")
            continuar(operacao)
        
# Chama a função 'programa()' pela primeira vez

    operacao = 0
    programa(operacao)

except:
    print("-----------------------")
    print("Valor incorreto, fique atento ao deixar campos vazios e ao inserir valores. Reinicie o programa.")
    time.sleep(4)
