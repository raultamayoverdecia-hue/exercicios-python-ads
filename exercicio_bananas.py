# exercicios-python-ads
Exercícios de lógica de programação em Python - 1º Semestre ADS."
# Entradas
qtd_plastico = int(input("Caixas de plástico vendidas: "))
qtd_metal = int(input("Caixas de metal vendidas: "))

# Cálculos
valor_plastico = qtd_plastico * 5
valor_metal = qtd_metal * 10
total_geral = valor_plastico + valor_metal

# Resultados
print(f"Arrecadado com plástico: R$ {valor_plastico:.2f}")
print(f"Arrecadado com metal: R$ {valor_metal:.2f}")
print(f"Total geral: R$ {total_geral:.2f}")
