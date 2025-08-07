destinos = [
    {"nome":"Sâo luís","clima": "quente", "tipo": "urbano", "preco": 1000},
    {"nome":"Panaquatira","clima": "quente", "tipo": "rural", "preco": 40},
    {"nome":"Cabiceira do Curtia","clima": "frio", "tipo": "rural", "preco":2000 },
    {"nome":"Tropical","clima": "frio", "tipo": "urbano", "preco":10000 }
]
def recomendar_destino(clima, tipo, preco_max):
    for destino in destinos:
        if destino["clima"] == clima and destino["tipo"] == tipo and destino["preco"] <= preco_max:
            return f"Recomendamos: {destino['nome']} - Combina com seu orçamento."
    return "nenhum destino foi encontrado"

clima = input("Você prefere clima quente ou frio? ").strip().lower()
tipo = input("Prefere lugares com natureza ou paisagens urbanas?").strip().lower()
orcamento = float(input("Qual o seu orçamento disponível?"))

print(recomendar_destino(clima, tipo, orcamento))