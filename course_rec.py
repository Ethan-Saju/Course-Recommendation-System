
import warnings
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

df = pd.read_csv('Couse Recommendation System\course_recommendation.csv')


X = df.drop(columns=['Course'])

y = df['Course']

X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)


def predictions(f, i):
    fields = {'Data Science': 1, 'Internet of Things': 2,
              'Artificial Intelligence': 3, 'Electronics': 4, 'Cyber Security': 5}
    interests = {'Art': 500, 'Music': 1000, 'Biology': 1500,
                 'Graphic Design': 2000, 'Marketing': 2500}

    field = fields[f]
    interest = interests[i]

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        return model.predict([[field, interest]])[0]
