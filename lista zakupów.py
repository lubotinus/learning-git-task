lista = {
    "piekarnia": ["Chleb", "Bułka", "Pączek"],
    "warzywniak": ["Marchew", "Ser", "Rukola"]
}
n = 0
for x, y in lista.items():
    print(f"Idę do {x.title()}, kupiję tu następujące rzeczy: {y}")
    n = n + len(y)
print(f"W sumie kupuję {n} produktów")
print("Zmiana w branch")