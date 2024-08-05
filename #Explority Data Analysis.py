#Explority Data Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the Titanic dataset from seaborn's inbuilt dataset
df = sns.load_dataset('titanic')

# Display the first few rows of the dataset
df.head()
# Check the shape of the dataset
print(f"Dataset Shape: {df.shape}")

# Get basic information about the dataset
df.info()

# Summary statistics for numerical columns
df.describe()

# Check for missing values
df.isnull().sum()

# Display unique values for categorical columns
df.nunique()
# Histogram for numerical features
df.hist(figsize=(12, 8), bins=20, color='skyblue')
plt.suptitle('Distribution of Numerical Features', fontsize=16)
plt.show()

# Distribution plot for Age
plt.figure(figsize=(10, 6))
sns.histplot(df['age'].dropna(), kde=True, color='blue')
plt.title('Age Distribution')
plt.show()

# Count plot for categorical features like 'sex' and 'class'
plt.figure(figsize=(12, 6))
sns.countplot(x='sex', data=df, palette='Set2')
plt.title('Count of Passengers by Sex')
plt.show()

plt.figure(figsize=(12, 6))
sns.countplot(x='class', data=df, palette='Set3')
plt.title('Count of Passengers by Class')
plt.show()
# Scatter plot between Age and Fare
plt.figure(figsize=(10, 6))
sns.scatterplot(x='age', y='fare', data=df, hue='sex', palette='coolwarm')
plt.title('Age vs Fare by Sex')
plt.show()

# Pairplot to see the relationships across multiple features
sns.pairplot(df[['age', 'fare', 'pclass', 'survived']], hue='survived', palette='husl')
plt.suptitle('Pairplot of Age, Fare, Pclass, and Survival', y=1.02, fontsize=16)
plt.show()

# Correlation heatmap - Exclude non-numeric columns
plt.figure(figsize=(10, 8))

# Selecting only the numeric columns for correlation
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr()

# Plot the heatmap
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Check the correlation of specific features with survival
corr_with_survival = numeric_df.corr()['survived'].sort_values(ascending=False)
print("Correlation with Survival:\n", corr_with_survival)

# Boxplot to detect outliers in the Fare feature
plt.figure(figsize=(10, 6))
sns.boxplot(x='fare', data=df)
plt.title('Boxplot of Fare')
plt.show()

# Violin plot for Age distribution by Class
plt.figure(figsize=(12, 6))
sns.violinplot(x='class', y='age', data=df, palette='muted')
plt.title('Age Distribution by Class')
plt.show()
