# Docstrings are used for code documentation. Docstrings explains what a function
# and class is needed for. It describes the arguments and output etc. It is different from
# a comment because comments are for those who want to modify the code whereas docstrings are
# for those who wants to use the code.

def increment(n):
    """
    This function takes an integer argument and increment it.

    :param n: Takes an integer as input.
    :return: Increment a number.
    """
    n += 1
    return n


incremented_num = increment(5)
print(incremented_num)
# Annotations
# The above method is without annotations. Python is dynamically typed so we don't need to provide
# types explicitly. With annotations, we can do that.


def increment_annotations(n: int) -> int:
    n += 1
    return n


print(increment_annotations(9))
