import os
from PIL import Image


def extensao(arquivo):
    index = arquivo.rfind('.')
    return arquivo[index:]


def imagens(diretorio):
    ext_img = ['.png', '.jpg', '.jpeg']
    if not os.path.isdir(diretorio):
        print("Não existe esse diretório")
    else:
        arquivos = os.listdir(diretorio)
        if arquivos == []:
            print('Não existe imagens na pasta.')

        lista = []
        for nome in arquivos:
            if os.path.isfile(os.path.join(diretorio, nome)):
                ext = str.lower(extensao(nome))
                if ext in ext_img:
                    arquivo = os.path.join(diretorio, nome)
                    lista.append([arquivo, nome])
        return lista


def recortar(diretorio, onde='img', esquerda=0, topo=60, direita=1120, fundo=700):
    lista_imagens = imagens(diretorio)
    for i, item in enumerate(lista_imagens):
        imagem = item[0]
        img = Image.open(imagem)
        area = (esquerda, topo, direita, fundo)

        arquivo = item[1]
        salvar = onde
        endereco = f'{salvar}/{arquivo}'

        if not os.path.isdir(salvar):
            os.mkdir(salvar)

        recortada = img.crop(area)
        recortada.save(endereco)

        print(f"'{arquivo}' => recortado e salvo com sucesso!")


op = True
while op:
    print(40*'==')
    print('Recortar Imagens')
    print(40*'--')
    print()
    diretorio = str(input('Diretorio onde estão as imagens: '))
    salvar = str(input('Diretorio onde deve salvar as imagens: '))
    recortar(diretorio, salvar)

    print()
    opcao = input("Aperte 'f' para finalizar. ")
    if opcao.lower() == 'f':
        op = False

    print()
    print('FIM!!!')
    print(40*'==')
