
# Sample data
training_data = [
    ['Green', 3, 'Apple'],
    ['Yellow', 3, 'Apple'],
    ['Red', 1, 'Grape'],
    ['Red', 1, 'Grape'],
    ['Yellow', 3, 'Lemon'],
]

# Column labels
header = ["color", "diameter", "label"]


def unique_values(rows, col):
    """ Find the unique values for a column in a dataset. """
    return set([row[col] for row in rows])


class Question:
    """ A Question is used to partition a dataset """

    def __init__(self, column: int, value) -> None:
        self.column = column
        self.value = value

    def match(self, example) -> bool:
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if isinstance(val, int) or isinstance(val, float):
            return val > self.value
        return val == self.value

    def __repr__(self):
        condition = "=="
        if isinstance(self.value, int) or isinstance(self.value, float):
            condition = ">="
        return "Is %s %s %s?" % (header[self.column], condition, str(self.value))


def class_counts(rows):
    labels = {}
    for row in rows:
        name_label = row[-1]
        if not name_label in labels:
            labels[name_label] = 1
            continue
        labels[name_label] += 1
    return labels

class Leaf:
    """ A Leaf node classifies data. """

    def __init__(self, rows) -> None:
        self.prediction = class_counts(rows)


class Decision_Node:
    """ A Decision None asks a question. """

    def __init__(self, question, true_branch, false_branch) -> None:
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def gini(rows):

    labels = class_counts(rows)
    impurity = 1
    for label in labels:

    return

def info_gain(left, right, current_uncertainty):
    return

def find_best_split(rows):
    """ 
    Find the best question to ask by iterating over every feature
    and calculating the information gain
    """
    best_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    number_column = len(header)

    for column in range(number_column):
        values = unique_values(rows, column)
        for value in values:
            question = Question(column, value)

            # Splitting the dataset
            true_rows, false_rows = partition(rows, question)

            # Skip the split if it does not divide the dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            gain = info_gain


            # print(' %s: %s ' % (column, values) )

    return best_gain, best_question


def partition(rows, question):
    '''
    For each row in the dataset, check if it matches the question.
    If so, add it into "true_rows", otherwise, add it to "false_rows"
    '''
    true_rows, false_rows = [], []

    for row in rows:
        if question.match(row):
            true_rows.append(row)
        else:
            false_rows.append(row)

    return true_rows, false_rows


def build_tree(rows):
    """ Builds the tree. """

    gain, question = find_best_split(rows)

    # Condition Stop.
    # We can ask no further question.
    if gain == 0:
        return Leaf(rows)

    true_rows, false_rows = partition(rows, question)

    # Recursive the true_branch
    true_branch = build_tree(true_rows)

    # Recursive the false_branch
    false_branch = build_tree(false_rows)

    return Decision_Node(question, true_branch, false_branch)


if __name__ == '__main__':

    # my_tree = build_tree(training_data)

    # Evaluate
    testing_data = [
        ['Green', 3, 'Apple'],
        ['Yellow', 4, 'Apple'],
        ['Red', 2, 'Grape'],
        ['Red', 1, 'Grape'],
        ['Yellow', 3, 'Lemon'],
    ]

    test = class_counts(testing_data)

    print(test)
    print(Question(0, 'Green'))
    print(Question(1, 3))


