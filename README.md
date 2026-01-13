# Automação Faz Cadastro de Produtos

Este projeto foi desenvolvido durante a [Jornada Python da Hahstag Treinamentos](https://portalhashtag.com). O objetivo principal é a criação de uma automação que realiza o login e o cadastro de produtos em um sistema web de forma automática.

## Ferramentas Utilizadas

* **Python**: Linguagem de programação principal.
* **PyAutoGUI**: Biblioteca utilizada para controlar o mouse e o teclado, automatizando as interações com a interface gráfica.
* **Pandas**: Biblioteca para manipulação e análise de dados, utilizada aqui para ler a base de dados em formato CSV.
* **Time**: Biblioteca nativa do Python para controle de intervalos e pausas durante a execução dos comandos.

## Como Funciona

O programa principal, contido no arquivo `codigo.py`, processa os dados extraídos do arquivo `produtos.csv`. Ele simula a interação humana ao clicar nos campos específicos da tela e preencher as seguintes informações:

* Código do Produto
* Marca
* Tipo
* Categoria
* Preços (Unitário e Custo)
* Anotações

## Configuração de Coordenadas

> **Aviso Importante:** Os comandos de clique baseiam-se em coordenadas geográficas da tela (eixos X e Y) que variam de acordo com a resolução do monitor. Para adaptar o código ao seu ambiente, execute o script `auxiliar.py`. Ele fornecerá os pontos exatos onde o robô deve clicar na sua tela.
