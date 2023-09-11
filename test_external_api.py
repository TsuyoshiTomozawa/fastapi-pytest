from fastapi.testclient import TestClient
from aioresponses import aioresponses
from main import app
import pytest

client = TestClient(app)


async def fake_todo_response():
    return {"userId": 1, "id": 1, "title": "test", "completed": False}


@pytest.mark.asyncio
async def test_get_todo():
    with aioresponses() as mock_session:
        mock_session.get("https://jsonplaceholder.typicode.com/todos/1", payload=await fake_todo_response())

        response = client.get("/")

        # fake_todo_response() の実行を待機
        result = await fake_todo_response()

        assert response.status_code == 200
        assert response.json() == result
