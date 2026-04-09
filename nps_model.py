# Portfolio Project: Predictive NPS Modeling
# Description: Simple regression model to predict fan satisfaction (NPS)
# Note: Data is anonymized and simplified for demonstration purposes

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Load dataset
df = pd.read_csv('data/sample_nps_data.csv')

# Define features and target
features = ['win_pct', 'attendance', 'temperature']
target = 'nps'

X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error:", mae)
print("R² Score:", r2)

# Show feature importance (coefficients)
coefficients = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_
})

print("\nFeature Impact:")
print(coefficients)
