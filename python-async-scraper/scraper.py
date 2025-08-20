import aiohttp
import asyncio

URLS = [
    "https://example.com",
    "https://httpbin.org/get",
    "https://jsonplaceholder.typicode.com/todos/1"
]

async def fetch(session, url):
    async with session.get(url) as resp:
        print(f"{url}: {resp.status}")
        return await resp.text()

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in URLS]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
