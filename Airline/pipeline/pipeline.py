from collections import namedtuple
from datetime import datetime
import uuid
from Airline.config.configuration import Configuartion
from Airline.logging import logging
from Airline.exception import AirlineException
from threading import Thread
from typing import List

from multiprocessing import Process
from Airline.entity.artifact_entity import ModelPusherArtifact, DataIngestionArtifact, ModelEvaluationArtifact
from Airline.entity.artifact_entity import DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact
from Airline.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from Airline.component.data_ingestion import DataIngestion


import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd


class pipeline:

    def __init__(self, config: Configuartion = Configuartion()) -> None:
        try:
            self.config = config

        except Exception as e:
            raise AirlineException(e, sys)

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise AirlineException(str(e), sys)

    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass

    def run_pipeline(self):
        try:
            # data ingestion

            data_ingestion_artifact = self.start_data_ingestion()




        except Exception as e:
            raise AirlineException(e, sys)


