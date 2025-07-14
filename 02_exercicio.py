while True:
    nome = input("Digite o nome do usuário: ")

    if len(nome) >= 3:
        break
    else:
        print("Nome deve ter três caractéres ou mais!") 
        
while True:
    idade = int(input("Digite a sua idade: "))
    if idade <= 150 and idade >= 0:
        break        
    else:
        print("Idade deve ser menor que 150!")
        
while True:
    salario = float(input("Digite o seu salário: "))
    if salario > 0:
        break 
    else:
        print("Salalário deve ser maior que zero!")
        
while True:
    genero = input("Digite seu gênero. 'M' para msaculino, 'F' para feminino e  'O' para outro: ").upper()
    if genero in ['M', 'F', 'O']:
        break
    else:
        print("Digite o gênero novamente!")
        
while True:
    estado_civil = input("Digite seu estado civil. 'S' para soltero, 'C' para casado, 'V' para viúvo, 'D' para divorcido:").upper()
    if estado_civil in ['S', 'C', 'V', 'D']:
        break
    else:
        print("Estado Civil inválido. Digite novamente!")

print(f"Nome: {nome}.")
print(f"Idade: {idade}.")
print(f"Salário: R${salario:.2f}.")
if genero == 'M':
    print("Gênero: Masculino.")
elif genero == 'F':
    print("Gênero: Feminino.")
elif genero == 'O':
    print("Gênero: Outro.")
if estado_civil == 'S':
    print("Estado Civil: Solteiro.")
elif estado_civil == 'C':
    print("Estado Civil: Casado.")
elif estado_civil == 'D':
    print("Estado Civil: Divociado.") 
elif estado_civil == 'V':
    print("Estado Civil: Viúvo.")      