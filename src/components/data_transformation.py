import sys
import pandas as pd
import numpy as np

from src.entity import TrainingPipelineEntity
from src.entity.input_entity.data_transformation_entity import DataTransformationEntity
from src.entity.input_entity.data_ingestion_entity import DataIngestionEntity
from src.entity.artifact_entity import DataIngestionArtifactEntity, DataTransformationArtifactEntity

from src.utils.utils import clean_df, process_comment, get_transformation_object, save_numpy_array_data, save_object

from src.exception_handling.exception import NetworkSecurityException

from src.logging.logger import logging

class DataTransformation:
    def __init__(self, data_transformation_entity: DataTransformationEntity, data_ingestion_artifact_entity: DataIngestionArtifactEntity):
        self.data_transformation_entity = data_transformation_entity
        self.data_ingestion_artifact_entity = data_ingestion_artifact_entity

    def initiate_data_transformation(self):
        try:
            logging.info("Starting data transformation process")
            # read train and test data
            train_df = pd.read_csv(self.data_ingestion_artifact_entity.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact_entity.test_file_path)

            # clean the datarframe
            train_df = clean_df(train_df)
            test_df = clean_df(test_df)

            # split input and target features
            X_train = train_df.drop(columns='category')
            X_test = test_df.drop(columns='category')
            y_train = train_df['category']
            y_test = test_df['category']

            logging.info('Applying process_comment function in data transformation')
            # process clean_comment column
            X_train['clean_comment'] = X_train['clean_comment'].apply(lambda x: process_comment(x))
            X_test['clean_comment'] = X_test['clean_comment'].apply(lambda x: process_comment(x))
            # convert clean_comment column to vectorized form
            logging.info('Getting transformation object and applying fit_transform and transform methods')
            transformation = get_transformation_object()
            transformation_object = transformation.fit(X_train['clean_comment'].values)
            X_train_transformed = transformation_object.transform(X_train['clean_comment'].values)
            X_test_transformed = transformation_object.transform(X_test['clean_comment'].values)
     
            # convert to array and save the transformed data
            logging.info('Combining input features and target feature into single numpy array')
            train_arr = np.c_[X_train_transformed.toarray(), np.array(y_train)]
            test_arr = np.c_[X_test_transformed.toarray(), np.array(y_test)]

            save_numpy_array_data(self.data_transformation_entity.data_transformation_train_file_path, train_arr)
            save_numpy_array_data(self.data_transformation_entity.data_transformation_test_file_path, test_arr)
            save_object(self.data_transformation_entity.data_transformation_object_file_path, transformation_object)
            data_transformation_artifact = DataTransformationArtifactEntity(
                data_transformation_train_file_path=self.data_transformation_entity.data_transformation_train_file_path,
                data_transformation_test_file_path=self.data_transformation_entity.data_transformation_test_file_path,
                data_transformation_object_file_path=self.data_transformation_entity.data_transformation_object_file_path
            )
            return data_transformation_artifact
        except Exception as e:
            logging.error(f"Error occurred in initiate_data_transformation method: {e}")
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__":    
    training_pipeline_entity = TrainingPipelineEntity()
    data_ingestion_entity = DataIngestionEntity(training_pipeline_entity)
    
    # Create DataIngestionArtifactEntity from existing files (from data_ingestion stage)
    data_ingestion_artifact = DataIngestionArtifactEntity(
        train_file_path=data_ingestion_entity.ingested_dir_train_file_path,
        test_file_path=data_ingestion_entity.ingested_dir_test_file_path
    )
    
    # Create data transformation entity
    data_transformation_entity = DataTransformationEntity(training_pipeline_entity)
    
    # Run data transformation
    data_transformation = DataTransformation(data_transformation_entity, data_ingestion_artifact)
    data_transformation_artifact = data_transformation.initiate_data_transformation()
    
    print(f"Data transformation completed!")
    print(f"Train file: {data_transformation_artifact.data_transformation_train_file_path}")
    print(f"Test file: {data_transformation_artifact.data_transformation_test_file_path}")
    print(f"Transformation object: {data_transformation_artifact.data_transformation_object_file_path}")