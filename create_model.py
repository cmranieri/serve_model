from sklearn.datasets import load_breast_cancer
from sklearn.linear_model import LogisticRegression
import joblib

# Load dataset
data = load_breast_cancer()
X = data.data[:, [0, 1, 4]]  # mean radius, mean texture, mean smoothness
y = data.target

# Train simple model
model = LogisticRegression(max_iter=10000)
model.fit(X, y)

# Save model
joblib.dump(model, "model.pkl")

