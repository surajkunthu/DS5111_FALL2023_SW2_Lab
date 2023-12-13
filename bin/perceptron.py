"""
Module docstring
"""
class Perceptron:
    """
    Perceptron class docstring
    """

    def __init__(self):
        """
        Initialize perceptron
        """
        self._weights = None

    def train(self, inputs, labels):
        """
        train() function docstring
        """
        dummied_inputs = [inpx + [-1] for inpx in inputs]
        self._weights = [0.2] * len(dummied_inputs[0])

        for _ in range(5000):
            for dummy_input, label in zip(dummied_inputs, labels):
                label_delta = label - self.predict(dummy_input)
                for index, item in enumerate(dummy_input):
                    self._weights[index] += .1 * item * label_delta

    def predict(self, dummy_input):
        """
        predict() function docstring
        """
        if len(dummy_input) == 0:
            return None
        dummy_input = dummy_input + [-1]
        return int(0 < sum([x[0]*x[1] for x in zip(self._weights, dummy_input)])) #pylint: disable=R1728
