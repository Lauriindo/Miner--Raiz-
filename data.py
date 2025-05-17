from sqlalchemy import create_engine #Estou startando a conexão com o banco de dados
from sqlalchemy.orm import sessionmaker #Estou importando o sessionmaker para criar uma sessão com o banco de dados
from sqlalchemy.ext.declarative import declarative_base #Estou importando o declarative_base para criar as classes que representam as tabelas do banco de dados
db = create_engine("mysql+pymysql://root:1234@127.0.0.1:3306/Mineradora")#Aqui eu passo os parametros de conexão com o banco de dados, como Usuario:senha:ip do banco:nome

Session = sessionmaker(bind=db) #Aqui eu crio uma sessão com o banco de dados
session = Session() #Aqui eu crio uma sessão com o banco de dados

declarative_base() #Aqui eu crio uma base declarativa para criar as classes que representam as tabelas do banco de dados