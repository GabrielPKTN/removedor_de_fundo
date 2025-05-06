from PIL import Image
import rembg

def remover(caminho_entrada, caminho_saida):
    with open(caminho_entrada, "rb") as arquivo_entrada, open(caminho_saida, "wb") as arquivo_saida:

        imagem_entrada = Image.open(arquivo_entrada)

        imagem_saida = rembg.remove(imagem_entrada)

        imagem_saida.save(arquivo_saida, "PNG")

caminho_entrada = "./img/teste.jpg"
caminho_saida = "./img/new_teste.png"
remover(caminho_entrada, caminho_saida)