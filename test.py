
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
        self.predictions = class_counts(rows)


class Decision_Node:
    """ A Decision None asks a question. """

    def __init__(self, question, true_branch, false_branch) -> None:
        self.question = question
        self.true_branch = true_branch
        self.false_branch = false_branch

def gini(rows):

    labels = class_counts(rows)
    impurity = 1
    len_rows = len(rows)    # Total current sample 
    for name_label in labels:
        probability_of_label = labels[name_label] / len_rows
        impurity -= probability_of_label ** 2
    return impurity

def info_gain(left, right, current_uncertainty):
    # left is true_rows
    # right is false_rows
    info = 0    
    
    p_left = len(left) / (len(left) + len(right)) # probability left
    p_right = 1 - p_left  # probability right
    info = current_uncertainty - (p_left * gini(left) + p_right * gini(right))
    return info


def find_best_split(rows):
    """ 
    Find the best question to ask by iterating over every feature
    and calculating the information gain
    """
    best_info_gain = 0
    best_question = None
    current_uncertainty = gini(rows)
    number_column = len(header) - 1

    for column in range(number_column):
        values = unique_values(rows, column)
        for value in values:
            _question = Question(column, value)

            # Splitting the dataset
            true_rows, false_rows = partition(rows, _question)

            # Skip the split if it does not divide the dataset.
            if len(true_rows) == 0 or len(false_rows) == 0:
                continue

            # Calculate the information gain from this split
            _info_gain = info_gain(true_rows, false_rows, current_uncertainty)

            if _info_gain >= best_info_gain:
                best_info_gain, best_question = _info_gain, _question

    return best_info_gain, best_question


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

def classify(row, node):
    """See the 'rules of recursion' above."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        return node.predictions

    # Decide whether to follow the true-branch or the false-branch.
    # Compare the feature / value stored in the node,
    # to the example we're considering.
    if node.question.match(row):
        return classify(row, node.true_branch)
    else:
        return classify(row, node.false_branch)


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

def print_tree(node, spacing=""):
    """World's most elegant tree printing function."""

    # Base case: we've reached a leaf
    if isinstance(node, Leaf):
        print (spacing + "Predict", node.predictions)
        return

    # Print the question at this node
    print (spacing + str(node.question))

    # Call this function recursively on the true branch
    print (spacing + '--> True:')
    print_tree(node.true_branch, spacing + "  ")

    # Call this function recursively on the false branch
    print (spacing + '--> False:')
    print_tree(node.false_branch, spacing + "  ")


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

    print_tree(my_tree)
    # print(Question(0, 'Green'))
    # print(Question(1, 3))


