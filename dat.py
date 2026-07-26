import math

# Dataset stored inside the program
data = [
    [5.1, 3.5, "A"],
    [4.9, 3.0, "A"],
    [5.0, 3.6, "A"],
    [5.4, 3.9, "A"],
    [6.2, 3.4, "B"],
    [6.5, 3.0, "B"],
    [6.8, 3.2, "B"],
    [7.0, 3.1, "B"],
    [5.2, 3.4, "A"],
    [6.4, 3.2, "B"]
]

def split_data(data):
    train = []
    test = []

    for i in range(len(data)):
        if i % 3 == 0:
            test.append(data[i])
        else:
            train.append(data[i])

    return train, test

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def predict(train, test_row):
    nearest = train[0]
    min_distance = distance(train[0], test_row)

    for row in train:
        d = distance(row, test_row)
        if d < min_distance:
            min_distance = d
            nearest = row

    return nearest[2]

def evaluate(train, test):
    correct = 0

    print("\nPrediction Results")
    print("-"*40)

    for row in test:
        prediction = predict(train, row)

        print("Input:", row[0], row[1],
              "| Actual:", row[2],
              "| Predicted:", prediction)

        if prediction == row[2]:
            correct += 1

    accuracy = (correct/len(test))*100

    print("-"*40)
    print("Correct:", correct)
    print("Total:", len(test))
    print("Accuracy:", round(accuracy,2), "%")

def main():
    print("="*45)
    print("DATA CLASSIFICATION USING AI")
    print("="*45)

    train, test = split_data(data)

    print("Total Samples:", len(data))
    print("Training Samples:", len(train))
    print("Testing Samples:", len(test))

    evaluate(train, test)

main()