import os

from src.entity import TrainingPipelineEntity

from src.constants.constants import DATA_INGESTION_DIR, DATA_INGESTION_FEATURE_STORE_DIR, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME, TEST_FILE_NAME, FEATURE_STORE_FILE_NAME

class DataIngestionEntity:
    def __init__(self, training_pipeline_entity: TrainingPipelineEntity):
        self.data_ingestion_dir = os.path.join(training_pipeline_entity.artifact_dir, DATA_INGESTION_DIR)
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir, DATA_INGESTION_FEATURE_STORE_DIR, FEATURE_STORE_FILE_NAME)
        self.ingested_dir_train_file_path = os.path.join(self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TRAIN_FILE_NAME)
        self.ingested_dir_test_file_path = os.path.join(self.data_ingestion_dir, DATA_INGESTION_INGESTED_DIR, TEST_FILE_NAME)

