from fastapi import FastAPI
import aiohttp

app = FastAPI()


async def fetch_todo():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://jsonplaceholder.typicode.com/todos/1") as response:
            return await response.json()


@app.get("/")
async def root():
    todo = await fetch_todo()
    return todo
