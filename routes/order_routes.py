from fastapi import APIRouter

order_router = APIRouter(prefix="/order", tags=["oerder"])

#@order_router.(requisição)
#decorator coloca antes da funçao que atribui uma funcionalidade nova a essa funçao que esta criando
@order_router.get("/")
async def pedidos():
    return {"menssagem": "Você acessou a rota de pedidos!!."}

@order_router.get("/teste")
async def teste():
    return {"menssagem": "Você teste com sucesso!!."}