import pandas as panda

from entidades import Produto
from dao import ProdutoDao

lista = panda.read_csv('./lista-500.csv') 
bd = ProdutoDao() #

for i in range(len(lista)):
    item = lista.iloc[i] #
    produto = Produto(item[1], item[3], marca=item[2]) 
    bd.save(produto) 