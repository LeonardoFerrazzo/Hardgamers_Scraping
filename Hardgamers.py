#© Leonardo Ferrazzo#
from bs4 import BeautifulSoup
import requests
import csv
import numpy

qprod = int(input('Ingrese la cantidad de productos que desea monitorear '))
componente = []

while len(componente)<qprod:
    parte = input('Ingrese componente a buscar ')
    componente.append(parte) #El Append se usa para agregar elementos a la lista

#for i in range (qprod):
 #   componente.append(i)=input('Ingrese producto a buscar')
 #   i=0

gpu = input('Ingrese producto a buscar. Ej: "3070" para buscar una RTX 3070, Use "+" para seguir agregando productos. Ej: 3070+5600x')
url = 'https://www.hardgamers.com.ar/search?text='+gpu
page = requests.get(url) #Pido el request a la url que defini antes
soup = BeautifulSoup(page.content,'html5lib') #El lxml será mi parser de html

#print(soup.prettify()) #Veo el código html.

#page = soup.find()

print("--------------------------------------------------------------------")

print("Precio de componente")

for product_price in soup.find_all('h2',class_='product-price'):
   precio = product_price.text
   print(precio)
   lprecio=soup.find_all('h2',class_='product-price') #Creo una lista con los valores

print("--------------------------------------------------------------------")

print("Descripción")

for product_info in soup.find_all('h3',class_="product-title line-clamp"):
     info = product_info.text
     print(info)
     linfo = soup.find_all('h3',class_="product-title line-clamp")

print("--------------------------------------------------------------------")

print("Vendor")

for vendor in soup.find_all('h4',class_="subtitle"):
     vendedor = vendor.text
     print(vendedor)
     lvendor = soup.find_all('h4',class_="subtitle")

print("-------------------------ITERACIONES-----------------------------")
for i in range(18):
    print(lprecio[i].text)
    i=0
