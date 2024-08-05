# Exploratory Data Analysis (EDA) Project Report:

# Objective:
The objective of this project is to perform Exploratory Data Analysis (EDA) on a dataset using Python libraries such as pandas, numpy, matplotlib, and seaborn. The goal is to explore the data's characteristics, distributions, correlations, and outliers, and to visualize these findings using various plots to gain insights into the data.

# Dataset Description:
RangeIndex: 891 entries, 0 to 890
Data columns (total 15 columns)
S.no    Column       Non-Null Count  Dtype   
---  ------       --------------  -----   
 0   survived     891 non-null    int64   
 1   pclass       891 non-null    int64   
 2   sex          891 non-null    object  
 3   age          714 non-null    float64 
 4   sibsp        891 non-null    int64   
 5   parch        891 non-null    int64   
 6   fare         891 non-null    float64 
 7   embarked     889 non-null    object  
 8   class        891 non-null    category
 9   who          891 non-null    object  
 10  adult_male   891 non-null    bool    
 11  deck         203 non-null    category
 12  embark_town  889 non-null    object  
 13  alive        891 non-null    object  
 14  alone        891 non-null    bool  
# Key Steps in the Project:
Data Loading and Understanding:

Load the dataset and get a basic understanding of its structure, including the types of data it contains, the presence of any missing values, and the distribution of the data across different features.
Data Visualization:

Visualize the distribution of numerical features using histograms.
Analyze categorical features with count plots.
Use scatter plots to explore relationships between numerical variables and survival status.
Correlation Analysis:

Calculate the correlation between numerical features and visualize it using a heatmap to identify which features are strongly associated with the target variable (e.g., survival).
Outlier Detection:

Detect and visualize outliers in numerical features using boxplots and violin plots.
# Concusion:
The Exploratory Data Analysis (EDA) on the Titanic dataset provided valuable insights into the data's characteristics, distributions, correlations, and outliers:

Data Overview:

The dataset consists of various features, both numerical (e.g., age, fare) and categorical (e.g., sex, class).
Missing values were observed, particularly in the age and embarked columns, which may need imputation or special handling.

Distribution Analysis:
Numerical features like age and fare exhibited skewed distributions, indicating the presence of outliers, particularly in the fare column.
The majority of passengers were in the 3rd class, and there was a nearly even distribution between male and female passengers.

Relationship Exploration:
Scatter plots and pair plots revealed some relationships between numerical variables. For instance, older passengers generally paid higher fares.
Survival rates varied across different classes and between genders, with females and higher-class passengers showing a higher likelihood of survival.
![Screenshot 2024-08-05 094857](https://github.com/user-attachments/assets/3d9af106-7831-46c7-85b3-afc311e53466)


Correlation Analysis:
The correlation heatmap highlighted that pclass and fare had significant correlations with survival, while other numerical features had weaker correlations.
Encoding categorical variables like sex and class into numerical form provided additional insights, showing that being female or in a higher class was positively correlated with survival.
![image](https://github.com/user-attachments/assets/e74932bf-a7ef-44b0-a4a9-dc2bfaa36363)


Outlier Detection:
Outliers were detected in the fare and age columns, which could skew the analysis and might require further investigation or handling.
