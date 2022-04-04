import asyncio


async def fetch_data():
    print("start fetching")


async def main():
    task1 = asyncio.create_task(fetch_data())

    
if __name__ == "__main__":
    asyncio.run(main())