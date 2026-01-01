import os

from src.entity import TrainingPipelineEntity

from src.constants.constants import  MODEL_TRAINER_DIR, MODEL_TRAINER_TRAINED_MODEL_FILE_PATH

class ModelTrainerEntity:
    def __init__(self, training_pipeline_entity: TrainingPipelineEntity):
        self.model_trainer_dir = os.path.join(training_pipeline_entity.artifact_dir, MODEL_TRAINER_DIR)
        self.trained_model_file_path = os.path.join(self.model_trainer_dir, "model", MODEL_TRAINER_TRAINED_MODEL_FILE_PATH)