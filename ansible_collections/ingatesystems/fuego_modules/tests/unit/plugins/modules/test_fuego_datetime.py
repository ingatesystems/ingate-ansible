# -*- coding: utf-8 -*-
#
# Copyright: (c) 2022, Ingate Systems AB
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import os

from ansible_collections.ingatesystems.fuego_modules.tests.unit.compat.mock import patch
from ansible_collections.ingatesystems.fuego_modules.tests.unit.plugins.modules.utils import (
    set_module_args,
)
from .ingate_module import TestIngateModule, load_fixture
from ansible_collections.ingatesystems.fuego_modules.plugins.modules import (
    fuego_datetime,
)


class TestDateTimeModule(TestIngateModule):

    module = fuego_datetime

    def setUp(self):
        super(TestDateTimeModule, self).setUp()

        self.mock_make_request = patch('ansible_collections.ingatesystems.'
                                       'fuego_modules.plugins.modules.'
                                       'fuego_datetime.make_request')
        self.make_request = self.mock_make_request.start()

    def tearDown(self):
        super(TestDateTimeModule, self).tearDown()
        self.mock_make_request.stop()

    def load_fixtures(self, fixture=None, command=None, changed=False):
        self.make_request.side_effect = [(changed, command,
                                          load_fixture(fixture))]

    def test_fuego_datetime_set(self):
        """Test setting date, time and timezone.
        """
        command = 'set'
        set_module_args(
            dict(
                client=dict(
                    version='v1',
                    address='127.0.0.1',
                    scheme='http',
                    username='alice',
                    password='foobar'
                ),
                set=True,
                datetime=dict(
                    zone='Europe/Stockholm',
                    time='18:00:00',
                    date='2022-01-27'
                ),
            )
        )
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(result['changed'])
        self.assertTrue(command in result)
        data = result[command].get('msg', '')
        self.assertTrue(data == '2022-01-26 18:00:01 Europe/Stockholm')

    def test_fuego_datetime_get(self):
        """Test getting date, time and timezone.
        """
        command = 'get'
        set_module_args(
            dict(
                client=dict(
                    version='v1',
                    address='127.0.0.1',
                    scheme='http',
                    username='alice',
                    password='foobar'
                ),
                get=True,
                datetime=dict(
                    zone='Europe/Stockholm',
                    time='18:00:00',
                    date='2022-01-27'
                ),
            )
        )
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=False, fixture=fixture,
                                     command=command)
        self.assertFalse(result['changed'])
        self.assertTrue(command in result)
        data = result[command].get('msg', '')
        self.assertTrue(data == '2022-01-26 18:15:47 Europe/Stockholm')

    def test_fuego_datetime_timezone_list(self):
        """Test listing timezones.
        """
        command = 'timezone_list'
        set_module_args(
            dict(
                client=dict(
                    version='v1',
                    address='127.0.0.1',
                    scheme='http',
                    username='alice',
                    password='foobar'
                ),
                timezone_list=True,
            )
        )
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=False, fixture=fixture,
                                     command=command)
        self.assertFalse(result['changed'])
        self.assertTrue(command in result)
        zone = result[command][0]['data'].get('zone', '')
        self.assertTrue(zone == 'US/Samoa')
