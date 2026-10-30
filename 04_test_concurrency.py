import asyncio
import time

async def tugas(id_tugas, durasi):
    print(f"Tugas {id_tugas} dimulai")
    await asyncio.sleep(durasi)
    print(f"Tugas {id_tugas} selesai")

async def test_sequential():
    print("\n=== PENGUJIAN SEQUENTIAL ===")
    mulai = time.time()

    await tugas(1, 2)
    await tugas(2, 2)
    await tugas(3, 2)

    print(f"Total waktu: {time.time() - mulai:.2f} detik")

async def test_concurrent():
    print("\n=== PENGUJIAN CONCURRENT ===")
    mulai = time.time()

    await asyncio.gather(
        tugas(1, 2),
        tugas(2, 2),
        tugas(3, 2)
    )

    print(f"Total waktu: {time.time() - mulai:.2f} detik")

async def main():
    await test_sequential()
    await test_concurrent()

if __name__ == "__main__":
    asyncio.run(main())