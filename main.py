from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import api as api_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="./templates/static"), name="static")
templates = Jinja2Templates(directory="./templates")

origins = ["https://localhost:5500", "https://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

@app.get("/")
def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard/{user_id}")
def dashboard(request : Request, user_id : int):
    return templates.TemplateResponse("dashboard.html", {"request": request, "user_id": user_id})

app.include_router(api_router.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload_includes=["*.html", "*.css", "*.js"],
        reload_excludes=["./node_modules"],
        reload_dirs=["./templates", "./templates/static"],
        reload=True,
    )
