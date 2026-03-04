# Import Required Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score


# Load Dataset
df = pd.read_csv("score_updated.csv")

print("First 5 rows of dataset:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())


# Visualize Relationship
plt.figure(figsize=(6,4))
plt.scatter(df["Hours"], df["Scores"], color="blue")
plt.title("Study Hours vs Scores")
plt.xlabel("Study Hours")
plt.ylabel("Scores")
plt.grid(True)
plt.show()


# Prepare Features and Target
X = df[["Hours"]]     # Input feature
y = df["Scores"]      # Target variable


# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Train Linear Regression Model
model = LinearRegression()

model.fit(X_train, y_train)


# Model Parameters
print("\nModel Parameters")

print("Slope (Coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)


# Predictions
y_pred = model.predict(X_test)


# Model Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation")
print("Mean Squared Error:", mse)
print("R2 Score:", r2)


# Predict New Value
study_hours = pd.DataFrame([[4]], columns=["Hours"])

predicted_score = model.predict(study_hours)

print(f"\nPredicted Score for 4 study hours: {predicted_score[0]:.2f}")