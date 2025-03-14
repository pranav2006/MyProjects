import joblib
import pandas as pd

clf_loaded = joblib.load('sentiment_analysis.pkl')

new_review = input("Enter a movie review: ")
review_series = pd.Series([new_review])

prediction = clf_loaded.predict(review_series)

if prediction[0] == 'pos':
    print("The review is positive.")
else:
    print("The review is negative.")