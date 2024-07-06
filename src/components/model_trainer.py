
import os
import sys
from dataclasses import dataclass

from sklearn.ensemble import(
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from xgboost import XGBRegressor

from sklearn.metrics import r2_score

from src.exception import CustomException
from src.logger import logging

from src.utils import evaluate_models, save_abject


@dataclass
class ModelTrainerConfig:
    model_file_path = os.path.join("artifacts","model.pkl")

class ModelTrainer:
    
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self,train_array, test_array):
        try:
            logging.info("Spliting trainign and test data")
            X_train,y_train,X_test,y_test = (
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1],
            )

            models = {
                "Random Forest": RandomForestRegressor(),
                "Decision Tree": DecisionTreeRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "Linear Regression": LinearRegression(),
                "K-Neighbors Classifier": KNeighborsRegressor(),
                "XGBClassifier": XGBRegressor(),
                "AdaBoost Classifier": AdaBoostRegressor(),
                }
            
            models_report:dict = evaluate_models(X_train=X_train,X_test=X_test,y_train=y_train,y_test=y_test,models=models)

            # get the best model score and name from models_report
            best_model_score = max(sorted(models_report.values()))
            best_model_name = list(models_report.keys())[list(models_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.6:
                raise CustomException("No best Model found")
            logging.info(f"the best model in both training and testing is {best_model}")

            save_abject(
                file_path=self.model_trainer_config.model_file_path,
                obj=best_model 
            )

            prediced = best_model.predict(X_test)
            r2_score_val = r2_score(y_test,prediced)

            return r2_score_val

        except Exception as e:
            raise CustomException(e, sys)
