class DataIngestionArtifactEntity:
    def __init__(self, train_file_path: str, test_file_path: str):
        self.train_file_path: str = train_file_path
        self.test_file_path: str = test_file_path