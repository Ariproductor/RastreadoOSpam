

def verificacao1(email):
    for teste in enderecosfalsos:
        if teste == email[0:email.find(" ")]:
            spams.append(email)
            return False
    return True


def verificacao2(email):
    emailcopia = email.upper()
    for teste in termos:
        if teste in emailcopia:
            add_endereco(email)
            spams.append(email)
            return False
    return True


def add_endereco(email):  
    endereco = email[0:email.find(" ")]
    enderecosfalsos.append(endereco)


def mover():
    print("Caixa de entrada:")
    print(caixa_de_entrada)
    print("Spam:")
    print(spams)
    opcao = int(input('''
                      De qual sessão deseja mudar um email para outra posicao? 
                      Digite 1 se for da Caixa de Entrada, 
                      Ou Digite 2 se for da de Spams: '''))
    if opcao == 1:

        posicao = int(input('''
                            O email de qual posicao? 
                            Vale lembrar que começa sempre da posição 0.: '''))
        copia = caixa_de_entrada[posicao]
        add_endereco(copia)
        del(caixa_de_entrada[posicao])
        spams.append(copia)
        
    if opcao == 2:

        posicao = int(input('''
                            O email de qual posicao? 
                            Vale lembrar que começa sempre da posição 0.: '''))
        copia = spams[posicao]
        endereco = copia[0:copia.find(" ")]
        enderecosfalsos.remove(endereco)
        del(spams[posicao])
        caixa_de_entrada.append(copia)



def atualizar():
    qtd_Caixa_de_entrada = len(caixa_de_entrada)
    qtd_Spams = len(spams)
    ind1 = 0
    ind2 = 0

    for cont1 in range(0,qtd_Caixa_de_entrada):
        email = caixa_de_entrada[ind1]
        for teste in enderecosfalsos:
            if teste == email[0:email.find(" ")]:
                copia = email
                caixa_de_entrada.remove(email)
                spams.append(copia)
                ind1 = ind1 - 1
        ind1 = ind1 + 1

    for cont2 in range(0,qtd_Spams):
        teste3 = 0
        email = spams[ind2]
        for teste in enderecosfalsos:
            if teste == email[0:email.find(" ")]:
                teste3 = 1
                ind2 = ind2 + 1
        if teste3 == 0:
            print(email)
            copia = email
            spams.remove(email)
            caixa_de_entrada.append(copia)

    print("Caixa de entrada:")
    print(caixa_de_entrada)
    print("Spam:")
    print(spams)
    print(ind2)


def caixas():

    open("emails_normais.txt", "w").close()
    open("emails_spams.txt", "w").close()

    emails_normais = open("emails_normais.txt", "w")
    emails_spams = open("emails_spams.txt", "w")
    for email in caixa_de_entrada:
        emails_normais.write(f"{email}\n")
    for email in spams:
        emails_spams.write(f"{email}\n")

    emails_normais.close()
    emails_spams.close()



emails = []
e = open ("Email.txt")
for linha in e:
    emails.append(linha.strip())

termos = []
t = open ("Termos.txt")
for linha in t:
    termos.append(linha.strip())


emails_normais = open('emails_normais.txt', 'w')
emails_spams = open('emails_spams.txt', 'w')

enderecosfalsos = []
caixa_de_entrada = []
spams = []

for email in emails:
    teste1 = verificacao1(email)
    if teste1:
        teste2 = verificacao2(email)
    if (teste1) and (teste2):
        caixa_de_entrada.append(email)


while True:

    escolha = int(input('''
                        Afim de testar o programa há 5 escolhas que pode fazer: 
                        Digite 1 para visualizar seus emails; 
                        Digite 2 para mudar um email de lugar; 
                        Digite 3 para criar os arquivos das caixas atualizadas;  
                        Digite 4 para atualizar todos os emails; 
                        mas caso queira finalizar o programa digite qualquer outro inteiro.: '''))

    if escolha == 1:
        print("Caixa de entrada:")
        print(caixa_de_entrada)
        print("Spam:")
        print(spams)
        continue
    elif escolha == 2:
        mover()
        continue
    elif escolha == 3:
        caixas()
        continue
    elif escolha == 4:
        atualizar()
        continue
    else:
        print("Não digitou nem 1, 2, 3 ou 4, o programa será finalizado.")
        break
