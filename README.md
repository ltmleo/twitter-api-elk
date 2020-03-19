# Twitter API
Esse projeto mostra de maneira simplificada o funcionamento de um ecossistema de microsserviçios. E contem principlamente 4 componentes: 
- Uma aplicação python agendada para rodar de hora em hora que salva informaçãos adquridas com a API do twitter em um banco de dados não relacional (mongoDB);
- API REST para realizar consultas ao banco, desenvolvida em Flask;
- Iinterface Web para consumir esta API desenvolvida em FLask;
- Stack de monitoração, logging e APM (elastic) para acompanhar o desenmpenho do sistema desenvolvido.

Além disso, visando auto scalabilidade e facilidadade no deploy, foram utilizadas as ferramentas Helm e Kubernetes.

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
 Responsavél por alimentar o banco de dados, esse componente é agendado para rodar de uma e uma hora consumindo determinadas **#hashtags**, listadas abaixo:
 - "#openbanking", "#apifirst", "#devops", #cloudfirst", "#microservices", "#apigateway",  "#oauth", "#swagger", "#raml" e "#openapis".
 
 
 e salvando as seguintes informações de cada tweet:
 
 - user: username do usuiaro;
 - followers: Quantidade de seguidores do usuario;
 - date: Data em que o tweet foi publicado;
 - language: Lingua em que o tweet foi publicado;
 - countrt: Localização em que o tweet foi publicado;
 
 
#### Operação
 Para rodar essa aplicação é necessario exportar como variavel de ambiente a variavél **PASSWORD**, à qual irá descriptografar as secrets e tokens da API do twitter.
 
#### Melhorias
 - Colocar a variável PASSWORD como uma secret no kubernetes;
 - Colocar o atribulo salt da classe Crypt como um secret no kubernetes;
 - Ler de um configmap as hashtgas pela qual o programa deve iterar;
 -  Modificar a maneira com o qual o logstash acessa os logs da aplicação;
 -  Adicionar autenticação ao acessod o mognoDB;
 
### get-tweets-api 
 Responsável por consumir as informações no banco de dados e export em forma de uma API RESTFULL. Como está API foi pensada apenas para consumir os dados dos banco, apenas o metodo GET está disponível. O swagger da aplicação está disponivel no prefixo "/" da aplicação.
#### Operação
#### Melhorias

### web-interface
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