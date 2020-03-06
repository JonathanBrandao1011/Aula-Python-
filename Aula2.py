print('Registro Hospital')

nome = input('Qual Nome Completo do Paciente:').title()
idade = int(input('Qual idade do paciente:'))
risco = input('Esta No grupo de risco?: (sim ou nao)').title()
if risco != 'Sim' and risco != 'Nao':
    risco = input('Digite Novamente, Apenas sim ou nao').title()
if idade < 15 or idade > 60:
    print('Paciente precisa de atendimento prioritario')
elif risco == 'Sim':
    print('Paciente precisa de atendimento Prioritario')
else:
    print('Segue na Fila')


