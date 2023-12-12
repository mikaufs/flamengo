# Avaliação -- Programação para Internet - 3º bimestre.

Sistema de controle de discos

## Funcionalidades 
- O projeto conta com toda a estrutura de crud de discos pronta. Além disso, já vem com o template de login.


## Instalação

Baixe o projeto do github:

```sh
git clone git@github.com:irlanarley/prova-pi-3-bimestre.git
```

ou 

```sh
git clone https://github.com/irlanarley/prova-pi-3-bimestre.git
```

### Passos para instalação

1. Entre na pasta do projeto
```sh
cd prova-pi-3-bimestre
```
2. Crie um ambiente virtual
```sh
python -m venv venv
```
3. Ative o ambiente virtual
```sh
# Windows
venv\Scripts\activate

# Unix or MacOS
source venv/bin/activate
```
4. Instale as dependências do projeto
```sh
pip install -r requirements.txt
```

7. Inicie o servidor
**Obs.: Não faça as migrações. O banco de dados já está populado.**
```sh
python manage.py runserver
```

