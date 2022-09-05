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
    fuego_information,
)


class TestInformationModule(TestIngateModule):

    module = fuego_information

    def setUp(self):
        super(TestInformationModule, self).setUp()

        self.mock_make_request = patch('ansible_collections.ingatesystems.'
                                       'fuego_modules.plugins.modules.'
                                       'fuego_information.make_request')
        self.make_request = self.mock_make_request.start()

    def tearDown(self):
        super(TestInformationModule, self).tearDown()
        self.mock_make_request.stop()

    def load_fixtures(self, fixture=None, command=None, changed=False):
        self.make_request.side_effect = [(changed, command,
                                          load_fixture(fixture))]

    def test_fuego_information_unit(self):
        """Test retrieving unit information.
        """
        command = 'unit'
        set_module_args(
            dict(
                client=dict(
                    version='v1',
                    address='127.0.0.1',
                    scheme='http',
                    username='alice',
                    password='foobar'
                ),
                unit=True,
            )
        )
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=False, fixture=fixture,
                                     command=command)
        self.assertFalse(result['changed'])
        self.assertTrue(command in result)
        data = result[command].get('installid', '')
        self.assertTrue('4ac6959f41a164abf0a518c4a83d93835fd7b174' in data)

    def test_fuego_information_error(self):
        """Test retrieving error information.
        """
        command = 'error'
        set_module_args(
            dict(
                client=dict(
                    version='v1',
                    address='127.0.0.1',
                    scheme='http',
                    username='alice',
                    password='foobar'
                ),
                error=True,
            )
        )
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=False, fixture=fixture,
                                     command=command)
        self.assertFalse(result['changed'])
        self.assertTrue(command in result)
        data = result[command][0][command].get('table', '')
        self.assertTrue('misc.dns_servers' in data)

    def test_fuego_information_table_describe(self):
        """Test retrieving table descriptions.
        """
        command = 'table_describe'
        set_module_args(
            dict(
                client=dict(
                    version='v1',
                    address='127.0.0.1',
                    scheme='http',
                    username='alice',
                    password='foobar'
                ),
                table_describe=True,
            )
        )
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=False, fixture=fixture,
                                     command=command)
        self.assertFalse(result['changed'])
        self.assertTrue(command in result)
        data = result[command][0].get('table', '')
        info = data['info'].get('call_duration', '')
        self.assertTrue(info == 'TestuaDurationLimit')

    def test_fuego_information_table_list(self):
        """Test listing tables.
        """
        command = 'table_list'
        set_module_args(
            dict(
                client=dict(
                    version='v1',
                    address='127.0.0.1',
                    scheme='http',
                    username='alice',
                    password='foobar'
                ),
                table_list=True,
            )
        )
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=False, fixture=fixture,
                                     command=command)
        self.assertFalse(result['changed'])
        self.assertTrue(command in result)
        data = result[command][0].get('table', '')
        name = data.get('name', '')
        self.assertTrue(name == 'webgui.trunk_selection')
