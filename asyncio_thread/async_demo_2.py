import asyncio


async def fetch_data():
    print("start fetching")
    await asyncio.sleep(2)
    print('fetching finished')
    return {'Data': 1}


async def main():
    task1 = asyncio.create_task(fetch_data())


if __name__ == "__main__":
    asyncio.run(main())