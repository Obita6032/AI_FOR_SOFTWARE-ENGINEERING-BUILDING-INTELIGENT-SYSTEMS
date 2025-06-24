# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, classification_report

# Step 2: Load Data
df = pd.read_csv('data.csv')  # Adjust path
df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)

# Step 3: Label Encoding
df['diagnosis'] = df['diagnosis'].map({'M': 'high', 'B': 'low'})

# Step 4: Split Features and Target
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

# Step 5: Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 6: Train Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 7: Predict and Evaluate
y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred, pos_label="high")

print("Accuracy:", accuracy)
print("F1 Score:", f1)
print("\nClassification Report:\n", classification_report(y_test, y_pred))
Accuracy: 0.9561
F1 Score: 0.96

#               precision    recall  f1-score   support

#         high       0.96      0.93      0.94        45
#          low       0.95      0.97      0.96        69

#     accuracy                           0.95       114
#    macro avg       0.95      0.95      0.95       114
# weighted avg       0.95      0.95      0.95       114
