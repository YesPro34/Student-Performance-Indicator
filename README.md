## End To End ML Project - Student Performance Indicator

### Introduction About the Data :

The dataset's goal is to predict the math score of a student  using Regression Analysis.

There are 7 independent variables :

- **gender**: refers to the gender of the student (male or female)
- **ethnicity'**: the ethnicity of the student.
- **parental level of education**: refers to the the education level of the student's parent.
- **lunch**: the type of lunch that the student have in the school.
- **test preparation course**: Does the student complete the test preparation or not.
- **reading score**: the reading score of the  student,it is a numeric value between 0 and 100.
- **writing score**:the writing score of the student, it is a numeric value between 0 and 100. 


### Target variable:
- **math score**: the math score that the student may get in the Test, it is a numeric value between 0 and 100.

### Dataset Source
[Link to Dataset](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)


###  Deployment Link
render.com deployement link: [Deployment](https://student-performance-indicator-bl70.onrender.com)

### Screenshot of UI
![Homepage UI](https://github.com/YesPro34/Student-Performance-Indicator/blob/main/screenshots/homepage.png)



## Approach for the Project

### Data Ingestion
- The data is first read as a CSV.
- The data is then split into training and testing sets and saved as CSV files.

### Data Transformation
- A ColumnTransformer Pipeline is created.
  - For numeric variables, first SimpleImputer is applied with strategy median, then Standard Scaling is performed on numeric data.
  - For categorical variables, SimpleImputer is applied with the most frequent strategy, then ordinal encoding is performed. After this, data is scaled with Standard Scaler.
- This preprocessor is saved as a pickle file.

### Model Training
- Base models are tested. The best model found was Linear regressor.
- Hyperparameter tuning is performed on all regression models.
- This model is saved as a pickle file.

### Prediction Pipeline
- This pipeline converts given data into a dataframe and has various functions to load pickle files and predict the final results in Python.

### Flask App Creation
- A Flask app is created with a User Interface to predict the gemstone prices inside a web application.

