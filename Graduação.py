graduacao = str(input("Digite qual o tipo graduação você realiza:\n ")).title().strip()
while graduacao != 'Tecnologo' and graduacao != 'Tecnólogo' and graduacao != 'Bacharelado':
    print('Tipo de graduação invalida')
    graduacao = str(input("Digite qual o tipo graduação você realiza:\n ")).title().strip()

if graduacao == "Tecnologo" or graduacao == "Tecnólogo":
    print ("Tecnólogo tem duração de 2 até 3 anos.")
elif graduacao == "Bacharelado":
    print ("A duração de um bacharelado é de 4 até 6 anos.")
else:
    print("Tipo de graduação inválida.")