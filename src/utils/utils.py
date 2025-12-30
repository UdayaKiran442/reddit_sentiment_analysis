import pandas as pd
import numpy as np
import certifi, ssl, urllib.request
import nltk, os, sys, pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline

from src.logging.logger import logging

from src.exception_handling.exception import NetworkSecurityException

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('wordnet')    
nltk.download('omw-1.4') 
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('stopwords')

lemetiser = WordNetLemmatizer()

def read_csv(file_path: str) -> pd.DataFrame:
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(file_path, context=ssl_context) as response:
        df = pd.read_csv(response)
        return df

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    try:
        logging.info("Entered the clean_df function")
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        df = df[df['clean_comment'].str.strip() != '']
        df['clean_comment'] = df['clean_comment'].str.replace('\n', ' ')
        logging.info("Exiting the clean_df function")
        return df
    except Exception as e:
        logging.error(f"Error occurred in clean_df function: {e}")
        raise NetworkSecurityException(e, sys)

def process_comment(comment: str) -> str:
    try:
        words = nltk.word_tokenize(comment)
        words = [lemetiser.lemmatize(word) for word in words if word not in set(stopwords.words('english')) ]
        return ' '.join(words)
    except Exception as e:
        logging.error(f"Error occurred in process_comment function: {e}")
        raise NetworkSecurityException(e, sys)

def get_transformation_object() -> Pipeline:
    try:
        vectorizer = TfidfVectorizer()
        return Pipeline([('vectorizer', vectorizer)])
    except Exception as e:
        logging.error(f"Error occurred in get_transformation_object function: {e}")
        raise NetworkSecurityException(e, sys)

def save_numpy_array_data(file_path: str, array: np.array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj, array)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    
def save_object(file_path: str, obj: object) -> None:
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys) from e
    
def load_numpy_array_data(file_path: str) -> np.array:
    """
    load numpy array data from file
    file_path: str location of file to load
    return: np.array data loaded
    """
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise NetworkSecurityException(e, sys)