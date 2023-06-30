import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

# Load the csv file
df = pd.read_csv("kc_house_data.csv")

#print(df.info())

# Select independent and dependent variable
X = df[["bedrooms", "bathrooms", "sqft_living", "sqft_lot", "floors", "zipcode"]]
y = df["price"]

# Split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=50)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)

#Instantiate the model
classifier = RandomForestRegressor(max_depth=6)

#Fit the model
classifier.fit(X_train, y_train)

# Make pickle file or our model
pickle.dump(classifier, open("model.pkl", 'wb'))
