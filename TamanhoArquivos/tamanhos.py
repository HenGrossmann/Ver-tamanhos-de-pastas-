import os
import math
from tkinter import filedialog
import tkinter as tk

def get_folder_size(caminho_pasta):
    tamanho_total = 0
    for caminho_dir, sub_dir, arquivos in os.walk(caminho_pasta):
        for f in arquivos:
            # Soma todos arquivos naquela pasta
            caminho_arquivo = os.path.join(caminho_dir, f)
            tamanho_total += os.path.getsize(caminho_arquivo)
    return tamanho_total

def converter_tamanho(size_bytes):
    # Converte o tamanho do arquivo para ser mais facil de ler
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"


if __name__ == '__main__':
    # Janela do tkinter
    root = tk.Tk()
    root.withdraw()

    # Pede para o usuario escolher uma pasta
    caminho_pasta = filedialog.askdirectory()

    if caminho_pasta != '':
        lista_tamanhos_pasta = []
        for nome_do_arquivo in os.listdir(caminho_pasta):
            # Ver o que tem dentro e ver se e uma pasta
            pasta_dentro = os.path.join(caminho_pasta, nome_do_arquivo)

            
            if os.path.isdir(pasta_dentro):
                
                # Tamanho do arquivo
                tamanho_pasta = get_folder_size(pasta_dentro)

                # Converter tamanho do arquivo para ser mais facil de ler
                lista_tamanhos_pasta.append((nome_do_arquivo, tamanho_pasta))

        # Ordenar a lista por arquivos maiores
        lista_tamanhos_pasta.sort(key=lambda x: x[1], reverse=True)

        # printar a lista
        for nome_do_arquivo, tamanho_bytes in lista_tamanhos_pasta:
            # convert the folder size to a more human-readable format
            str_tamanho = converter_tamanho(tamanho_bytes)

            # print the name and size of the folder
            print(f"{nome_do_arquivo}: {str_tamanho}")
        
    else:
        print('Caminho nao encontrado')