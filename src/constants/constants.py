import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

ARTIFACT_DIR = "Artifacts"
DATA_INGESTION_DIR = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR = "feature_store"
DATA_INGESTION_INGESTED_DIR = "ingested"
TRAIN_FILE_NAME = "train.csv"
TEST_FILE_NAME = "test.csv"
FEATURE_STORE_FILE_NAME = "raw.csv"

DATA_TRANSFORMATION_DIR = "data_transformation"
DATA_TRANSFORMATION_TEST_FILE_PATH = "test.npy"
DATA_TRANSFORMATION_TRAIN_FILE_PATH = "train.npy"
DATA_TRANSFORMATION_OBJECT_FILE_PATH = "transformation_object.pkl"

MODEL_TRAINER_DIR = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_FILE_PATH = "trained_model.pkl"

PARAMS_FILE_PATH = os.path.join(ROOT_DIR, "params.yaml")