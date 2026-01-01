import pandas as pd
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run as app_run

from src.utils.utils import process_comment, load_object

from src.entity.input_entity.data_transformation_entity import DataTransformationEntity
from src.entity.input_entity.model_trainer_entity import ModelTrainerEntity
from src.entity import TrainingPipelineEntity

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

training_pipeline_entity = TrainingPipelineEntity()
data_transformation_entity = DataTransformationEntity(training_pipeline_entity=training_pipeline_entity)
model_trainer_entity = ModelTrainerEntity(training_pipeline_entity=training_pipeline_entity)

class Payload(BaseModel):
    comment: str

@app.post('/predict')
async def predict_sentiment(payload: Payload):
    comment = payload.comment
    # process the comment
    processed_comment = process_comment(comment=comment)
    # load transformation object
    transformation_object_file_path = data_transformation_entity.data_transformation_object_file_path
    transformation_object = load_object(file_path=transformation_object_file_path)

    # convert comment to vectorized form
    data = {'clean_comment': [processed_comment]}
    df = pd.DataFrame(data)
    vectorized_comment = transformation_object.transform(df['clean_comment'].values)
    prediction_arr = vectorized_comment.toarray()

    # load model 
    trained_model_file_path = model_trainer_entity.trained_model_file_path
    model = load_object(file_path=trained_model_file_path)
    # make prediction
    prediction = model.predict(prediction_arr)
    return prediction[0]


if __name__ == "__main__":
    app_run(app, host="0.0.0.0", port=8000)
