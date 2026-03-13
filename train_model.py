import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# load dataset
data = pd.read_csv("dataset.csv")

# create encoder
le = LabelEncoder()

# convert Animal column to numbers
data["Animal_Type"] = le.fit_transform(data["Animal_Type"])

# separate features & target
X = data.drop("Disease", axis=1)
y = data["Disease"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# save model + encoder
joblib.dump(model, "model.pkl")
joblib.dump(le, "animal_encoder.pkl")

print("Model & encoder saved")