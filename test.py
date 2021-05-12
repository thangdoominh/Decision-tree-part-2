
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


class Leaf:
    """ A Leaf node classifies data. """

    def __init__(self, rows) -> None:
        self.prediction = None


class Decision_Node:
    """ A Decision None asks a question. """

    def __init__(self, question, true_branch, false_branch) -> None:
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch



def build_tree(rows):
    """ Builds the tree. """


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
