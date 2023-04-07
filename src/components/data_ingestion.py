import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:

    #here is input train data path later on my data will save (train.csv) file in this particular file 
    train_data_path:str=os.path.join('artifacts',"train.csv")  
    test_data_path:str=os.path.join('artifacts',"test.csv")  
    raw_data_path:str=os.path.join('artifacts',"data.csv")

class DataIngestion: #-> when this call above three path will get save inside (ingestion_config) class variable itself
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        # read data from dataBase (i can create in util file and then i can able to read it)

        #-> but here reading in easy way
        logging.info("Entered the data ingestion method or component")

        #reading the data set from somewhere (it can be anywhere)

        try:   
            df=pd.read_csv('notebook\data\stud.csv')
            logging.info('Read the data set as dataframe')

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            #converting from row to csv file
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) #data save in raw path 

            logging.info("train test split initiated")
            #training the data
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            #saving the training file 
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("ingestion of the data is changed")
            #returning for the next data transformation part 
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":

    obj=DataIngestion()
    obj.initiate_data_ingestion()

# now artifacts folder will be created

