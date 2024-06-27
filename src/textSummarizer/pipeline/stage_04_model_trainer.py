from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.model_trainer import ModelTrainer

class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config = model_trainer_config)
        model, tokenizer = model_trainer.train() 
        model_trainer.save_model(model, tokenizer)
