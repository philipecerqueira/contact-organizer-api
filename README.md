# Contact Organizer API

Este projeto fornece uma API para gerenciar contatos, autenticando-se com o Google e permitindo que o usuário acesse seus contatos através da API do Google.

## Requisitos

- Python 3.12 ou superior
- PDM (Python Development Master) instalado para gerenciar dependências.

## Instalação e Inicialização

### 1. Clone o repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/contact-organizer-api.git
cd contact-organizer-api
```

### 2. Instale o PDM

Caso não tenha o PDM instalado, você pode instalá-lo com o seguinte comando:

```bash
pip install pdm
```

### 3. Instale as dependências

Com o PDM instalado, execute o seguinte comando para instalar as dependências do projeto:

```bash
pdm install
```

### 4. Configuração das Variáveis de Ambiente

Crie um arquivo .env no diretório raiz do projeto e adicione as variáveis de ambiente necessárias:

```env
GOOGLE_CLIENT_ID=seu-client-id
GOOGLE_CLIENT_SECRET=seu-client-secret
SECRET_KEY=sua-secret-key
FLASK_APP=app.main:create_app
```

### 5. Inicie o Servidor

Após instalar as dependências e configurar as variáveis de ambiente, inicie o servidor com o comando abaixo:

```bash
pdm run flask run
```

## Testando o Projeto

### 1. Endpoint /api/auth/login

Este endpoint redireciona o usuário para o Google para autenticação.

**Método**: GET

**Exemplo de uso**: Acesse `http://localhost:5000/api/auth/login` no navegador para iniciar o processo de login com o Google.

---

### 2. Endpoint /api/auth/callback

Após o login no Google, o Google redireciona para este endpoint com o código de autorização, que será trocado por um token de acesso.

**Método**: GET

**Exemplo de uso**: Este endpoint é chamado automaticamente após a autenticação no Google. Não é necessário chamar manualmente.

---

### 3. Endpoint /api/auth/logout

Este endpoint permite que o usuário faça logout, removendo o token de acesso da sessão.

**Método**: GET

**Exemplo de uso**: Acesse `http://localhost:5000/api/auth/logout` para sair da aplicação.

---

### 4. Endpoint /api/contact/

Este endpoint retorna os contatos do usuário autenticado.

**Método**: GET

**Exemplo de uso**: Acesse `http://localhost:5000/api/contact/` para obter todos os contatos do usuário autenticado.
