```bash
# Subir a aplicação
$ docker-compose up --build

# Gerar migração inicial
$ docker-compose run api alembic revision --autogenerate -m "cria tabelas"

# Aplicar migração
$ docker-compose run api alembic upgrade head
```

Pronto! Agora é só rodar via Docker que a API estará disponível em http://localhost:8000/docs
