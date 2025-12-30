class DataIngestionArtifactEntity:
    def __init__(self, train_file_path: str, test_file_path: str):
        self.train_file_path: str = train_file_path
        self.test_file_path: str = test_file_path

class DataTransformationArtifactEntity:
    def __init__(self, data_transformation_train_file_path: str, data_transformation_test_file_path: str, data_transformation_object_file_path: str):
        self.data_transformation_train_file_path: str = data_transformation_train_file_path
        self.data_transformation_test_file_path: str = data_transformation_test_file_path
        self.data_transformation_object_file_path: str = data_transformation_object_file_path

class ModelTrainerArtifactEntity:
    def __init__(self, trained_model_file_path: str):
        self.trained_model_file_path = trained_model_file_path