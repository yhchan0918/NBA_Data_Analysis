import joblib
import uvicorn
import numpy as np
import pandas as pd
from pydantic import BaseModel

# FastAPI libray
from fastapi import FastAPI, UploadFile, File

# Initiate app instance
app = FastAPI(
    title="NBA Games Analytics",
    version="1.0",
    description="Logistic Regression model is used for prediction",
)

# Initialize model artifacte files. This will be loaded at the start of FastAPI model server.
scaler = joblib.load("./model/scaler.joblib")
model = joblib.load("./model/model.joblib")

# This struture will be used for Json validation.
# With just that Python type declaration, FastAPI will perform below operations on the request data
## 1) Read the body of the request as JSON.
## 2) Convert the corresponding types (if needed).
## 3) Validate the data. If the data is invalid, it will return a nice and clear error,
##    indicating exactly where and what was the incorrect data.
class Data(BaseModel):
    G_home: float
    W_PCT_home: float
    HOME_RECORD_home: float
    ROAD_RECORD_home: float
    W_PCT_prev_home: float
    HOME_RECORD_prev_home: float
    ROAD_RECORD_prev_home: float
    G_away: float
    W_PCT_away: float
    HOME_RECORD_away: float
    ROAD_RECORD_away: float
    W_PCT_prev_away: float
    HOME_RECORD_prev_away: float
    ROAD_RECORD_prev_away: float
    WIN_PRCT_home_3g: float
    PTS_home_3g: float
    FG_PCT_home_3g: float
    FT_PCT_home_3g: float
    FG3_PCT_home_3g: float
    AST_home_3g: float
    REB_home_3g: float
    WIN_PRCT_away_3g: float
    PTS_away_3g: float
    FG_PCT_away_3g: float
    FT_PCT_away_3g: float
    FG3_PCT_away_3g: float
    AST_away_3g: float
    REB_away_3g: float
    WIN_PRCT_home_10g: float
    PTS_home_10g: float
    FG_PCT_home_10g: float
    FT_PCT_home_10g: float
    FG3_PCT_home_10g: float
    AST_home_10g: float
    REB_home_10g: float
    WIN_PRCT_away_10g: float
    PTS_away_10g: float
    FG_PCT_away_10g: float
    FT_PCT_away_10g: float
    FG3_PCT_away_10g: float
    AST_away_10g: float
    REB_away_10g: float


# Api root or home endpoint
@app.get("/")
def read_home():
    """
     Home endpoint which can be used to test the availability of the application.
     """
    return {"message": "System is healthy"}


# ML API endpoint for making prediction aganist the request received from client
@app.post("/predict")
def predict(data: Data):
    # Extract data in correct order
    data_dict = data.dict()
    # Scale data
    data_df = pd.DataFrame.from_dict([data_dict])
    data_df = scaler.transform(data_df)
    # Create prediction
    prediction = model.predict(data_df)
    # Map prediction to appropriate label

    prediction_label = [
        "Home Team Will Win" if label == 1 else "Away Team Will Win" for label in prediction
    ]
    # Return response back to client
    return {"prediction": prediction_label}

