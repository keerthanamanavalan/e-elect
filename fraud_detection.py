import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import joblib

# Load and preprocess data from Excel file without Timestamp column
data = pd.read_excel('fraud_detection_data.xlsx', usecols=lambda col: col not in ['Timestamp'])

# Perform one-hot encoding for categorical columns (e.g., 'Gender')
data = pd.get_dummies(data, columns=['Gender','Location','Voting_Method','IP_Address','Transaction_ID'])

# Convert integer columns to object dtype to resolve dtype promotion error
data['Voter_ID'] = data['Voter_ID'].astype('object')  # Convert Voter_ID to object
data['Age'] = data['Age'].astype('object')  # Convert Age to object

# Ensure correct data types for other columns (if needed)
data['Fradulent_Label'] = data['Fradulent_Label'].astype('int64')  # Convert Fradulent_Label to int64 if needed

# Separate features (X) and target variable (y)
X = data.drop(columns=['Fradulent_Label'])
y = data['Fradulent_Label']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Isolation Forest model for anomaly detection
model = IsolationForest(contamination=0.1) 
model.fit(X_train)

# Predict anomalies
y_pred = model.predict(X_test)
y_pred[y_pred == 1] = 0  # 1 indicates normal, 0 indicates anomaly


print(model)
joblib.dump(model, 'isolation_forest_model.joblib')
# Evaluate model performance
print(classification_report(y_test, y_pred))
