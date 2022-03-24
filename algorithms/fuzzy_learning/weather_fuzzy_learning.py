from fuzzy_system.fuzzy_learning_helper import load_weather
from fuzzy_system.fuzzy_learning_helper import split_train_test
from fuzzy_system.fuzzy_learning_system import FuzzyLearningSystem

def execute_test(resolution, x_n, y_n):

    X, y = load_weather()

    X_train, X_test, y_train, y_test = split_train_test(X, y, test_size = 0.2)

    learning_system = FuzzyLearningSystem(res=resolution)

    learning_system.fit(X_train, y_train, X_n=x_n, y_n=y_n)

    score = learning_system.score(X_test, y_test)

    print(learning_system)

    learning_system.generate_rules_csv('weather_rules.csv')

    return score

if __name__ == "__main__":
    result = execute_test(1000,4,16)
    print(result)
