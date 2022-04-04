#await to let other coroutine to run, create_task to add a corotine
import asyncio
import time

async def sub(text):
    print(text)
    print(time.perf_counter())
    await asyncio.sleep(3)

async def main():
    print("hello main")
    print(time.perf_counter())
    # await will halt current object to let this to run first
    # await sub('stop main wait sub routine to finish')
    # this will let python to know async.io start as soon as possible
    task = asyncio.create_task(sub('Second'))
    # await task  # this will halt until task is done, same as await sub, do not use
    await asyncio.sleep(0)
    print('finish main')
    print(time.perf_counter())


if __name__ == "__main__":
    print("main start now")
    print(time.perf_counter())
    asyncio.run(main())  # this create a event loop to run