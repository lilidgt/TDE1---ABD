# TDE1-ABD
(lissa deguti) TDE 1 - Arquitetura de Banco de Dados (Turma 2º U) - Ciência da Computação (Noite) - 2024 / 2º Sem

# Documentação do Projeto de Banco de Dados de um Cinema

Setembro 2024

## 1 Introdução
Este documento descreve o desenvolvimento de um banco de dados para gerenciar um cinema, utilizando Python. O trabalho foi realizado como parte de um projeto acadêmico na disciplina de Arquitetura de Banco de Dados. O tema do banco de dados era de livre escolha, e optei por desenvolver um sistema para o gerenciamento de cinemas.
O objetivo principal do trabalho era implementar um banco de dados utilizando Python, de forma a criar uma aplica¸c˜ao funcional. Para isso, utilizei o framework Flask, que permitiu integrar a lógica do banco de dados com uma interface web. O banco de dados foi desenvolvido utilizando SQLAlchemy como ORM (Object-Relational Mapping) e SQLite como o sistema de banco de dados.

## 2 Tecnologias Utilizadas
### 2.1 Python e Flask
O projeto exigia o uso de Python para implementar o banco de dados. Escolhi o Flask como o framework principal para a aplicação, pois ele facilita a criação de APIs e integra bibliotecas como o SQLAlchemy. Flask é um framework minimalista e leve, ideal para pequenos projetos e protótipos, permitindo a criação rápida de rotas HTTP, manipulação de dados e geração de conteúdo dinâmico na web. Ele á popular por sua simplicidade e flexibilidade, tornando-se uma escolha viável para o desenvolvimento deste banco de dados.
Com o Flask, o servidor web foi configurado para processar solicitações do usuário e acessar o banco de dados para operações como criar, ler, atualizar e deletar (operações CRUD). Abaixo está um resumo do funcionamento básico do Flask:
#### • Rotas:
- No Flask, as rotas definem os caminhos de URL que o usuário pode acessar, como visualizar a lista de filmes ou cadastrar uma nova sala. Cada rota est´a vinculada a uma função Python que realiza uma ação específica.
### • Templates:
- Utilizei o sistema de templates do Flask para renderizar os arquivos HTML que formam a interface com o usu´ario. Esses templates são responsáveis por exibir informações do banco de dados e coletar dados via formulários.
### • SQLAlchemy:
- Este ORM foi utilizado para interagir com o banco de dados de forma simples e eficiente, mapeando classes Python para tabelas do banco de dados.
### • SQLite:
- Escolhi o SQLite por ser um sistema de banco de dados leve, ideal para este projeto acadêmico, onde os dados são armazenados localmente no arquivo cinema.db.

## 3 Estrutura do Projeto
O projeto foi organizado da seguinte forma:
### • instance/:
- Esta pasta cont´em o arquivo cinema.db, que é o banco de dados em SQLite.
### • templates/:
- Contém os arquivos HTML que formam a interface do sistema:
  -> filmes.html: Exibe a tabela com a lista de filmes cadastrados, além de botões para editar, excluir ou registrar novos filmes.
  -> salas.html: Exibe a tabela com a lista de salas cadastradas, além de botões para editar, excluir ou registrar novas salas.
  –> sessoes.html: Exibe a tabela com a lista de sessões cadastradas, além de botões para editar, excluir ou registrar novas sessões.
  –> clientes.html: Exibe a tabela com a lista de clientes cadastrados, além de botões para editar, excluir ou registrar novos clientes.
  –> filme cadastro.html: Formulário para registrar um novo filme, solicitando informações: título, gênero, duração e classificação.
  –> sala cadastro.html: Formulário para registrar uma nova sala, solicitando informaçõess: nome e capacidade.
  –> sessao cadastro.html: Formulário para registrar uma nova sessão, solicitando informações: dia, mês e ano, horário, filme e sala.
  –> cliente cadastro.html: Formulário para registrar um novo cliente, solicitando informações: nome e email.
  –> update filme.html: Formulário para editar os dados de um filme já cadastrado.
  –> update sala.html: Formulário para editar os dados de uma sala já cadastrada.
  –> update sessao.html: Formulário para editar os dados de uma sessão já cadastrada.
  –> update cliente.html: Formulário para editar os dados de um cliente já cadastrado.

## 4 Entidades
As quatro entidades do sistema de banco de dados são:
### • Filme:
- Representa os filmes que estão disponíveis para exibição no cinema. Cada filme possui atributos: título, duração, gênero e classificação.
### • Sala:
- Representa as salas de cinema onde os filmes são exibidos. Cada sala possui atributos: nome e capacidade.
### • Sessão:
- As sessões conectam um filme a uma sala em uma determinada data, criando a relação entre quando e onde o filme será exibido.
### • Cliente:
- Representa os clientes do cinema, armazenando informações de nome e e-mail.

## 5 Funcionamento do Sistema
O sistema desenvolvido permite ao usuário interagir com o banco de dados de maneira simples, através de uma interface web que foi projetada com o auxílio do Flask e do SQLAlchemy. As principais funcionalidades do sistema incluem:
### • Listagem de filmes, salas, sessões e clientes:
O usuário pode visualizar os dados das quatro entidades principais em tabelas HTML.
### • Cadastro de novos filmes, salas e sess˜oes:
Através de formulários em HTML, o usuário pode inserir novos registros no banco de dados.
### • Edição e exclusão de registros:
A interface oferece bot˜oes para editar ou excluir filmes, salas e sessões existentes.
### • Validação de dados:
A entrada de dados nos formulários é validada para garantir que não ocorra repetição de informação (além da verificação da pré-existência de alguns dados como pré-requisito para registro de novos dados).
Cada uma dessas operações é realizada por meio de rotas específicas no Flask, que recebem as solicitações do usuário, processam os dados e interagem com o banco de dados por meio do SQLAlchemy.
O uso do Flask foi fundamental para facilitar a criação da interface web e a gestão das rotas, permitindo um fluxo contínuo de informalções entre o frontend e o banco de dados. A simplicidade e flexibilidade oferecidas por essas tecnologias tornaram possível a implementação de um sistema funcional.

## 6 Obrigada
Esse projeto foi finalizado gra¸cas a ajuda do meu colega Eduardo, que me apresentou o framework Flask e me instruiu em sua utilização.
