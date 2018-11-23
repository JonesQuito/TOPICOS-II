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
Agora, após o ambiente ter sido devidamente preparado, podemos executar o projeto, mas antes vamos entender como o mesmo está estruturado. Dentro do diretório do projeto `TOPICOS-II` temos alguns diretórios e arquivos necessários para o funcionamento projeto. Vamos começar pelo diretório `dataset_txt`: &nbsp;


	#### dataset_txt
	- Religião
	- Esportes
	- Educação
	- Saúde
	- Política
O `dataset_txt` é o nosso dataset, é o conjunto de dados usado para treinar os nossos classificadores. Ele contém 5 subdiretórios que representam as 5 classes de texto possíves. Dentro de cada diretório há vários textos da classe correspondente ao nome do diretório.  

Na raíz do projeto também temos o diretório `modulos` que contém módulos como `file.py` contendo funções para manipular arquivos, como exemplo, temos a função `getAllFiles(path)` que retorna uma lista com todos os arquivos encontrados no diretório passado como argumento da função. Outra função importante do módulo `file.py` é a `getDirectories(path, index)`, ela lista os subdiretórios de um diretório passado como argumento. 

No referido módulo também temos a função `cleaner(text)` que recebe um texto e remove todos os caracteres que não sejam letras do alfabeto português, remove palavras formadas por menos que 2 caracteres e stop words, além de reduzir as palavras ao seu radical. 

Finalmente, após o ambiente preparado e os principais componentes da estrutura do projeto compreendidos, vamos executar os notebooks para ver e compreender as etapas do processo de classificação de textos com ntlk e scikit-learn.

- A
	


`create table database_text
(
	id serial primary key,
	classe varchar(30),
	narrativa text
);`
