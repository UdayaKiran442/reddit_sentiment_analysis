import os

from src.entity import TrainingPipelineEntity

from src.constants.constants import DATA_TRANSFORMATION_DIR, DATA_TRANSFORMATION_TEST_FILE_PATH, DATA_TRANSFORMATION_TRAIN_FILE_PATH, DATA_TRANSFORMATION_OBJECT_FILE_PATH


class DataTransformationEntity:
    def __init__(self, training_pipeline_entity: TrainingPipelineEntity):
        self.data_transformation_dir = os.path.join(training_pipeline_entity.artifact_dir, DATA_TRANSFORMATION_DIR)
        self.data_transformation_train_file_path = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TRAIN_FILE_PATH)
        self.data_transformation_test_file_path = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_TEST_FILE_PATH)
        self.data_transformation_object_file_path = os.path.join(self.data_transformation_dir, DATA_TRANSFORMATION_OBJECT_FILE_PATH)