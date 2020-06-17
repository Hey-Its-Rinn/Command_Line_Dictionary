import unittest
from unittest.mock import patch
from lib.funcs import lookup


class TestFuncs(unittest.TestCase):
    def test_lookup_succeeds_with_valid_params(self):
        """
        test lookup succeeds with valid params
        """

        # calls
        result = lookup('rain')

        # asserts
        self.assertEqual(result, [
        	"Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.",
        	"To fall from the clouds in drops of water."
        	]
        )

    def test_lookup_succeeds_with_valid_params_lower_returns_a_capitalized_key(self):
        """
        test lookup succeeds with valid params lower returns a capitalized key
        """

        # calls
        result = lookup('paris')

        # asserts
        self.assertEqual(result, ['The capital and largest city of France.'])

    def test_lookup_succeeds_with_valid_params_lower_returns_an_all_uppercase_key(self):
        """
        test lookup succeeds with valid params lower returns an all uppercase key
        """

        # calls
        result = lookup('usa')

        # asserts
        self.assertEqual(result, [
        	'A country and federal republic in North America located north of Mexico and south of Canada, ' + \
        	'including Alaska, Hawaii and overseas territories.'
        	]
        )

    @patch('builtins.input')
    def test_lookup_succeeds_with_valid_non_exact_params_y(self, mock_inputs):
        """
        test lookup succeeds with valid non-exact params y
        """

        # mocks
        mock_inputs.side_effect = 'y'

        # calls
        result = lookup('rainn')

        # asserts
        self.assertEqual(result, [
        	"Precipitation in the form of liquid water drops with diameters greater than 0.5 millimetres.",
        	"To fall from the clouds in drops of water."
        	]
        )

    @patch('builtins.input')
    def test_lookup_succeeds_with_valid_non_exact_params_n(self, mock_inputs):
        """
        test lookup succeeds with valid non-exact params n
        """

        # mocks
        mock_inputs.side_effect = 'n'

        # calls
        result = lookup('rainn')

        # asserts
        self.assertEqual(result, ['No word found.'])


if __name__ == '__main__':
    unittest.main()
