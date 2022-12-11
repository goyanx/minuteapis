from fastapi import FastAPI, Request
from pydantic import BaseModel
import uvicorn
from allennlp.predictors.predictor import Predictor
import allennlp_models.rc

app = FastAPI()


class APIRequest(BaseModel):
    passage: str
    question: str


@app.on_event("startup")
def load_model():
    global predictor
    predictor = Predictor.from_path(
        "https://storage.googleapis.com/allennlp-public-models/bidaf-elmo.2021-02-11.tar.gz")


@app.get("/api")
async def get_analysis(p: str = 'Peter Sullivan is an associate in the Risk Assessment and Management Office at MBS', q: str = 'what is the problem ?'):
    results = predictor.predict(passage=p, question=q)
    return {"answer": results}


@app.post("/api")
async def get_analysisPost(data: APIRequest):
    results = predictor.predict(passage=data.passage, question=data.question)
    return {"answer": results}

if __name__ == "__main__":
    uvicorn.run(app, debug=True)
