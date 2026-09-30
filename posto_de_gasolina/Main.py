from Combustivel import Combustivel
from Veiculo import Veiculo
from Abastecimento import Abastecimento



# FUNÇÃO PARA CALCULAR OS TOTAIS

def calcular_totais(abastecimentos):
    total_etanol = 0
    total_gasolina = 0
    total_diesel = 0

    for abastecimento in abastecimentos:

        if abastecimento.combustivel.nome == "Etanol":
            total_etanol += abastecimento.valor

        elif abastecimento.combustivel.nome == "Gasolina":
            total_gasolina += abastecimento.valor

        elif abastecimento.combustivel.nome == "Diesel":
            total_diesel += abastecimento.valor

    total_dia = total_etanol + total_gasolina + total_diesel

    return total_etanol, total_gasolina, total_diesel, total_dia



# FUNÇÃO PARA GERAR/ATUALIZAR O RECIBO

def gerar_recibo(abastecimentos):
    total_etanol, total_gasolina, total_diesel, total_dia = (
        calcular_totais(abastecimentos)
    )


    with open("recibo_posto.txt", "w", encoding="utf-8") as arquivo:

        arquivo.write("========== POSTO DE GASOLINA ==========\n")

        for abastecimento in abastecimentos:

            arquivo.write(
                f"{abastecimento.veiculo}\n"
            )

            arquivo.write(
                f"Combustível: {abastecimento.combustivel}\n"
            )

            arquivo.write(
                f"Valor: R$ {abastecimento.valor:.2f}\n\n"
            )

        arquivo.write("========================================\n")
        arquivo.write(f"Etanol: R$ {total_etanol:.2f}\n")
        arquivo.write(f"Gasolina: R$ {total_gasolina:.2f}\n")
        arquivo.write(f"Diesel: R$ {total_diesel:.2f}\n")
        arquivo.write(f"TOTAL DO DIA: R$ {total_dia:.2f}\n")



# METODO PARA LER O RECIBO

def ler_recibo():
    with open("recibo_posto.txt", "r", encoding="utf-8") as arquivo:


        conteudo = arquivo.read()

    print("\n")
    print("========== CONTEÚDO DO RECIBO ==========")
    print(conteudo)


    # ENCONTRANDO OS VALORES DENTRO DO TEXTO


    posicao_etanol = conteudo.find("Etanol:")
    posicao_gasolina = conteudo.find("Gasolina:")
    posicao_diesel = conteudo.find("Diesel:")
    posicao_total = conteudo.find("TOTAL DO DIA:")

    # Pegando as linhas completas
    linha_etanol = conteudo[posicao_etanol:].split("\n")[0]
    linha_gasolina = conteudo[posicao_gasolina:].split("\n")[0]
    linha_diesel = conteudo[posicao_diesel:].split("\n")[0]
    linha_total = conteudo[posicao_total:].split("\n")[0]

    print("========== VALORES ENCONTRADOS NO TXT ==========")
    print(linha_etanol)
    print(linha_gasolina)
    print(linha_diesel)
    print(linha_total)



# COMBUSTÍVEIS

etanol = Combustivel("Etanol")
gasolina = Combustivel("Gasolina")
diesel = Combustivel("Diesel")



# VEÍCULOS INICIAIS

carro = Veiculo("Carro", "ABC-1234")
moto = Veiculo("Moto", "DEF-5678")
van = Veiculo("Van Escolar", "GHI-9012")



# ABASTECIMENTOS INICIAIS

abastecimento1 = Abastecimento(carro, etanol, 50)
abastecimento2 = Abastecimento(moto, gasolina, 25)
abastecimento3 = Abastecimento(van, diesel, 200)



# LISTA PRINCIPAL DE ABASTECIMENTOS

abastecimentos = [
    abastecimento1,
    abastecimento2,
    abastecimento3
]



# MOSTRANDO ABASTECIMENTOS INICIAIS

print("========== ABASTECIMENTOS DO DIA ==========")

for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()



# ETAPA 1
# GERANDO O RECIBO INICIAL

gerar_recibo(abastecimentos)

print("\nRecibo inicial criado com sucesso!")



# ETAPA 2
# NOVOS VEÍCULOS


onibus = Veiculo("Ônibus", "JKL-3456")
caminhao = Veiculo("Caminhão", "MNO-7890")
pickup = Veiculo("Pickup", "PQR-1122")
suv = Veiculo("SUV", "STU-3344")
byd = Veiculo("BYD", "VWX-5566")



# NOVOS ABASTECIMENTOS


abastecimento4 = Abastecimento(onibus, diesel, 300)
abastecimento5 = Abastecimento(caminhao, diesel, 450)
abastecimento6 = Abastecimento(pickup, gasolina, 120)
abastecimento7 = Abastecimento(suv, gasolina, 180)
abastecimento8 = Abastecimento(byd, etanol, 80)



# ADICIONANDO OS NOVOS ABASTECIMENTOS
# À LISTA PRINCIPAL


abastecimentos.append(abastecimento4)
abastecimentos.append(abastecimento5)
abastecimentos.append(abastecimento6)
abastecimentos.append(abastecimento7)
abastecimentos.append(abastecimento8)



# MOSTRANDO TODOS OS ABASTECIMENTOS


print("\n========== TODOS OS ABASTECIMENTOS ==========")

for abastecimento in abastecimentos:
    abastecimento.mostrar_abastecimento()




# ATUALIZANDO O MESMO ARQUIVO TXT


gerar_recibo(abastecimentos)

print("\nRecibo atualizado com sucesso!")



# ETAPA 3
# LENDO O ARQUIVO TXT


ler_recibo()