# fatiamento_strings.py

s = "Insper"
# I N S P E R
# 0 1 2 3 4 5

# Fatiamento [início : fim_exclusivo]
t = s[2:4] 
print(f"Fatiamento de '{s}' [2:4]: {t}") # Resultado: 'sp'

# Variantes possíveis:
print(f"Do início até o índice 3: {s[:3]}") # 'Ins'
print(f"Do índice 3 até o fim: {s[3:]}")    # 'per'
print(f"String invertida: {s[::-1]}")       # 'repsnI'
