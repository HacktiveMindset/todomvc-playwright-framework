import json
def load_test_data():
    with open("test-data/testData.json") as f:
        return json.load(f)
