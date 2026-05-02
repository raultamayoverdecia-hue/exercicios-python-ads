# Calcula o total de vendas baseado em pacotes fechados
qtd_lapis = int(input("Quantidade de pacotes de lápis (12 un): "))
qtd_canetas = int(input("Quantidade de pacotes de canetas (10 un): "))

total_lapis = qtd_lapis * 8.00
total_canetas = qtd_canetas * 10.00
total_geral = total_lapis + total_canetas

print(f"Total Lápis: R$ {total_lapis:.2f}")
print(f"Total Canetas: R$ {total_canetas:.2f}")
print(f"Total Geral: R$ {total_geral:.2f}")
