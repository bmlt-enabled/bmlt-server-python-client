# coding: utf-8

"""
    BMLT

    BMLT Admin API Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bmlt_client.models.validation_error import ValidationError

class TestValidationError(unittest.TestCase):
    """ValidationError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ValidationError:
        """Test ValidationError
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ValidationError`
        """
        model = ValidationError()
        if include_optional:
            return ValidationError(
                message = 'The field is required. (and 1 more error)',
                errors = {
                    'key' : [
                        'error details'
                        ]
                    }
            )
        else:
            return ValidationError(
                message = 'The field is required. (and 1 more error)',
                errors = {
                    'key' : [
                        'error details'
                        ]
                    },
        )
        """

    def testValidationError(self):
        """Test ValidationError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
