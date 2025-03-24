# Bootcamp API - Usando Python com Flask

Projeto desenvolvido para disciplina de `Bootcamp Desenvolvimento e Projetos de Sistema` pelo `Grupo 1`


## Pré Requisitos
- [Git](https://git-scm.com/downloads) - Para baixar o projeto e fazer o versionamento do código
- [Python 3.12+](https://www.python.org/downloads/) - Executa o código
- [Visual Studio Code](https://code.visualstudio.com/download) - IDE para desenvolvimento "Recomendada pelo grupo"
- [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) - Para rodar a aplicação dentro de um container e garantir ambiente estável
- [Docker Compose](https://docs.docker.com/compose/) - Para facilitar a criação de container. Geralmente já vem com o Docker Desktop mas se não estiver instalado busque na documentação

## Baixar o projeto para sua máquina local

Clonar o repositório para sua máquina local
```bash
git clone https://github.com/vinilima2/bootcamp-api-python-flask
```

Acessar o diretório do projeto
```bash
cd bootcamp-api-python-flask
```

<br/>

## Como rodar o projeto
OBS: Todos os seguintes comandos estão sendo executados dentro da pasta do projeto - `bootcamp-api-python-flask`

### Docker - Windows
Para criar o container e executar a aplicação. Caso não queira que ela execute em segundo plano adicione `-d` ao final do comando
```bash
# Criar uma nova imagem e subir ela em um container
docker-compose.exe up --build
```

Para parar o container ou remover a imagem e o container
```bash
docker-compose.exe down
```

<br/>

### Linux ou Git - Bash
Baixar as dependências do projeto
```bash
# Instalar dependências
pip install -r requirements.txt
```

Rodar o script para iniciar o programa junto da configuração da base de dados
```bash
# Executar projeto
./run.sh
```

<br/>

### Windows - CMD ou Powershell
Por meio do CMD ou Powershell que podem ser acessados pelo terminal rode os seguintes comandos
```bash
# Instalar dependências
pip install -r requirements.txt
```
> Importante analisar o código do script para entender os comandos executados, o mesmo comando pode ser rodado diretamente pelo terminal

Rodar o script para iniciar o programa junto da configuração da base de dados
```bash
# Executar projeto
./run.sh
```
> Importante analisar o código do script para entender os comandos executados, o mesmo comando pode ser rodado diretamente pelo terminal

Lembrando que também é possível rodar o comando da seção [Linux ou Git](#linux-ou-git---bash) basta ter instalado o Git com o Git Bash.