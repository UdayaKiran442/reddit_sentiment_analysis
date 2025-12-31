import os, sys
from sklearn.model_selection import train_test_split

from src.utils.utils import read_csv, read_yaml_file

from src.entity import TrainingPipelineEntity
from src.entity.input_entity.data_ingestion_entity import DataIngestionEntity
from src.entity.artifact_entity import DataIngestionArtifactEntity

from src.constants.constants import PARAMS_FILE_PATH

from src.exception_handling.exception import NetworkSecurityException

class DataIngestion:
    def __init__(self, data_ingestion_entity: DataIngestionEntity):
        self.data_ingestion_entity = data_ingestion_entity
    
    def initiate_data_ingestion(self):
        try:
            # read data from source
            df = read_csv("https://raw.githubusercontent.com/Himanshu-1703/reddit-sentiment-analysis/refs/heads/main/data/reddit.csv")
            params_file = read_yaml_file(PARAMS_FILE_PATH)
            test_size = params_file['data_ingestion']['test_size']
            random_state = params_file['data_ingestion']['random_state']


            # create directories if not exist
            ingested_dir_name = os.path.dirname(self.data_ingestion_entity.ingested_dir_train_file_path)
            os.makedirs(ingested_dir_name, exist_ok=True)
            feature_store_dir = os.path.dirname(self.data_ingestion_entity.feature_store_file_path)
            os.makedirs(feature_store_dir, exist_ok=True)

            # split data into train and test
            train, test = train_test_split(df, test_size=test_size, random_state=random_state)

            # save data to feature store and ingested directories
            train.to_csv(self.data_ingestion_entity.ingested_dir_train_file_path, index=False, header=True)
            test.to_csv(self.data_ingestion_entity.ingested_dir_test_file_path, index=False, header=True)
            df.to_csv(self.data_ingestion_entity.feature_store_file_path, index=False, header=True)
            data_ingestion_artifact = DataIngestionArtifactEntity(
                test_file_path=self.data_ingestion_entity.ingested_dir_test_file_path,
                train_file_path=self.data_ingestion_entity.ingested_dir_train_file_path
            )
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        

if __name__ == "__main__":
    training_pipeline_entity = TrainingPipelineEntity()
    data_ingestion_entity = DataIngestionEntity(training_pipeline_entity)

    data_ingestion = DataIngestion(data_ingestion_entity)
    data_ingestion_entity = data_ingestion.initiate_data_ingestion()

    print(data_ingestion_entity.test_file_path, data_ingestion_entity.train_file_path) 