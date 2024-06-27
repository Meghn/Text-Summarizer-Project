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

# This is my entity for Model Trainer
@dataclass(frozen=True)
class ModelTrainerConfig:
    root_dir: Path
    data_path: Path
    model_ckpt: Path
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_step: int
    evaluation_strategy: str
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int

# This is my entity for Model Evaluation
@dataclass(frozen=True)
class ModelEvaluationConfig:
    root_dir: Path
    data_path: Path
    model_path: Path
    tokenizer_path: Path
    metric_file_name: Path