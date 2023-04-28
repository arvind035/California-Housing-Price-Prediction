from HousePricePrediction.pipeline.pipeline import Pipeline
from HousePricePrediction.exception import HousePriceException
from HousePricePrediction.logger import logging
from HousePricePrediction.config.configuration import Configuartion
from HousePricePrediction.component.data_transformation import DataTransformation
import os
def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuartion(config_file_path=config_path))
        pipeline.start()
        logging.info("main function execution completed.")

    except Exception as e:
        logging.error(f"{e}")
        print(e)



if __name__=="__main__":
    main()

