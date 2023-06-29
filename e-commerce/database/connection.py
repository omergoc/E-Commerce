import motor.motor_asyncio

# MongoDB bağlantısı
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
database = client["e_ticaret_db"]
