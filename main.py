from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount("/static", StaticFiles(directory="./templates/static"), name="static")
templates = Jinja2Templates(directory="./templates")

origins = ["https://localhost:5500", "https://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def index(request : Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard/{id}")
def dashboard(request : Request, id : int):
    return templates.TemplateResponse("dashboard.html", {"request": request, "id": id})

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
