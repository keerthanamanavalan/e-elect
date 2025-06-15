import pandas as pd
import nltk
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split

# Load data from Excel file
data = pd.read_excel('D:/mini_proj/data/chatbot_data.xlsx')

# Preprocess text
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = nltk.word_tokenize(text)
    tokens = [lemmatizer.lemmatize(token.lower()) for token in tokens]
    return ' '.join(tokens)

data['Processed_Input'] = data['User_Input'].apply(preprocess_text)

# C11ck if the dataset is large enough to split
if len(data) > 1:
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(data['Processed_Input'], data['Response'], test_size=0.2, random_state=42)
else:
    # Use all data for training if the dataset is too small
    X_train = X_test = data['Processed_Input']
    y_train = y_test = data['Response']

# Create a pipeline that combines the vectorizer and the classifier
model = make_pipeline(TfidfVectorizer(), MultinomialNB())

# Train the model
model.fit(X_train, y_train)

# Evaluate the model if there is a test set
if len(data) > 1:
    accuracy = model.score(X_test, y_test)
    print(f'Model Accuracy: {accuracy}')
else:
    print('Dataset too small to split; using entire dataset for training.')

def get_response(user_input):
    processed_input = preprocess_text(user_input)
    predicted_response = model.predict([processed_input])[0]
    return predicted_response

# Chat with the bot
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    response = get_response(user_input)
    print(f"Bot: {response}")
