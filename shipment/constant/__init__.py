import os
from os import environ
from datetime import datetime
from from_root.root import from_root
from dotenv import load_dotenv
load_dotenv()

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

MODEL_CONFIG_FILE = "config/model.yaml"
SCHEMA_FILE_PATH = "config/schema.yaml"

DB_URL = os.getenv("MONGO_DB_URL")

TARGET_COLUMN = "Cost"
DB_NAME = "SURRAJIT"
COLLECTION_NAME = "ShipmentData"
TEST_SIZE = 0.2
ARTIFACTS_DIR = os.path.join(from_root(), "artifacts", TIMESTAMP)


DATA_INGESTION_ARTIFACTS_DIR = "DataIngestionArtifacts"
DATA_INGESTION_TRAIN_DIR = "Train"
DATA_INGESTION_TEST_DIR = "Test"
DATA_INGESTION_TRAIN_FILE_NAME = "train.csv"
DATA_INGESTION_TEST_FILE_NAME = "test.csv"


DATA_VALIDATION_ARTIFACT_DIR = "DataValidationArtifacts"
DATA_DRIFT_FILE_NAME = "DataDriftReport.yaml"