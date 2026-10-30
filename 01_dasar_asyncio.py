import asyncio
import time

def tugas_sync(id_tugas: int, durasi: float):
    print(f"[SYNC] Tugas {id_tugas} mulai...")
    time.sleep(durasi)
    print(f"[SYNC] Tugas {id_tugas} selesai!")

def demo_sync():
    print("=== PENGUJIAN SYNCHRONOUS ===")
    mulai = time.time()

    tugas_sync(1, 1.0)
    tugas_sync(2, 1.0)
    tugas_sync(3, 1.0)

    selesai = time.time()
    print(f"Total Waktu Sync: {selesai - mulai:.2f} detik\n")

async def tugas_async(id_tugas: int, durasi: float):
    print(f"[ASYNC] Tugas {id_tugas} mulai...")
    await asyncio.sleep(durasi)
    print(f"[ASYNC] Tugas {id_tugas} selesai!")

async def demo_async():
    print("=== PENGUJIAN ASYNCHRONOUS ===")
    mulai = time.time()

    await asyncio.gather(
        tugas_async(1, 1.0),
        tugas_async(2, 1.0),
        tugas_async(3, 1.0)
    )

    selesai = time.time()
    print(f"Total Waktu Async: {selesai - mulai:.2f} detik")

if __name__ == "__main__":
    demo_sync()
    asyncio.run(demo_async())