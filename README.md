# 🚗 Sistema de Locadora de Veículos

Um sistema web desenvolvido em **Python** com a framework **Django** para a gestão e apresentação de veículos de uma locadora. Este projeto esta sendo construído como parte da disciplina de WebMobile e foca-se numa interface limpa e responsiva.

## 🛠️ Tecnologias Utilizadas

* **Backend:** Python e Django
* **Frontend:** HTML5, CSS3, e Bootstrap 5 (para um design responsivo e moderno)
* **Base de Dados:** SQLite (padrão do Django, ideal para desenvolvimento)
* **Ambiente e Deploy:** Suporte a virtual environment (venv) e Docker (inclui `Dockerfile`)

## ✨ Funcionalidades Atuais

* **Autenticação Segura:** Sistema de login para utilizadores através de nome de utilizador e palavra-passe.
* **Catálogo de Veículos:** Listagem dinâmica dos veículos disponíveis na base de dados, apresentando a marca/modelo, ano e o valor da diária.
* **Painel Administrativo:** Acesso ao painel nativo do Django (`/admin`) para adicionar, editar ou remover veículos facilmente.

## 🚀 Como executar o projeto localmente

Siga os passos abaixo para ter o projeto a funcionar na sua máquina.

### Pré-requisitos
* Python 3.x instalado
* Git instalado

### Passo a Passo

1. **Clone este repositório:**
   ```bash
   git clone [https://github.com/math3us-sousa/LocadoraVeiculos.git](https://github.com/math3us-sousa/LocadoraVeiculos.git)

2. **Navegue até à pasta do projeto:**
   ```bash
   cd LocadoraVeiculos
   ```

3. **Crie e ative o ambiente virtual:**
   * Em sistemas Linux/macOS:
     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Navegue para a diretoria do sistema e prepare a base de dados:**
   ```bash
   cd sistema
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crie um superutilizador (para aceder ao painel de administração e adicionar carros):**
   ```bash
   python manage.py createsuperuser
   ```

7. **Inicie o servidor local:**
   ```bash
   python manage.py runserver
   ```

8. **Aceda no navegador:**
   * A aplicação estará disponível em: `http://127.0.0.1:8000/`
   * Para adicionar veículos ao banco, aceda a: `http://127.0.0.1:8000/admin` e faça login com o superutilizador criado no passo 6.

## 🐳 Como executar com Docker (Opcional)
Se preferir utilizar contentores, o projeto já possui o ficheiro configurado:
```bash
docker build -t locadora_veiculos .
docker run -p 8000:8000 locadora_veiculos

***
