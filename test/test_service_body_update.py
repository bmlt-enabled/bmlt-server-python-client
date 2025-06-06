# coding: utf-8

"""
    BMLT

    BMLT Admin API Documentation

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bmlt_client.models.service_body_update import ServiceBodyUpdate

class TestServiceBodyUpdate(unittest.TestCase):
    """ServiceBodyUpdate unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ServiceBodyUpdate:
        """Test ServiceBodyUpdate
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ServiceBodyUpdate`
        """
        model = ServiceBodyUpdate()
        if include_optional:
            return ServiceBodyUpdate(
                parent_id = 0,
                name = 'string',
                description = 'string',
                type = 'string',
                admin_user_id = 0,
                assigned_user_ids = [
                    0
                    ],
                url = 'string',
                helpline = 'string',
                email = 'string',
                world_id = 'string'
            )
        else:
            return ServiceBodyUpdate(
                parent_id = 0,
                name = 'string',
                description = 'string',
                type = 'string',
                admin_user_id = 0,
                assigned_user_ids = [
                    0
                    ],
        )
        """

    def testServiceBodyUpdate(self):
        """Test ServiceBodyUpdate"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
