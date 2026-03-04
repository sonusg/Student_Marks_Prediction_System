# 📊 Student Marks Prediction using Machine Learning

A simple and beginner-friendly Machine Learning project that predicts **student exam scores based on study hours** using **Simple Linear Regression**.

This project demonstrates the complete ML workflow:
data analysis → visualization → model training → evaluation → prediction.



## 🎯 Project Goal

Educational platforms often want to understand **how study time affects student performance**.
Instead of waiting for final exam results, we can use **Machine Learning** to estimate expected marks earlier.

This helps educators:

* 📉 Identify students who may need extra help
* 📈 Encourage better study habits
* 🎯 Predict academic performance in advance
  


## 📂 Dataset

The dataset contains **96 student records** with two numerical features:

| Feature   | Description             |
| --------- | ----------------------- |
| ⏱ Hours   | Number of hours studied |
| 📝 Scores | Marks obtained in exam  |

Example:

| Hours | Scores |
| ----- | ------ |
| 2.5   | 21     |
| 5.1   | 47     |
| 3.2   | 27     |
| 8.5   | 75     |



## 🧠 Machine Learning Model

This project uses **Simple Linear Regression** from the **scikit-learn** library.

The model learns a relationship between:


Study Hours → Exam Score


The learned equation is:

Score = m × Hours + c


Where:

* **m** → how much marks increase per study hour
* **c** → base score when study hours = 0



## 📈 Model Performance

| Metric             | Value |
| ------------------ | ----- |
| Mean Squared Error | 17.00 |
| R² Score           | 0.97  |

An **R² score of 0.97** means the model explains **97% of the relationship between study hours and marks**, which indicates a strong predictive model.



## 🔮 Example Prediction

If a student studies:

Study Hours = 4


The model predicts:

Predicted Score ≈ 41.78


## 🛠 Technologies Used

* 🐍 Python
* 📊 Pandas (data analysis)
* 📉 Matplotlib (visualization)
* 🤖 Scikit-learn (machine learning)


## 📊 Visualization

The project plots a **scatter graph** showing the relationship between study hours and scores.

This helps visualize how **study time influences academic performance**.

## 💡 What I Learned

Through this project I learned:

* How **Linear Regression works**
* How to **prepare and analyze datasets**
* How to **train and evaluate ML models**
* How to **make predictions using machine learning**



## 👨‍💻 Author

**Sonu SG**

Computer Science student interested in
Machine Learning • Software Engineering • Real-world problem solving


⭐ If you found this project helpful, feel free to **star the repository**!




