# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_shoes_get(self):
        """Test case for shoes_get

        
        """
        response = self.client.open(
            '/v1/shoes',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shoes_id_delete(self):
        """Test case for shoes_id_delete

        
        """
        response = self.client.open(
            '/v1/shoes/{id}'.format(id=789),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shoes_id_put(self):
        """Test case for shoes_id_put

        
        """
        name = 'name_example'
        response = self.client.open(
            '/v1/shoes/{id}'.format(id=789),
            method='PUT',
            data=json.dumps(name),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_shoes_post(self):
        """Test case for shoes_post

        
        """
        name = 'name_example'
        response = self.client.open(
            '/v1/shoes',
            method='POST',
            data=json.dumps(name),
            content_type='text/plain; charset=utf-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
