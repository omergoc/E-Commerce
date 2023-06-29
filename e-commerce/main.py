from fastapi import FastAPI
from api.v1.routers import user as v1_user_router
from api.v1.routers import product as v1_product_router
from api.v1.routers import order as v1_order_router
from api.v1.routers import auth as v1_auth_router
from api.v1.routers import category as v1_category_router


app = FastAPI(title="Bigital E-Ticaret API")

# Endpoint'ler ve diğer kodlar...

# API sürümleri için yönlendiricileri ekleyin
app.include_router(v1_auth_router.router, prefix="/api/v1", tags=["Auth"])
app.include_router(v1_user_router.router, prefix="/api/v1", tags=["User"])
app.include_router(v1_product_router.router, prefix="/api/v1", tags=["Product"])
app.include_router(v1_order_router.router, prefix="/api/v1", tags=["Order"])
app.include_router(v1_category_router.router, prefix="/api/v1", tags=["Category"])


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
