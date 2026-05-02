# Peso do prato montado menos o peso do prato vazio (100g)
peso_prato_cheio = float(input("Peso total do prato (kg): "))
peso_vazio = 0.1

valor_pagar = (peso_prato_cheio - peso_vazio) * 30.00

print(f"Valor a pagar: R$ {valor_pagar:.2f}")
