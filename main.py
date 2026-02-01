import csv
from imovel import Imovel
from contrato import Contrato

print("===== SISTEMA DE ORÇAMENTO IMOBILIÁRIO =====")

tipo = input("Tipo de imóvel (apartamento / casa / estudio): ")
quartos = int(input("Quantidade de quartos (1 ou 2): "))

if tipo.lower() == "estudio":
    garagem = int(input("Quantidade de vagas de estacionamento: "))
    criancas = False
else:
    garagem = input("Possui garagem? (s/n): ").lower() == "s"
    criancas = input("Possui crianças? (s/n): ").lower() == "s"

# Criando objeto Imóvel
imovel = Imovel(tipo, quartos, garagem, criancas)
valor_aluguel = imovel.calcular_aluguel()

# Criando objeto Contrato
contrato = Contrato()
parcelas = int(input("Deseja parcelar o contrato em quantas vezes? (até 5): "))
valor_parcela_contrato = contrato.parcelar(parcelas)

# Exibição dos resultados
print("\n===== ORÇAMENTO FINAL =====")
print(f"Valor do aluguel mensal: R$ {valor_aluguel}")
print(f"Contrato imobiliário: {parcelas}x de R$ {valor_parcela_contrato}")

# Gerando CSV
with open("orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["Parcela", "Valor Mensal"])

    for i in range(1, 13):
        writer.writerow([i, valor_aluguel])

print("\nArquivo 'orcamento.csv' gerado com sucesso!")
print("============================================")
