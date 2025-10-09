from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Раздача статических файлов (изображения, видео и т.д.)
# Монтируем текущую директорию для доступа к файлам
app.mount("/static", StaticFiles(directory="."), name="static")

@app.get("/")
async def read_index():
    """Главная страница"""
    return FileResponse("index.html")

# Обработка запросов к файлам напрямую (без /static/)
@app.get("/{file_path:path}")
async def serve_file(file_path: str):
    """
    Раздача любых файлов из корневой директории.
    Это позволяет обращаться к файлам напрямую, например /logo2.png
    """
    if os.path.exists(file_path):
        return FileResponse(file_path)
    # Если файл не найден, возвращаем 404
    return {"error": "File not found"}, 404

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=5500)

