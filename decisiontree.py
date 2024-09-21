import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from urllib.parse import urlparse

# Load the dataset
URL = pd.read_csv("decision.csv")

# Feature extraction from URL
URL['url_length'] = URL['URL'].apply(lambda x: len(x))
URL['domain'] = URL['URL'].apply(lambda x: urlparse(x).netloc)

# Drop the original 'domain' column
URL.drop('domain', axis=1, inplace=True)

# Encoding categorical features
URL = pd.get_dummies(URL, columns=['URL'])

# Split the dataset into features and target variable
X = URL.drop(['Label'], axis=1)
y = URL['Label']

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create Decision Tree classifier object
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train, y_train)

# Predict the response for test dataset
y_pred = clf.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
