from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.entity.input_entity import DataIngestionEntity, TrainingPipelineEntity, DataTransformationEntity, ModelTrainerEntity

if __name__ == "__main__":
    training_pipeline_entity = TrainingPipelineEntity()
    data_ingestion_entity = DataIngestionEntity(training_pipeline_entity=training_pipeline_entity)
    data_ingestion = DataIngestion(data_ingestion_entity)
    data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
    print("Data Ingestion Successfully completed")
    data_transformation = DataTransformation(
        data_transformation_entity= DataTransformationEntity(training_pipeline_entity=training_pipeline_entity),
        data_ingestion_artifact_entity= data_ingestion_artifact
    )
    data_transformation_artifact = data_transformation.initiate_data_transformation()
    print("Data Transformation Successfully completed")
    model_trainer = ModelTrainer(
        data_transformation_artifact_entity=data_transformation_artifact,
        model_trainer_entity= ModelTrainerEntity(training_pipeline_entity=training_pipeline_entity)
    )
    model_trainer_artifact = model_trainer.initiate_model_trainer()
    print(model_trainer_artifact)
    print("Model Training Successfully completed")