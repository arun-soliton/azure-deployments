from fastapi import FastAPI
import uvicorn
from datetime import datetime
import httpx
from config import settings
from qdrant_client import QdrantClient

app = FastAPI()
start_time = datetime.utcnow()


@app.get("/")
async def health_check():

    current_time = datetime.utcnow()
    server_uptime = (current_time - start_time).total_seconds()
    hours = int(server_uptime // 3600)
    minutes = int((server_uptime % 3600) // 60)
    seconds = int(server_uptime % 60)
    uptime_in_hours = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    return {"status": "ok", "uptime": uptime_in_hours}


@app.get("/qdrant-test")
async def qdrant_test():

    try:
        url = f"http://{settings.QDRANT_URL}"
        client = QdrantClient(
            url=url,
            port=settings.QDRANT_PORT,
            api_key=settings.QDRANT_PASSWORD,
        )

        collections_available = client.get_collections()
        return {"qdrant_status": "reachable", "collections": collections_available}
    except Exception as e:
        return {"qdrant_status": "unreachable", "error": str(e)}


@app.get("/neo4j-test")
async def neo4j_test():

    try:
        neo4j_url = f"http://{settings.NEO4J_URL}:{settings.NEO4J_PORT}"
        async with httpx.AsyncClient() as client:
            response = await client.get(
                neo4j_url, auth=(settings.NEO4J_USERNAME, settings.NEO4J_PASSWORD)
            )

            if response.status_code == 200:
                return {
                    "neo4j_status": "reachable",
                    "status_code": response.status_code,
                    "text": response.json() if response else "",
                }
            else:
                return {
                    "neo4j_status": "unreachable",
                    "status_code": response.status_code,
                }
    except Exception as e:
        import traceback

        traceback.print_exc()
        return {"neo4j_status": "unreachable", "error": str(e)}


if __name__ == "__main__":
    uvicorn.run(app, host=settings.APP_HOST, port=settings.APP_PORT)
