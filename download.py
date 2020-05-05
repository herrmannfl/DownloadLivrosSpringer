import csv
import os
import sys
import urllib.request
import xlrd
import time

print("Baixando lista de livros do site da Springer...")
urllib.request.urlretrieve("https://resource-cms.springernature.com/springer-cms/rest/v1/content/17858272/data/v5", "livros.xlsx")
print("Criando dicionário do arquivo baixado....")
workbook = xlrd.open_workbook('livros.xlsx')
worksheet = workbook.sheet_by_index(0)
first_row = []
for col in range(worksheet.ncols):
    first_row.append( worksheet.cell_value(0,col))
# criando o dicionário
data =[]
for row in range(1, worksheet.nrows):
    elm = {}
    for col in range(worksheet.ncols):
        elm[first_row[col]]=worksheet.cell_value(row,col)
    data.append(elm)
#percorrendo o dicionário criado.
for i in range(len(data)):
    startime = time.time()

    # pegando a última parte do link DOI para compor a URL de download do PDF
    link = data[i]['DOI URL']
    parts = link.split("/")
    filespringer = parts[len(parts)-1] # pegando última posição do
    url = "https://link.springer.com/content/pdf/10.1007/"+filespringer+".pdf"

    # Criando diretório para download (se não existir)
    pwd = os.getcwd()
    foldername = pwd+"/"+data[i]['English Package Name']
    if not os.path.exists(foldername):
        os.mkdir(foldername)

    #nome do arquivo local (depois do download)
    bookname = data[i]['Book Title']
    clearbookname = bookname.replace(":","-") # removendo : do nome
    clearbookname = clearbookname.replace("/","-") # removendo / do nome
    filename = foldername +"/"+ clearbookname + ".pdf"

    #Iniciando dowload
    print("Download em andamento: "+data[i]['Book Title']+"-"+url+"...")
    try:
        urllib.request.urlretrieve(url, filename)
        # calculando tempo de download
        hours, rem = divmod(time.time() - startime, 3600)
        minutes, seconds = divmod(rem, 60)
        print("Tempo de download: {:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds))
    except:
        print("ERRO!")