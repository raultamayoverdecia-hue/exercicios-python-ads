# Lê o nome e duas notas, calcula a média e imprime o resultado
nome = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))

media = (n1 + n2) / 2

print(f"{nome} obteve a média {media:.1f}")
