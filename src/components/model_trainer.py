import numpy as np
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

from src.entity.artifact_entity import DataTransformationArtifactEntity, ModelTrainerArtifactEntity

from src.entity.input_entity.model_trainer_entity import ModelTrainerEntity

from src.logging.logger import logging

from src.utils.utils import load_numpy_array_data, save_object

class ModelTrainer:
    def __init__(self, data_transformation_artifact_entity: DataTransformationArtifactEntity, model_trainer_entity: ModelTrainerEntity):
        self.data_transformation_artifact_entity = data_transformation_artifact_entity
        self.model_trainer_entity = model_trainer_entity

    def train_model(self, X_train, y_train, X_test, y_test):
        try:
            logging.info("Training the model")
            model = RandomForestClassifier()
            model.fit(X_train, y_train)
            logging.info("Model training completed")
            y_pred_test = model.predict(X_test)
            y_pred_train = model.predict(X_train)
            test_accuracy = accuracy_score(y_test, y_pred_test)
            train_accuracy = accuracy_score(y_train, y_pred_train)
            print(f"Test Accuracy: {test_accuracy}")
            print(f"Train Accuracy: {train_accuracy}")
            model_trainer_artifact = ModelTrainerArtifactEntity(
                trained_model_file_path = self.model_trainer_entity.trained_model_file_path
            )
            os.makedirs(os.path.dirname(self.model_trainer_entity.trained_model_file_path), exist_ok=True)
            save_object(self.model_trainer_entity.trained_model_file_path, model)
            logging.info("Trained model saved successfully")

            return model_trainer_artifact
        except Exception as e:
            logging.error(f"Error occurred in train_model method: {e}")
            raise e

    
    def initiate_model_trainer(self):
        logging.info("Entered the initiate_model_trainer method of ModelTrainer class")
        train_arr_path = self.data_transformation_artifact_entity.data_transformation_train_file_path
        test_arr_path = self.data_transformation_artifact_entity.data_transformation_test_file_path

        train_arr =  load_numpy_array_data(train_arr_path)
        test_arr = load_numpy_array_data(test_arr_path)

        X_train = train_arr[:, :-1]
        y_train = train_arr[:, -1]
        X_test = test_arr[:, :-1]
        y_test = test_arr[:, -1]

        model_trainer_artifact = self.train_model(X_train, y_train, X_test, y_test)
        return model_trainer_artifact




        