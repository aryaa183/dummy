# logistic_regression.py

import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# -----------------------------
# 1. Load dataset
# -----------------------------
data = pd.read_csv('cleaned_accident_data.csv')  # make sure path is correct

# -----------------------------
# 2. Select features similar to your user input form
# -----------------------------
form_features = [
    'Time Period',             # categorical
    'Weather Conditions',      # categorical
    'Road Condition',          # categorical
    'Lighting Conditions',     # categorical
    'Speed Limit (km/h)',      # numeric
    'Driver Age'               # numeric
]

X = data[form_features]
y = data['Accident Severity']  # already numeric (0,1,2)

# -----------------------------
# 3. Identify categorical & numeric features
# -----------------------------
categorical_features = [
    'Time Period',
    'Weather Conditions',
    'Road Condition',
    'Lighting Conditions'
]

numeric_features = [
    'Speed Limit (km/h)',
    'Driver Age'
]

# -----------------------------
# 4. Preprocessing pipeline
# -----------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features),
        ('num', 'passthrough', numeric_features)
    ]
)

# -----------------------------
# 5. Logistic Regression pipeline
# -----------------------------
logreg_pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('classifier', LogisticRegression(max_iter=2000))
])

# -----------------------------
# 6. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 7. Train model
# -----------------------------
logreg_pipeline.fit(X_train, y_train)

# -----------------------------
# 8. Evaluate
# -----------------------------
y_pred = logreg_pipeline.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

# -----------------------------
# 9. Save model
# -----------------------------
joblib.dump(logreg_pipeline, 'risk_model_logreg.pkl')
print("Logistic Regression model saved as risk_model_logreg.pkl")
