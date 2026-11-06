"""Small calculator module with an intentional bug for the Acyclic swarm demo."""


def add(a, b):
    return a + b


def subtract(a, b):
    # BUG: should be a - b
    return b - a


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b
