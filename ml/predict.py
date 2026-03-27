import pickle
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')

# Global variables to hold the loaded model and vectorizer
model = None
vectorizer = None

def load_models():
    global model, vectorizer
    if not os.path.exists(MODEL_PATH) or not os.path.exists(VECTORIZER_PATH):
        raise FileNotFoundError("Model or Vectorizer file not found. Ensure you run train.py first.")
        
    if model is None or vectorizer is None:
        with open(MODEL_PATH, 'rb') as f:
            model = pickle.load(f)
        with open(VECTORIZER_PATH, 'rb') as f:
            vectorizer = pickle.load(f)
            
    return model, vectorizer

def predict_fake_news(text: str):
    """
    Predicts if the text is fake or real news.
    Returns: label (str), probability (float)
    """
    m, v = load_models()
    
    # Vectorize the input
    tfidf_input = v.transform([text])
    
    # Predict
    prediction = m.predict(tfidf_input)[0]
    
    # PassiveAggressiveClassifier doesn't provide predict_proba directly out of the box without calibration,
    # but we can use decision_function to get confidence.
    decision = m.decision_function(tfidf_input)[0]
    confidence = float(abs(decision))  # the magnitude is confidence
    
    # In GonzaloA/fake_news normally: 0 = Fake, 1 = True (Real)
    # Check dataset specs or our train script assumptions.
    # We'll map: 1 -> Real/Authentic, 0 -> Fake/Misleading
    if prediction == 1:
        result = "Real News"
    else:
        result = "Fake News"
        
    return {"result": result, "confidence": confidence}
