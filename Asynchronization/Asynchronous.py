import asyncio
import time


async def f1():
    print("f1 starting...")
    await asyncio.sleep(3)  # non-blocking delay
    print("f1 done")
    return 10


async def f2():
    print("f2 starting...")
    await asyncio.sleep(3)  # non-blocking delay
    print("f2 done")
    return 20


async def main():
    start_time = time.time()

    task1 = asyncio.create_task(f1())
    task2 = asyncio.create_task(f2())

    x = await task1
    y = await task2

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"x: {x}, y: {y}")
    print(f"elapsed_time: {elapsed_time}") # 3s


if __name__ == "__main__":
    asyncio.run(main())