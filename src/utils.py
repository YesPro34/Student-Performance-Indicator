import numpy as np
import pandas as pd
import sys
import os
from src.exception import CustomException
import dill
from sklearn.metrics import r2_score

def save_abject(file_path,obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def evaluate_models(X_train,y_train,X_test,y_test,models):

    report = {}

    for i in range(len(list(models))):
        model = list(models.values())[i]
        model.fit(X_train,y_train) #train model
        y_train_pred = model.predict(X_train)
        y_test_pred = model.predict(X_test)
        # evaluate each model 
        train_model_score = r2_score(y_train,y_train_pred)
        test_model_score = r2_score(y_test,y_test_pred)
        report[list(models.keys())[i]] = test_model_score
        
        return report 
