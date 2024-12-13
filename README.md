# ATV-DJANGO-GRUPO
# 📚 Sistema de Gestão Escolar

Este é um projeto de um **Sistema de Gestão Escolar** desenvolvido com o framework Django. O sistema inclui funcionalidades completas de CRUD para Alunos, Professores, Disciplinas, Turmas, Notas e Frequências. Além disso, possui autenticação de usuários, templates extensíveis e estilização com CSS e JavaScript.


## 🎯 Como Executar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/c4milafeitosa/sistema-escolar.git
   cd sistema-escolar
   ```

2. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/Mac
   venv\Scripts\activate # Windows
   ```

4. **Configure o banco de dados**:
   ```bash
   python manage.py migrate
   ```

5. **Crie um superusuário**:
   ```bash
   python manage.py createsuperuser
   ```

6. **Execute o servidor**:
   ```bash
   python manage.py runserver
   ```

7. **Acesse o sistema**:
   - Página inicial: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - Área administrativa: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 👩‍💻 Contribuidores

- Camila Feitosa - Configuração inicial e autenticação.
- Brenda Leticia - CRUD de Alunos e Professores.
- Nataly Pereira - CRUD de Disciplinas e Turmas.
- Mirela Aquino - CRUD de Notas e Frequências, integração de CSS e JavaScript.
