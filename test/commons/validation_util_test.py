from unittest import TestCase

import src.commons.validation_util as validation_util


class ValidationUtilTest(TestCase):

    def test_validate_not_blank_ok(self):
        response = validation_util.validate_not_blank(['test', 'demo'])
        self.assertIsNone(response)
