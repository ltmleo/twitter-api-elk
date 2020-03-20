# Twitter API
Esse projeto mostra de maneira simplificada o funcionamento de um ecossistema de microsserviços. E contém principalmente 4 componentes:
- Uma aplicação python agendada para rodar de hora em hora que salva informações adquiridas com a API do twitter em um banco de dados não relacional (mongoDB);
- API REST para realizar consultas ao banco, desenvolvida em Flask;
- Interface Web para consumir esta API desenvolvida em FLask;
- Stack de monitoração, logging e APM (elastic) para acompanhar o desempenho do sistema desenvolvido.
 
Além disso, visando auto escalabilidade e facilidade no deploy, foram utilizadas as ferramentas Helm e Kubernetes.
 
**Table of Contents**
 
[TOCM]
 
[TOC]
 
## Requisitos
- Minikube: v1.1.9
- Kubernetes:  v1.15.4
- Docker: v18.09.7
- Helm: v2.14.2
- Python: v3.6.9
 
## Componentes
### save-tweets
Responsável por alimentar o banco de dados, esse componente é agendado para rodar de uma e uma hora consumindo determinadas **#hashtags**, listadas abaixo:
- "#openbanking", "#apifirst", "#devops", #cloudfirst", "#microservices", "#apigateway",  "#oauth", "#swagger", "#raml" e "#openapis".
e salvando as seguintes informações de cada tweet:
- user: username do usuário;
- followers: Quantidade de seguidores do usuário;
- date: Data em que o tweet foi publicado;
- language: Língua em que o tweet foi publicado;
- country: Localização em que o tweet foi publicado;
#### Operação
Para rodar essa aplicação é necessário exportar como variável de ambiente a variável **PASSWORD**, à qual irá descriptografar as secrets e tokens da API do twitter.
#### Melhorias
- Colocar a variável PASSWORD como uma secret no kubernetes;
- Colocar o atributo salt da classe Crypt como um secret no kubernetes;
- Ler de um config map as hashtgas pela qual o programa deve iterar;
-  Modificar a maneira com o qual o logstash acessar os logs da aplicação;
-  Adicionar autenticação ao acesso do mognoDB;
### get-tweets-api
Responsável por consumir as informações no banco de dados e export em forma de uma API RESTFUL. Como está API foi pensada apenas para consumir os dados dos banco, apenas o método GET está disponível. O swagger da aplicação está disponível no prefixo "/" da aplicação.
#### Operação
Para acessar a documentação completa dos métodos disponíveis da API, pode-se acessar o swagger, disponibilizado no prefixo ‘/’. Abaixo os métodos disponíveis.
 
- '/mostFolowed', '/mostFolowed/<topic>', '/mostFolowed/<int:number>', '/mostFolowed/<topic>/<int:number>': Método que retorna os usuários com mais seguidores, podemos filtrar por método e o número de usuários de retorno. 
- ‘/hashTags’: Retorna as hashtags cadastradas no banco;
- '/getByHour': Trás os número de publicações por hora do dia;
- '/getByLang', '/getByLang/<hashtag>': O número de publicações por língua, pode-se filtrar pela hashtag;
- '/getByCountry', '/getByCountry/<hashtag>': O número de publicações por localização, pode-se filtrar pela hashtag;
- '/healthcheck': Retorna ok 200;
- '/' - swagger da aplicação;

#### Melhorias
- Adicionar API-KEY;
- Fazer com que o healthcheck realize testes nos metodos;

### web-interface [WIP]
TODO
#### Operação
#### Melhorias
 
### ELK
TODO
#### Operação
#### Melhorias
 
### Deploy
TODO
#### Operação
#### Melhorias

