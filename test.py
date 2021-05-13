
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


def unique_vals(rows, col):
    """ Find the unique values for a column in a dataset. """
    return set([row[col] for row in rows])


class Question:
    """ A Question is used to partition a dataset """

    def __init__(self, column, value) -> None:
        self.column = column
        self.value = value

    def match(self, example) -> bool:
        # Compare the feature value in an example to the
        # feature value in this question.
        val = example[self.column]
        if isinstance(val, int) or isinstance(val, float):
            return val > self.value
        return val == self.value


def class_counts(rows):
    pass

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

def find_best_split(self):
    """ 
    Find the best question to ask by iterating over every feature
    and calculating the information gain
    """

def partition(rows, question):
    pass

def build_tree(rows):
    """ Builds the tree. """

    gain, question = find_best_split(rows)


    # Condition Stop.
    # We can ask no further question.
    if gain == 0: return Leaf(rows)


    true_rows, false_rows = partition(rows, question)

    # Recursive the true_branch
    true_branch = build_tree(true_rows)

    # Recursive the false_branch
    false_branch = build_tree(false_branch)

    return Decision_Node(question, true_branch, false_branch)

if __name__ == '__main__':

    my_tree = build_tree(training_data)

    # Evaluate
    testing_data = [
        ['Green', 3, 'Apple'],
        ['Yellow', 4, 'Apple'],
        ['Red', 2, 'Grape'],
        ['Red', 1, 'Grape'],
        ['Yellow', 3, 'Lemon'],
    ]

    print(testing_data)
