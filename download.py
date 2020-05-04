import csv
import os
import sys
import urllib.request

dirName='./'
with open(dirName+'listalivros.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} \t{row[1]} \t{row[2]} \t{row[3]}')
            line_count += 1
            #criando a pasta
            nomepasta = dirName+row[1]
            if not os.path.exists(nomepasta):
                os.mkdir(nomepasta)
                print("Directory ", nomepasta, " Created ")
            else:
                print("Directory ", nomepasta, " already exists")
            # fazendo download do arquivo
            print('Beginning file download ...')
            url = row[3]
            nomeArquivo = nomepasta +"/"+ row[0] + ".pdf"
            if not os.path.exists(nomeArquivo):
                try:
                    urllib.request.urlretrieve(url, nomeArquivo)
                except:
                    print("An exception occurred")
                    print(url+" - "+nomeArquivo)
            else:
                print("File ",nomeArquivo," already exists")


    print(f'Processed {line_count} lines.')
