import numpy as np 

class MonitorarTemperatura:
    def __init__(self):
        self.leituraTemperatura = []
    def adicionarTemperatura(self, valor):
        self.leituraTemperatura.append(valor)
        print(f"Nova leitura registrada: {valor} °C")
    def calcular_estatisticas(self):
        dados = np.array(self.leituraTemperatura)
        estatistica = {
            "máxima" : dados.max(),
            "mínima" : dados.min(),
            "média" : dados.mean()
        }
        return estatistica
    def verificar_seguranca(self):
        fora_do_limite = False
        for temp in self.leituraTemperatura:
            if temp < 20 or temp > 80:
                print(f"Alerta!!!!! Temperatura fora do limite seguro detectada: {temp} °C")
        if not fora_do_limite:
            print("Todas as temperaturas estão dentro do limite seguro")
monitor = MonitorarTemperatura()
leituraTemperatura = [25,30,90,45,70]
for temp in leituraTemperatura:
    monitor.adicionarTemperatura(temp)
estatisticas = monitor.calcular_estatisticas()
print("\n Estátisticas das temperaturas registradas:")
print(f"Temperatura Máxima: {estatisticas['máxima']} °C")
print(f"Temperatura Mínima: {estatisticas['mínima']} °C")
print(f"Temperatura Média: {estatisticas['média']} °C")
monitor.verificar_seguranca()