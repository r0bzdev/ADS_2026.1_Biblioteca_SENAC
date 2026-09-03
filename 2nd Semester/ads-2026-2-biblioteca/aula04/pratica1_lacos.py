# Aquecimento: Laços

servicos = ["corte", "barba", "sobrancelha", "hidratacao"]
precos = {"corte": 35, "barba": 25, "sobrancelha": 15, "hidratacao": 40}
comanda = ["corte", "barba", "corte", "pintura"]

# 0. Percorra servicos com for e imprima cada um
for servico in servicos:
    print(servico)


# 1. Imprima a mesma lista numerada a partir de 1, com enumerate
for numero, servico in enumerate(servicos, start=1):
    print(numero, servico)


# 2. Some com um for os precos dos itens da comanda
# que existem no dicionario precos
total = 0

for item in comanda:
    if item in precos:
        total += precos[item]

print("Total:", total)


# 3. Usando while, descubra quantos cortes de 35 cabem em 200
valor = 200
cortes = 0

while valor >= 35:
    valor -= 35
    cortes += 1

print("Quantidade de cortes:", cortes)


# 4. Percorra a comanda e imprima so os itens do catalogo,
# usando continue para pular os outros
for item in comanda:
    if item not in precos:
        continue

    print(item)

itens = ["corte", "pintura", "tintura", "barba"]

for item in itens:
    if item not in ("corte", "barba"):
        itens.remove(item)

print(itens)
