# Classificação de textos com nltk e scikit-learn
## Preparando o ambiente
	### Pré requisitos
	[] python
	[] postgres
	[] jupyter-notebook
	[] scikit-learn
	[] nltk
	[] pandas
	[] matplotlib
	[] psycopg2

- Primeiramente sertifique-se de está com o python 3.x instalado na máquina (Foi testado no python 3.7)

- Instale o SGBD postgres e o pgadmin
	Os scrips supôem que tenha um banco de dados de nome `topicos_ii` criado em `localhost` com o usuário `postgres` e senha `postgres`. Dessa forma recomenda-se que esta estrutura esteja disponível em seu computador ou que os dados de conexão com o banco sejam alterados nos scrips para refletir o banco que você tem disponível para uso.
	
- Instale o virtualenv (cmd)
	`pip install virtualenv`
	
- Crie um ambiente virtual (cmd)
	`virtualenv nome_do_ambiente`
	
- Faça o clone do projeto dentro do ambiente virtual criado no passo anterior. Use o seguint comando no git bash:
	`git clone https://github.com/JonesQuito/TOPICOS-II.git`


### Base_de_dados_de_textos esta organizada nas seguintes categorias:
#### - Religião
#### - Esportes
#### - Educação
#### - Saúde
#### - Política


`create table database_text
(
	id serial primary key,
	classe varchar(30),
	narrativa text
);`
