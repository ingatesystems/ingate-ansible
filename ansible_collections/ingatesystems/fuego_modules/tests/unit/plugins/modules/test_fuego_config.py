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
    fuego_config,
)


class TestConfigModule(TestIngateModule):

    module = fuego_config

    def setUp(self):
        super(TestConfigModule, self).setUp()

        self.mock_make_request = patch('ansible_collections.ingatesystems.'
                                       'fuego_modules.plugins.modules.'
                                       'fuego_config.make_request')
        self.make_request = self.mock_make_request.start()

    def tearDown(self):
        super(TestConfigModule, self).tearDown()
        self.mock_make_request.stop()

    def load_fixtures(self, fixture=None, command=None, changed=False):
        self.make_request.side_effect = [(changed, command,
                                          load_fixture(fixture))]

    def test_fuego_config_add(self):
        """Test adding a row to a table.
        """
        command = 'add'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            add=True,
            table='misc.dns_servers',
            columns=dict(
                server='192.168.1.23'
            )))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)

    def test_fuego_config_delete(self):
        """Test deleting all rows in a table.
        """
        command = 'delete'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            delete=True,
            table='misc.dns_servers',
        ))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)

    def test_fuego_config_get(self):
        """Test returning all rows in a table.
        """
        command = 'get'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            get=True,
            table='misc.dns_servers',
        ))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)

    def test_fuego_config_modify(self):
        """Test modifying a row.
        """
        command = 'modify'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            modify=True,
            table='misc.unitname',
            columns=dict(
                unitname='"Testapi - 1541699806"'
            )))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)

    def test_fuego_config_revert(self):
        """Test reverting the preliminary configuration.
        """
        command = 'revert'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            revert=True
        ))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)

    def test_fuego_config_factory(self):
        """Test loading factory defaults.
        """
        command = 'factory'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            factory=True
        ))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)

    def test_fuego_config_store(self):
        """Test storing the preliminary configuration.
        """
        command = 'store'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            store=True
        ))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)

    def test_fuego_config_download(self):
        """Test doing backup of configuration database.
        """
        command = 'store'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            download=True
        ))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)

    def test_fuego_config_return_rowid(self):
        """Test retrieving a row id.
        """
        command = 'return_rowid'
        set_module_args(dict(
            client=dict(
                version='v1',
                address='127.0.0.1',
                scheme='http',
                username='alice',
                password='foobar'
            ),
            return_rowid=True,
            table='network.local_nets',
            columns=dict(
                interface='eth0'
            )))
        fixture = '%s_%s.%s' % (os.path.basename(__file__).split('.')[0],
                                command, 'json')
        result = self.execute_module(changed=True, fixture=fixture,
                                     command=command)
        self.assertTrue(command in result)
