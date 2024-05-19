import numpy as np
import pandas as pd
from datetime import datetime
from raw_data import getDataSet
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import time


def build_model():
    print("building model")
    # Convert timestamps to readable datetime
    dates = getDataSet() # [datetime.fromtimestamp(ts) for ts in timestamps]
    print("number of readtAt: ", len(dates))
    start_time = time.time()

    # Create a DataFrame
    df = pd.DataFrame(dates, columns=['datetime'])

    # Extract features
    df['hour'] = df['datetime'].dt.hour
    # df['minute'] = df['datetime'].dt.minute # why not work with this?
    df['day_of_week'] = df['datetime'].dt.weekday
    df['is_weekend'] = df['day_of_week'].apply(lambda x: 1 if x > 4 else 0)

    # For the purpose of this example, let's assume the target is the hour of the day
    df['target'] = df['hour'] # TODO create manually this target dt_now x schedule_dt

    # Drop the original datetime column
    df.drop('datetime', axis=1, inplace=True)

    # print("df\n",df) # hour  day_of_week  is_weekend  target

    X = df.drop('target', axis=1)
    y = df['target'] # TODO how use two variables to target this

    # split data set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42) # why 42? what's random_state?

    # Initialize the model
    clf = RandomForestClassifier(n_estimators=100, random_state=42) # why 42? what's random_state?

    # Train the model
    clf.fit(X_train.values, y_train)
    print("model built in {} seconds".format(time.time() - start_time))

    # Predict on the test set
    y_pred = clf.predict(X_test.values)
    # Evaluate the accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy}")
    return clf


def run():
    clf = build_model()
    now = datetime.now()

    # Sample prediction
    for dt in [now, now.replace(hour=10), now.replace(hour=15), now.replace(hour=1), now.replace(day=now.day+2), now.replace(day=now.day+3)]:
        features = np.array([[dt.hour, dt.weekday(), 1 if dt.weekday() > 4 else 0]])
        # Predict the best hour
        predicted_hour = clf.predict(features)
        print(f"Best time to send a message at {dt.strftime('%Y-%m-%d %H:%M')} ({dt.strftime('%a')}) is next: {predicted_hour[0]}:00")

if __name__ == "__main__":
    run()
