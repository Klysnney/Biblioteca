# Biblioteca API

A API da Biblioteca é um sistema simples para gerenciar informações sobre livros, autores e anos de publicação. Esta API permite a criação, leitura, atualização e exclusão de informações sobre livros.

## Configuração

Antes de começar a usar a API, certifique-se de que você tenha o Python instalado em seu ambiente. Além disso, você precisará das seguintes bibliotecas:

- Flask
- Flask-RESTful
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-Marshmallow

Você pode instalar essas dependências com o seguinte comando:

```bash
pip install Flask Flask-RESTful Flask-SQLAlchemy Flask-Migrate Flask-Marshmallow
```

## Configuração do Banco de Dados

Certifique-se de ter um servidor MySQL em execução em sua máquina ou em um local acessível. Você precisará configurar as variáveis de ambiente no arquivo `config.py` para se conectar ao seu banco de dados. Aqui estão as configurações padrão:

```python
DEBUG = True
USERNAME = "root"
PASSWORD = "Everton12"
SERVER = "localhost"
DB = "biblioteca"
SQLALCHEMY_DATABASE_URI = f'mysql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
```

Você deve adaptar essas configurações de acordo com o seu ambiente.

## Uso

Depois de configurar seu ambiente e banco de dados, você pode executar a API com o seguinte comando:

```bash
python run.py
```

A API estará acessível em `http://localhost:5001`.

## Endpoints

### GET /biblioteca

- Descrição: Obtém a lista de todos os livros na biblioteca.
- Resposta: Uma lista de objetos JSON, onde cada objeto representa um livro.

### GET /biblioteca/<int:id>

- Descrição: Obtém informações detalhadas sobre um livro específico com base no ID.
- Resposta: Um objeto JSON que representa o livro ou uma mensagem de erro se o livro não for encontrado.

### POST /biblioteca

- Descrição: Adiciona um novo livro à biblioteca.
- Parâmetros de Solicitação: Deve incluir dados sobre o livro, autor e ano de publicação no corpo da solicitação em formato JSON.
- Resposta: Um objeto JSON que representa o livro recém-adicionado.

### PUT /biblioteca/<int:id>

- Descrição: Atualiza as informações de um livro existente com base no ID.
- Parâmetros de Solicitação: Deve incluir os dados atualizados do livro, autor e ano de publicação no corpo da solicitação em formato JSON.
- Resposta: Um objeto JSON que representa o livro atualizado ou uma mensagem de erro se o livro não for encontrado.

### DELETE /biblioteca/<int:id>

- Descrição: Exclui um livro da biblioteca com base no ID.
- Resposta: Uma mensagem de confirmação ou uma mensagem de erro se o livro não for encontrado.

## Contribuindo

Sinta-se à vontade para contribuir para este projeto. Você pode abrir problemas (issues) ou enviar solicitações de pull (pull requests) para melhorar a API.

## Licença

Este projeto é licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
