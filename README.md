# T2_POOA

Integrantes:
  - Max Marcio F Santos 758935
  - Matheus Schmidt Figueiredo 758616

A ideia central desse projeto é aplicar o princípio aberto-fechado, na prática, usando 
"Construir uma ferramenta para encontrar e baixar títulos das notícias do dia, nos principais sites de notícias (G1, UOL, etc)." como contexto.

Esse projeto foi construido em Python fazendo uso da 
[Beautiful Soup 4](https://pypi.org/project/bs4/) que é uma biblioteca Python para extrair dados de arquivos HTML e XML.

Para executar o codigo basta utilizar o comando a seguir no diretorio raiz
```bash
    python __main__.py
```

# Entendendo o codigo
O código gira em torno de finders, que são classes que procuram o conjunto [nome da noticia + url] nos sites, e processors, que processam a informação gerada pelos finders.

Para adicionar um site nas buscas basta adicionar um finder que herda da classe abstrata NewsFinder para esse site em particular. 
Finders são necessários pois cada site tem uma maneira diferente de colocar suas notícias em seus HTML,
isso faz com que não possamos simplesmente passar o url do site como parametro para um método geral de uma classe finder geral.
Além disso, com os finder nós podemos tratar cada input diretamente dentro do escopo da própria classe.
Isso é util, por exemplo, caso queiramos filtrar algo que venha de um site em especifico ou traduzir os nomes de notícia que vem de sites extrangeiros.

Para adicionar um processo temos que adicionar uma classe que herda de Processor e em seu método execute tratar as informações da maneira como quisermos.

Além disso podemos ter finders ou processors que nao querermos usar ou processors que necessitam de configuração, 
para isso temos um json chamado cfg que nos permite habilitar ou desabilitar finders e processors e também configurar processors.
