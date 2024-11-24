from fastapi import FastAPI, Form, Request 
from fastapi.responses import HTMLResponse 
from fastapi.exceptions import HTTPException 
from fastapi.templating import Jinja2Templates 
import random 
from fastapi.staticfiles import StaticFiles

app = FastAPI() 
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")
# Simulated database (key: URL, value: Text)
data_store = {}
# List of words for URL generation
word_list = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi", "lemon", "mango", "peach"]
# Generate a unique URL
def generate_url(): 
    return f"{random.choice(word_list)}-{random.choice(word_list)}"
@app.get("/", response_class=HTMLResponse) 
def home(request: Request):
    """ Home page with a form to submit text. """ 
    return templates.TemplateResponse("home.html", {"request": request})
@app.post("/submit", response_class=HTMLResponse)
def submit_text(request: Request, text: str = Form(...)):
    """ Submit text and generate a unique URL for it. """ 
    url = generate_url()
    # Save the text to the data store, overwriting if the 
    # URL already exists
    data_store[url] = text 
    return templates.TemplateResponse("success.html", {"request": request, "url": url})
@app.get("/{url}", response_class=HTMLResponse) 
def view_text(request: Request, url: str):
    """ View the text associated with a given URL. """ 
    text = data_store.get(url) 
    if not text:
        raise HTTPException(status_code=404, detail="URL not found")
    return templates.TemplateResponse("view.html", {"request": request, "text": text})
