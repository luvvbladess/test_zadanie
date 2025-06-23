from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def hello(
    name: str = Query("Recruto", min_length=1),
    message: str = Query("Давай дружить", min_length=1)
):
    return f"Hello {name}! {message}"
