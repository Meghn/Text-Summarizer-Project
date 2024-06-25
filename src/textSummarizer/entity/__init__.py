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