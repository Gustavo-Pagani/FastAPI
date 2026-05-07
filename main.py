from fastapi import FastAPI

app = FastAPI()

from routes.auth_routes import auth_router
from routes.order_routes import order_router

app.include_router(auth_router)
app.include_router(order_router)

# para rodar o nosso código, executar no terminal: uvicorn main:app --reload

#para fazer migraçao do banco de dados: alembic revision --autogenerate -m "adiciona campos no usuario"
#depois : alembic upgrade head

# endpoint:
# dominio.com/pedidos


# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> edição
# Delete -> deletar