import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

print("Loading dataset...")

df = pd.read_csv(
    r"C:\Users\Sri Pranav\Downloads\traffic-dashboard\backend\data\US_Accidents_March23.csv",
    nrows=300000   # load only 3 lakh rows instead of 30 lakh
)

print("Dataset loaded")
print("Rows loaded:", len(df))


# Select useful columns
df = df[["Severity","Start_Time","Temperature(F)","Visibility(mi)","Wind_Speed(mph)","Humidity(%)"]]

print("Parsing datetime...")

# THIS LINE FIXES YOUR ERROR 100%
df["Start_Time"] = pd.to_datetime(df["Start_Time"], format="ISO8601", errors="coerce")

# Convert to hour
df["Hour"] = df["Start_Time"].dt.hour

# Drop missing values
df = df.dropna()
df = df.drop("Start_Time", axis=1)

print("Training model...")

# Features & target
X = df.drop("Severity", axis=1)
y = df["Severity"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier(
    n_estimators=50,   # reduce trees
    max_depth=10,      # limit tree depth
    n_jobs=-1          # use all CPU cores
)

model.fit(X_train, y_train)

# Save model inside model folder
joblib.dump(model, r"C:\Users\Sri Pranav\Downloads\traffic-dashboard\backend\model\traffic_model.pkl")

print("✅ MODEL TRAINED AND SAVED SUCCESSFULLY!")
