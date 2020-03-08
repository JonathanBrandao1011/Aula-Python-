nome = input('Insira seu nome:').title()
genero = input('Qual seu genero:').title()
while genero != 'Feminino' and genero != 'Masculino':
    print('insira apenas masculino ou feminino')
    genero = input('Qual seu genero:').title()

Permi = input('Qual seu nivel de acesso:').title()
while Permi != 'Adm' and Permi != 'Usr' and Permi != 'Guest'and Permi!= 'Sem Nivel':
    Permi =input('Coloque um dos niveis: Adm, Usr ou Guest.\nCaso nao tenha um nivel de acesso digite Sem nivel:').title()

if Permi == 'Adm':
    Senha = input('Insira a Senha de acesso:').title()
    while Senha != 'Batata123':
        print('Senha incorreta')
        Senha = input('Insira a Senha de acesso:').title()
elif Permi == 'Usr':
    Senha = input('Insira a Senha de acesso:').title()
    while Senha != 'Tomate123':
        print('Senha incorreta')
        Senha = input('Insira a Senha de acesso:').title()
elif Permi == 'Guest':
    Senha = input('Insira a Senha de acesso:').title()
    while Senha != 'Abacate123':
        print('Senha incorreta')
        Senha = input('Insira a Senha de acesso:').title()
    
if genero == 'Feminino' and Permi == 'Adm':
    print('Bem vinda Administradora '+(nome))
elif genero == 'Masculino' and Permi == 'Adm':
    print('Bem vindo Administrador '+(nome))
elif genero == 'Feminino' and Permi == 'Usr':
    print('Bem vinda Usuaria '+(nome))
elif genero == 'Masculino' and Permi == 'Usr':
    print('Bem vindo Usuario '+(nome))
elif genero == 'Feminino' and Permi == 'Guest':
    print('Bem vinda Visitante '+(nome))
elif genero == 'Masculino' and Permi == 'Guest':
    print('Bem vindo Visitante '+(nome))
elif genero == 'Masculino':
    print('Ola Desconhecido')
else:
    print('Ola Desconhecida')