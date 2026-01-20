print("\nBem vindo ao nosso sistema de controle e gestão de finanças!\n")

print("\nVamos começar com algumas perguntas simples para entender melhor sua situação financeira.\n")

# Coletando dados do usuário

print("Para uma análise mais detalhada, precisamos saber como esta a sua vida financeira atualmente. \n")

renda_mes = -1
while renda_mes <= 0:
    try:
        renda_mes = float(input("Digite sua renda mensal total (em R$): R$"))
        if renda_mes <= 0:
         print("❌ Por favor, digite um valor válido para os gastos com necessidades: R$" "")
    except ValueError:
         print("❌ Por favor, digite apenas números")
         renda_mes = -1
     
gastos_necessidades = -1
while gastos_necessidades < 0:
    try:
        gastos_necessidades = float(input("Digite o valor gasto mensalmente com necessidades: R$"))
        if gastos_necessidades < 0:
         print("❌ Por favor, digite um valor válido para os gastos com necessidades!")
    except ValueError:
         print("❌ Por favor, digite apenas números")
         renda_mes = -1

gastos_desejos = -1
while gastos_desejos < 0:
    try:
        gastos_desejos = float(input("Digite o valor gasto mensalmente com desejos: R$"))
        if gastos_desejos < 0:
         print("❌ Por favor, digite um valor válido para os gastos com desejos!")
    except ValueError:
         print("❌ Por favor, digite apenas números")
         gastos_desejos = -1

add_poupanca = -1
while add_poupanca < 0:
        add_poupanca = input("Consegue poupar algum valor mensalmente? (sim/não): ").strip().lower()
        if add_poupanca == "não" or add_poupanca == "nao":
            add_poupanca = 0
            print("✅ Nenhum valor de valor polpado mensalmente")
        elif add_poupanca == "sim":
            try: 
                add_poupanca_input = input("Qual é o valor que é poupado mensalmente? R$")
                add_valor = float(add_poupanca_input)
                if add_valor >= 0:
                    add_poupanca = add_valor
                    print(f"O valor adicionado mensalmente é {add_valor:.2f}")
                else:
                    print("O valor não pode ser negativo")
                    add_poupanca = -1
            except ValueError:
                print("Digite somente números")
        else:
            print("Digite apenas sim ou não")
            add_poupanca = -1


poupanca_existente = -1 
while poupanca_existente < 0:
        poupanca_resposta = input("Voce possui algum valor em uma poupança? (sim/não)").strip().lower()
        if poupanca_resposta == "não" or poupanca_resposta == "nao":
            poupanca_existente = 0
            print("✅ Nenhum valor em poupança registrado")
        elif poupanca_resposta == "sim":
            try:
                valor_input = input("Qual o valor guardado na poupança exatamente?: R$")
                valor = float(valor_input)
                if valor >= 0:
                    poupanca_existente = valor
                    print(f"O valor na poupança é {valor:.2f}")
            except ValueError:
                print("Digite somente números!")
        



coleta_final = input("Coleta de dados iniciais finalizada, deseja continuar? (sim/não) ").strip().lower()
if coleta_final == "não" or coleta_final == "nao":
    print("Sendo assim, ficamos por aqui! Volte sempre!")
    coleta_final = 0
elif coleta_final == "sim":
    print("\n📊 MENU DE OPÇÕES - ANÁLISE FINANCEIRA\n")
    print("="*50)
    print("1. 📈 Ver análise completa da situação atual")
    print("2. 🎯 Ver metas ideais (Regra 50-30-20)")
    print("3. 💰 Fazer projeção de poupança futura")
    print("4. 📋 Receber recomendações personalizadas")
    print("5. 🔄 Refazer coleta de dados")
    print("6. 🚪 Sair do sistema")
    print("="*50)
    
    opcao = input("Digite o número da opção desejada: ").strip()

if opcao == "1":
    print("📊 ANÁLISE DOS SEUS GASTOS:")

perc_necessidades = (gastos_necessidades / renda_mes) * 100
perc_desejos = (gastos_desejos / renda_mes) * 100
perc_poupanca = (add_poupanca / renda_mes) * 100

print(f"🥦 Necessidades: R$ {gastos_necessidades:.2f} ({perc_necessidades:.1f}%)")
print(f"🎮 Desejos: R$ {gastos_desejos:.2f} ({perc_desejos:.1f}%)") 
print(f"💰 Poupança: R$ {add_poupanca:.2f} ({perc_poupanca:.1f}%)")

    
