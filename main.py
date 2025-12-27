from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.entity.input_entity import DataIngestionEntity, TrainingPipelineEntity, DataTransformationEntity

if __name__ == "__main__":
    training_pipeline_entity = TrainingPipelineEntity()
    data_ingestion_entity = DataIngestionEntity(training_pipeline_entity=training_pipeline_entity)
    data_ingestion = DataIngestion(data_ingestion_entity)
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    data_transformation = DataTransformation(
        data_transformation_entity= DataTransformationEntity(training_pipeline_entity=training_pipeline_entity),
        data_ingestion_artifact_entity= data_ingestion_artifact
    )
    data_transformation_artifact = data_transformation.initiate_data_transformation()
    print("Data Transformation Completed")
    print("\n")
    print(data_transformation_artifact.data_transformation_object_file_path, data_transformation_artifact.data_transformation_test_file_path, data_transformation_artifact.data_transformation_train_file_path)