# coding: utf-8

from __future__ import absolute_import

from . import BaseTestCase
from six import BytesIO
from flask import json


class TestDefaultController(BaseTestCase):
    """ DefaultController integration test stubs """

    def test_correlatefield_get(self):
        """
        Test case for correlatefield_get

        
        """
        data = dict(netcdf_source1='netcdf_source1_example',
                    netcdf_source2='netcdf_source2_example',
                    frequency='frequency_example',
                    average='average_example',
                    var='var_example',
                    netcdf_target='netcdf_target_example')
        response = self.client.open('/climexp//correlatefield/',
                                    method='GET',
                                    data=data)
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
