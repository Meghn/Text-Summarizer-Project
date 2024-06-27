# # Step 4.5: check the logger 
# from textSummarizer.logging import logger

# logger.info("Text summarizer project setup completed successfully.")

# Step 7.7: Add the Data Ingestion to the main file
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} stage <<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>> Completed {STAGE_NAME} stage <<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} stage <<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>> Completed {STAGE_NAME} stage <<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} stage <<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>> Completed {STAGE_NAME} stage <<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Trainer"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} stage <<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> Completed {STAGE_NAME} stage <<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Model Evaluation"
try:
    logger.info(f">>>>> Starting {STAGE_NAME} stage <<<<<")
    model_trainer = ModelEvaluationTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>> Completed {STAGE_NAME} stage <<<<<\n\nx=============x")
except Exception as e:
    logger.exception(e)
    raise e