import asyncio
import time

async def tugas_buruk(id_tugas):
    print(f"[BURUK] Tugas {id_tugas} mulai")
    time.sleep(2)
    print(f"[BURUK] Tugas {id_tugas} selesai")

async def tugas_baik(id_tugas):
    print(f"[BAIK] Tugas {id_tugas} mulai")
    await asyncio.sleep(2)
    print(f"[BAIK] Tugas {id_tugas} selesai")

async def demo_buruk():
    print("=== ANTI-PATTERN: time.sleep() ===")
    mulai = time.time()

    await asyncio.gather(
        tugas_buruk(1),
        tugas_buruk(2),
        tugas_buruk(3)
    )

    print(f"Total waktu buruk: {time.time() - mulai:.2f} detik\n")

async def demo_baik():
    print("=== SOLUSI: asyncio.sleep() ===")
    mulai = time.time()

    await asyncio.gather(
        tugas_baik(1),
        tugas_baik(2),
        tugas_baik(3)
    )

    print(f"Total waktu baik: {time.time() - mulai:.2f} detik")

async def main():
    await demo_buruk()
    await demo_baik()

if __name__ == "__main__":
    asyncio.run(main())