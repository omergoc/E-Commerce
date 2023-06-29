from fastapi import APIRouter
from api.v1.routers.user import router as v1_user_router
from api.v1.routers.product import router as v1_product_router
from api.v1.routers.order import router as v1_order_router
from api.v1.routers.auth import router as v1_auth_router
from api.v1.routers.category import router as v1_category_router


router = APIRouter()

router.include_router(v1_user_router, prefix="/v1")
router.include_router(v1_product_router, prefix="/v1")
router.include_router(v1_order_router, prefix="/v1")
router.include_router(v1_auth_router, prefix="/v1")
router.include_router(v1_category_router, prefix="/v1")
