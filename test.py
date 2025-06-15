import pandas as pd
import joblib

# Load the trained Isolation Forest model
model = joblib.load('D:/mini_proj/isolation_forest_model.joblib')

# Function to preprocess user input data and check if user is fraudulent
def check_fraudulent(user_data):
    # Create a DataFrame with user input data
    user_df = pd.DataFrame([user_data])

    # Perform one-hot encoding for categorical columns
    user_df = pd.get_dummies(user_df, columns=['Gender','Location','Voting_Method','IP_Address','Transaction_ID'])

    # Ensure columns match with the model's feature names
    missing_cols = set(model.feature_names_in_) - set(user_df.columns)
    for col in missing_cols:
        user_df[col] = 0  # Add missing columns with default value 0

    # Reorder columns to match the model's feature order
    user_df = user_df[model.feature_names_in_]
    print(user_df)
    # Make predictions using the loaded model
    prediction = model.predict(user_df)
    print(prediction[0])
    # Interpret the prediction
    if prediction[0] == 1:
        return "User is likely not fraudulent."
    else:
        return "Potential fraud detected!"

# Example user input data (replace these values with actual user input)
user_input = {
    'Voter_ID': 1004.00,  # Not seen in training data
    'Age':40,  # Higher age compared to training data
    'Gender': 'Female',  # Similar to training data
    'Location': 'CityD',  # Uncommon location
    'Voting_Method': 'In-Person',  # Uncommon voting method
    'IP_Address': '192.168.4.1',  # Rare IP address
    'Transaction_ID': 'IKL012',  # Unusual transaction ID
    #'Fradulent_Label': 0  # Assuming this is a numeric label
}



# Check if the user is fraudulent based on the input data
result = check_fraudulent(user_input)
print(result)
