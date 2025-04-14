# classification.py
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import numpy as np
import joblib

def train_classifier(X, y):
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X, y)
    return clf

def evaluate_classifier(clf, X_test, y_test):
    preds = clf.predict(X_test)
    print(classification_report(y_test, preds))

def save_model(clf, path):
    joblib.dump(clf, path)

def load_model(path):
    return joblib.load(path)
