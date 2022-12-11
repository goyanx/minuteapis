from fastapi import FastAPI, Request
import logging
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api")
async def get_analysis(p: str = 'Peter Sullivan is an associate in the Risk Assessment and Management Office at MBS'):
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)
