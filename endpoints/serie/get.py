from fastapi.responses import JSONResponse
from fastapi import Form

from src import App, Endpoint, Method

class GetSerie(Endpoint):

    async def callback(self, id: int = Form()) -> JSONResponse:

        async with self.app.pool.acquire() as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT id FROM Serie WHERE id = %s", (id,))
                if not await cursor.fetchone():
                    return JSONResponse({"error": "This serie does not exist."}, 400)
                await cursor.execute("SELECT FROM Serie WHERE id = %s", (id,))
                return JSONResponse({})
            
def setup(app : App) -> GetSerie:
    return GetSerie(app, Method.GET, "/serie/get", JSONResponse)