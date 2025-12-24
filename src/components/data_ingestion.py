from src.entity.input_entity import DataIngestionEntity

class DataIngestion:
    def __init__(self, data_ingestion_entity: DataIngestionEntity):
        print("Data Ingestion Started")
        print(f"Data Ingestion Dir: {data_ingestion_entity.data_ingestion_dir}")
        print(f"Feature store path: {data_ingestion_entity.feature_store_file_path}")
        print(f"Train file path: {data_ingestion_entity.ingested_dir_train_file_path}")
        print(f"Test file path: {data_ingestion_entity.ingested_dir_test_file_path}")