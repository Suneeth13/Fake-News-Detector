import os
import pickle
import pandas as pd
from datasets import load_dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, classification_report

def train_model():
    print("Loading dataset 'GonzaloA/fake_news' from Hugging Face...")
    try:
        dataset = load_dataset('GonzaloA/fake_news')
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return

    # Using the train split for training and validation split for testing
    train_df = pd.DataFrame(dataset['train'])
    test_df = pd.DataFrame(dataset['validation'])

    # Combine title and text for better context
    train_df['content'] = train_df['title'] + " " + train_df['text']
    test_df['content'] = test_df['title'] + " " + test_df['text']

    # The labels in GonzaloA/fake_news are: 0 for Fake and 1 for True
    # Let's map Fake to 1 and True to 0 so "Fake News Detector" flags 1 as Fake.
    # Actually, let's keep it as is, we can handle it in predict.
    y_train = train_df['label']
    y_test = test_df['label']

    print("Vectorizing Text Data...")
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7, max_features=10000)
    tfidf_train = vectorizer.fit_transform(train_df['content'])
    tfidf_test = vectorizer.transform(test_df['content'])

    print("Training Passive Aggressive Classifier...")
    model = PassiveAggressiveClassifier(max_iter=50)
    model.fit(tfidf_train, y_train)

    print("Evaluating Model...")
    y_pred = model.predict(tfidf_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Validation Accuracy: {accuracy * 100:.2f}%")
    print(classification_report(y_test, y_pred))

    # Save the model
    os.makedirs('ml', exist_ok=True)
    
    with open('ml/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    
    with open('ml/model.pkl', 'wb') as f:
        pickle.dump(model, f)
        
    print("Model and vectorizer saved to ml/ dir.")

if __name__ == "__main__":
    train_model()
