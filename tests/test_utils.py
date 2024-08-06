import logging
import json

import pytest
from unittest import TestCase
from pdflc.utils import get_page_numbers


LOG = logging.getLogger(__name__)


class GetPageNumbersTest(TestCase):
    """Test case of function to get page numbers parsed from a pattern"""

    def setUp(self):
        ...

    def test_normal_case(self):
        """We test the normal case"""
        inputs = ['1, 2, 3, 4,5',
                  '1-10',
                  '1, 5-9, 30, 44, 12-14',
                  '1, 1-3, 2-3, 5,']
        target = [[0, 1, 2, 3, 4],
                  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                  [0, 4, 5, 6, 7, 8, 11, 12, 13, 29, 43],
                  [0, 1, 2, 4]]

        for inp, tar in zip(inputs, target):
            output = get_page_numbers(inp)

            self.assertIsInstance(output, list)
            self.assertEqual(output, tar)

