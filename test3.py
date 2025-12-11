
class Number:
    """
    A class to represent an integer and perform various operations on it.
    """

    def __init__(self, value: int):
        """
        Initialize the Number instance with an integer value.
        Raise a TypeError if the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("Only integers are allowed.")
        self.value = value

    def double(self) -> int:
        """Return the double of the number."""
        return self.value * 2

    def triple(self) -> int:
        """Return the triple of the number."""
        return self.value * 3

    def quadruple(self) -> int:
        """Return the quadruple of the number."""
        return self.value * 4

    def halve(self) -> float:
        """Return half of the number."""
        return self.value / 2

    def evaluate(self) -> dict:
        """
        Evaluate the number for various properties:
        - Even or odd
        - Divisibility by 3
        - Positive, negative, or zero

        Returns:
            A dictionary with the evaluation results.
        """
        results = {
            "even_or_odd": "even" if self.value % 2 == 0 else "odd",
            "divisible_by_3": "divisible by 3" if self.value % 3 == 0 else "not divisible by 3",
            "sign": (
                "positive" if self.value > 0 else
                "negative" if self.value < 0 else
                "zero"
            ),
        }
        return results




print(Number(-45).evaluate())

print(Number(98).evaluate())

print(Number(721).evaluate())

print(Number(0).evaluate())
