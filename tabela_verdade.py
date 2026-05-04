# tabela_verdade.py

print("A | B | NOT A | A AND B | A OR B")
print("-" * 30)

combinacoes = [(True, True), (True, False), (False, True), (False, False)]

for a, b in combinacoes:
    print(f"{a} | {b} | {not a} | {a and b} | {a or b}")
