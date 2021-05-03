'''
Thang Do Minh

Pruning
Use CART (Classification and Regression Tree) - Gini index
Step 1: read data
Step 2: convert data (csv) -> array 2D
Step 3: Calculate gini - Calculate Entropy (impurity) 
Step 4: Pick order for attribute
Step 5: Stop conditione
    - Node has Entropy = 0
    - Child of node less than k (which k is number we pick, maybe test many time -> pick
    - Limited the height of tree
    - ...
Step 6: Build tree
* Advanced: "Reduced Error Pruning" -> split tree
'''
import csv
import math

buying = 0
maint = 1
doors = 2
persons = 3
lug_boot = 4
safety = 5

attribute_data = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']

def getListValueUniqueAttribute():

    return []

def getProbability():
    return 

def calculateEntropy(rows):
    # return dist value entropy or attribute
    value_entropy = {}
    for attribute in attribute_data:
        # Calculate entropy
        entropy = 0
        list_value_unique_attribute = getListValueUniqueAttribute()
        for value_attribute in list_value_unique_attribute:
            probability = getProbability()
            entropy += property * math.log(property, 2)
        value_entropy[attribute] = -entropy

    return value_entropy



def best_split(rows):
    pass


def partition(rows, question):
    left_branch, right_branch = [], []
    for row in rows:
        # TODO
        pass



class Leaf:
    predictions: dict

    def __init__(self, predictions):
        self.predictions = predictions

    def predict(self):
        return max(self.predictions)


def label_count(rows):
    count = {}
    for row in rows:
        label = row[-1]
        if label not in count:
            count[label] = 1
        count += 1
    return count


def label_percentage(rows):
    pers_label = {}
    count_label = label_count(rows)
    total = sum([i for i in count_label.values()])
    for label, count in count_label.items():
        pers_label[label] = count / total
    return pers_label


def buildTree(rows: list, algorithm, stop):
    gain, question = best_split(rows)
    if gain == 0:
        pers_label = label_percentage(rows)
        return Leaf(predictions=pers_label)
    left_brach, right_brach = partition(rows, question)

    left = buildTree(left_brach)
    right = buildTree(right_brach)
    return Node(question, left, right)


class Node:
    def __init__(self, data, left, right) -> None:
        self.data = data
        self.left = left
        self.right = right

    def predict(self):
        # TODO
        pass


class CarRecord:
    def __init__(self, buying, maint, doors, persons, lug_boot, safety, label=None) -> None:
        self.buying = buying
        self.maint = maint
        self.doors = doors
        self.persons = persons
        self.lug_boot = lug_boot
        self.safety = safety
        self.label = label

    def __repr__(self):
        return 'buying: %s\tmaint: %s\tdoors: %s\t persons: %s\tlug_boot: %s\t safety: %s\tlabel:%s' \
               % (self.buying, self.maint, self.doors, self.persons, self.lug_boot, self.safety, self.label)


def read_file_data(path: str):
    cars = []
    with open(path, 'r') as f:
        for row in csv.reader(f):
            car = CarRecord(
                buying=row[0],
                maint=row[1],
                doors=row[2],
                persons=row[3],
                lug_boot=row[4],
                safety=row[5]
            )
            cars.append(car)
            print(car)

        # Build tree (node root)
        # Use Entropy
        root = buildTree(rows=cars, algorithm='entropy_gain', stop='end')

        # Predict on data was split

        # return data_f


def main():
    print('--- S T A R T ---')
    data = read_file_data('./data/car.data')
    print('--- D O N E ---')


if __name__ == '__main__':
    main()
