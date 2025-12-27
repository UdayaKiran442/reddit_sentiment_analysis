import os
from datetime import datetime

from src.constants.constants import ARTIFACT_DIR, DATA_INGESTION_DIR, DATA_INGESTION_FEATURE_STORE_DIR, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME, TEST_FILE_NAME, FEATURE_STORE_FILE_NAME, DATA_TRANSFORMATION_DIR, DATA_TRANSFORMATION_TEST_FILE_PATH, DATA_TRANSFORMATION_TRAIN_FILE_PATH, DATA_TRANSFORMATION_OBJECT_FILE_PATH

class TrainingPipelineEntity:
    def __init__(self, timestamp = datetime.now()):
        timestamp=timestamp.strftime("%m_%d_%Y_%H_%M_%S")
        self.artifact_name = ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name, timestamp)

class DataIngestionEntity:
    def __init__(self, training_pipeline_entity: TrainingPipelineEntity):
        self.data_ingestion_dir = os.path.join(training_pipeline_entity.artifact_dir, DATA_INGESTION_DIR)
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FEATURE_STORE_FILE_NAME)
        self.ingested_dir_train_file_path = os.path.join(self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
        self.ingested_dir_test_file_path = os.path.join(self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)

class DataTransformationEntity:
    def __init__(self, training_pipeline_entity: TrainingPipelineEntity):
        self.data_transformation_dir = os.path.join(training_pipeline_entity.artifact_dir, DATA_TRANSFORMATION_DIR)
        self.data_transformation_train_file_path = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TRAIN_FILE_PATH)
        self.data_transformation_test_file_path = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TEST_FILE_PATH)
        self.data_transformation_object_file_path = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_OBJECT_FILE_PATH)
