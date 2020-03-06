print('Registro Hospital')

nome = input('Qual nome do Paciente:').title()
idade = int(input('Qual idade do paciente:'))
while(idade < 1 or  idade > 100):
    print('Idade Invalida')
    idade = int(input('Insira a idade correta:'))

risco = input('Esta No grupo de risco?: (sim ou nao)').title()
while(risco != 'Sim' and risco != 'Nao'):
    risco = input('Digite Novamente, Apenas sim ou nao:').title()

if idade < 15 or idade > 60:
    print('O paciente '+(nome)+' precisa de atendimento prioritario')
elif risco == 'Sim':
    print('O paciente '+(nome)+' precisa de atendimento Prioritario')
else:
    print('O paciente '+(nome)+' Segue na Fila')

