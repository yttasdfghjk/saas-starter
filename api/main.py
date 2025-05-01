from fastapi import Fastapi

app = Fastapi()

app.get("/health")
async def health_check():
    return "The Health Check is successful!!!"
