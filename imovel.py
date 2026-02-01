class Imovel:
    def __init__(self, tipo, quartos, garagem, criancas):
        self.tipo = tipo.lower()
        self.quartos = quartos
        self.garagem = garagem
        self.criancas = criancas

    def calcular_aluguel(self):
        valor = 0

        # APARTAMENTO
        if self.tipo == "apartamento":
            valor = 700

            if self.quartos == 2:
                valor += 200

            if self.garagem:
                valor += 300

            if not self.criancas:
                valor *= 0.95  # desconto de 5%

        # CASA
        elif self.tipo == "casa":
            valor = 900

            if self.quartos == 2:
                valor += 250

            if self.garagem:
                valor += 300

        # ESTÚDIO
        elif self.tipo == "estudio":
            valor = 1200

            if self.garagem >= 2:
                valor += 250

                if self.garagem > 2:
                    valor += (self.garagem - 2) * 60

        return round(valor, 2)
    