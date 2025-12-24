from src.components.data_ingestion import DataIngestion
from src.entity.input_entity import DataIngestionEntity, TrainingPipelineEntity

if __name__ == "__main__":
    training_pipeline_entity = TrainingPipelineEntity()
    data_ingestion_entity = DataIngestionEntity(training_pipeline_entity=training_pipeline_entity)
    data_ingestion = DataIngestion(data_ingestion_entity)