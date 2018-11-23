# Classificação de textos com nltk e scikit-learn

## Preparando o ambiente

### Pré requisitos
	### Pré requisitos
	[] python
	[] postgres
	[] virtualenv
	[] jupyter-notebook
	[] psycopg2
	[] nltk
	[] pandas
	[] matplotlib
	[] scikit-learn
	
---
### Etapas de preparação do ambiente
- Primeiramente sertifique-se de está com o python 3.x instalado na máquina (Foi testado no python 3.7)

- Instale o SGBD postgres e o pgadmin
	- Os scrips supôem que tenha um banco de dados de nome `topicos_ii` criado em `localhost` com o usuário `postgres` e senha `postgres`. Dessa forma recomenda-se que esta estrutura esteja disponível em seu computador ou que os dados de conexão com o banco sejam alterados nos scrips para refletir o banco que você tem disponível para uso.
	
- Instale o virtualenv (cmd)
	- `pip install virtualenv`
	
- Crie um ambiente virtual (cmd)
	- `virtualenv nome_do_ambiente`
	
- Faça o clone do projeto dentro do ambiente virtual criado no passo anterior. Use o seguint comando no git bash:
	- `git clone https://github.com/JonesQuito/TOPICOS-II.git`

- Navegue para dentro do seu ambiente virtual criado anteriormente e ative-o(cmd)
	- `Scripts\activate`

- Com o ambiente virtual ativo, instale as bibliotecas necessárias para o projeto
	- `pip install jupyter`
	- `pip install psycopg2`
	- `pip install nltk`
	- `pip install pandas`
	- `pip install matplotlib`
	- `pip install -U scikit-learn`

---
### Descrição do projeto
Agora, após o ambiente ter sido devidamente preparado, podemos executar o projeto, mas antes vamos entender como o mesmo está estruturado. Dentro do diretório do projeto `TOPICOS-II` temos alguns diretórios e arquivos necessários para o funcionamento projeto. &nbsp; Vamos começão pelo diretório `dataset_txt`: &nbsp;


	#### Base_de_dados_de_textos
		- Religião
		- Esportes
		- Educação
		- Saúde
		- Política


`create table database_text
(
	id serial primary key,
	classe varchar(30),
	narrativa text
);`
