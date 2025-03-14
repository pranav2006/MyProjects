# **Movie Review Sentiment Analysis**
This project is a movie review sentiment analysis model built using **Naive Bayes** and **CountVectorizer**. The model classifies movie reviews as either **positive** or **negative**. It leverages data from the NLTK `movie_reviews` dataset and has been optimized to increase the accuracy of sentiment predictions. It is built on `scikit-learn` library.

## **Table of Contents**:
- [Model Improvements](#model-improvements)
- [Cross-Validation](#cross-validation)
- [Model Saving and Loading](#model-saving-and-loading)
- [Input New Reviews](#input-new-reviews)
- [Example Output](#example-output)
- [Conclusion](#conclusion)
  
## **Model Improvements**:

### **Hyperparameter Tuning**:
Through `GridSearchCV`, the following optimal parameters were found:
- **nb__alpha**: 0.5   (smoothing for Naive Bayes)
- **vectorizer__ngram_range**: (1, 2)   (both unigrams and bigrams)

## **Cross-Validation**:

We used **5-fold cross-validation** to evaluate the model's robustness across different data splits. The model achieved consistent accuracy scores:

```
Cross-Validation Scores: [0.8175, 0.845, 0.8325, 0.8375, 0.825]
```


## **Model Saving and Loading**:

The trained model is saved using **joblib** so that it can be reused later without retraining. It is saved as `sentiment_analysis.pkl`.

## **Input New Reviews**:

You can input a new review and predict its sentiment using the trained model.

### **Example Usage**:

```python
# Input new review
new_review = input("Enter a movie review: ")
new_review_series = pd.Series([new_review])

# Predict sentiment
prediction = clf_loaded.predict(new_review_series)
```

## **Example Output**:

Here is an example of what using the model might look like:

```
Enter a movie review: The movie was fantastic!
The review is positive.
```
```
Enter a movie review: I didn't like the plot.
The review is negative.
```

## **Conclusion**:

This project marks my **first machine learning project**, demonstrating how to apply machine learning to perform sentiment analysis on movie reviews. Through this journey, I’ve explored key steps such as **feature engineering**, **hyperparameter tuning**, and **model evaluation** using cross-validation.

I actually wanted to use the **TfidfVectorizer** instead of **CountVectorizer**, but I hadn't learned about it yet. I will definitely learn more about it and use it in my future models and projects. The model has been optimized for better performance and designed for easy deployment and reuse in other applications.

I’m excited to continue learning and expanding my skills in the field of **machine learning**!
