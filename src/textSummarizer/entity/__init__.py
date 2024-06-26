# Step 7.3: Update the entity file
from dataclasses import dataclass
from pathlib import Path

# This is my entity for Data Ingestion
@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

# This is my entity for Data Validation
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list

# This is my entity for Data Transformation
@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_path: str
    tokenizer_name: list