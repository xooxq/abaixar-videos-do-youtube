from pytube import YouTube
from os import system
from time import sleep

def limpar(x):
    system('cls')
    print(x)
    sleep(1)
    system('cls')

while True:
    system('cls')
    while True:
        try:
            #caso você digite errado o link ou qualquer coisa que não seja o link, vai retornar um erro do pytube e não do código em sí.
            x = input("Digite a url do link (0 para cancelar): ").strip()
            if x == "0":
                break
            yt = YouTube(x)
            break
        except:
            limpar("Erro. Digite um link válido!")
    if x == '0':
        break
    system('cls')
    print('\tYoutube')
    print("-"*30)
    print('O que deseja fazer com o link?\n')
    while True:
        try:
            y = int(input("""[0] Cancelar
[1] Vídeo
[2] Áudio
"""))
            if y <= 2 and y >= 0:
                break
            else:
                limpar("Digite apenas de 0 a 2!")
        except ValueError:
            limpar("Digite apenas números!")
    if y==0:
        break
    print("-"*30)

    if y == 1:
        #caso você queira abaixar outra resolução, só alterar de "720p", para a resolução desejada.
        vd = yt.streams.filter(res="720p", progressive=True, file_extension="mp4").first()
        if vd:
            vd.download(filename=f"{yt.title}.mp4") # o vídeo será abaixado na pasta de onde o .py estiver.
        else:
            print('Não foi possível abaixar esse vídeo')
    else:
        ad = yt.streams.filter(only_audio=True).first()
        if ad:
            ad.download(filename=f"{yt.title}.mp3") # assim como o vídeo, o áudio será abaixado na pasta de onde o .py estiver. 
        else:
            print('Infelizmente não é possível abaixar esse áudio.')
    sleep(2)
    z = input("Deseja abaixar mais algo (s/n) ?: ").strip().upper()
    #e aqui, fazendo a verificação para que o user digite apenas "s" ou "n".
    while z not in "SN":
        limpar("Digite apenas 's' ou 'n'.")
        z = input("Deseja abaixar mais coisas (s/n) ?: ").strip().upper()
    if z == 'N':
        system('cls')
        print('Fim do programa. Volte logo\n')
        break
    #faça bom uso do código :)
