# !/usr/bin/env python
# -*- coding:utf-8 -*-

import unittest

from base import BaseTestCase


class TestMainBlueprint(BaseTestCase):

    def test_index(self):
        # Ensure Flask is setup.
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Docker Cloud Demo', response.data)


if __name__ == '__main__':
    unittest.main()