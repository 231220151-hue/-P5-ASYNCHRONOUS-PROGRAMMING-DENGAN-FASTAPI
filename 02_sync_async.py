from fastapi import FastAPI
import time
import asyncio

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Praktikum 2 - Sync vs Async"}

@app.get("/sync")
def sync_task():
    mulai = time.time()
    time.sleep(3)
    selesai = time.time()

    return {
        "jenis": "Synchronous",
        "durasi": round(selesai - mulai, 2),
        "message": "Proses synchronous selesai"
    }

@app.get("/async")
async def async_task():
    mulai = time.time()
    await asyncio.sleep(3)
    selesai = time.time()

    return {
        "jenis": "Asynchronous",
        "durasi": round(selesai - mulai, 2),
        "message": "Proses asynchronous selesai"
    }