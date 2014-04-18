import romanesco
import unittest

class TestR(unittest.TestCase):

    def setUp(self):
        self.array_out = {
            "inputs": [],
            "outputs": [{"name": "output", "type": "r", "format": "object"}],
            "script": "output = c(1,2,3)",
            "mode": "r"
        }

        self.array_in = {
            "inputs": [{"name": "input", "type": "r", "format": "object"}],
            "outputs": [{"name": "output", "type": "r", "format": "object"}],
            "script": "output = c(input, c(4,5))",
            "mode": "r"
        }

        self.function_out = {
            "inputs": [],
            "outputs": [{"name": "output", "type": "r", "format": "object"}],
            "script": "output = function (x) {\nreturn(x * x)\n}",
            "mode": "r"
        }

        self.function_in = {
            "inputs": [{"name": "input", "type": "r", "format": "object"}],
            "outputs": [{"name": "output", "type": "number", "format": "number"}],
            "script": "output = input(4)",
            "mode": "r"
        }

    def test_array(self):
        outputs = romanesco.run(self.array_out, inputs={}, outputs={"output": {"format": "serialized"}})
        self.assertEqual(outputs["output"]["data"], "A\n2\n196610\n131840\n14\n3\n1\n2\n3\n")

        outputs = romanesco.run(self.array_in, inputs={"input": outputs["output"]}, outputs={"output": {"format": "serialized"}})
        self.assertEqual(outputs["output"]["data"], "A\n2\n196610\n131840\n14\n5\n1\n2\n3\n4\n5\n")

    def test_function(self):
        outputs = romanesco.run(self.function_out, inputs={}, outputs={"output": {"format": "serialized"}})
        self.assertEqual(outputs["output"]["data"], "A\n2\n196610\n131840\n1027\n253\n1026\n1\n262153\n1\nx\n251\n254\n6\n1\n262153\n1\n{\n2\n6\n1\n262153\n6\nreturn\n2\n6\n1\n262153\n1\n*\n2\n511\n2\n511\n254\n254\n254\n")

        outputs = romanesco.run(self.function_in, inputs={"input": outputs["output"]})
        self.assertEqual(outputs["output"]["data"], 16)

if __name__ == '__main__':
    unittest.main()