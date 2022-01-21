#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright: (c) 2022, Ingate Systems AB
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = '''
---
module: fuego_information
short_description: Retrieve information from an Ingate SBC.
description:
  - Retrieve information from an Ingate SBC.
version_added: '1.0.0'
extends_documentation_fragment:
  - ingatesystems.fuego_modules.common_options
options:
  unit:
    description:
      - Retrieve information about the unit.
    type: bool
  error:
    description:
      - List all errors in all tables in the preliminary configuration.
    type: bool
  table_describe:
    description:
      - Describe all configuration tables, listing its columns and their types.
    type: bool
  table_list:
    description:
      - List all tables.
    type: bool
author:
  - Ingate Systems AB (@ingatesystems)
'''

EXAMPLES = '''
# Retrieve information about the unit
- fuego_information:
    client: "{{ stored_client_data }}"
    unit: true

# List current configuration error(s)
- fuego_information:
    client: "{{ stored_client_data }}"
    error: true

# Describe all tables
- fuego_information:
    client: "{{ stored_client_data }}"
    table_describe: true

# List all tables
- fuego_information:
    client: "{{ stored_client_data }}"
    table_list: true
'''

RETURN = '''
unit:
  description: Information about the unit
  returned: when C(unit) is yes and success
  type: complex
  contains:
    installid:
      description: The installation identifier
      returned: success
      type: str
      sample: any
    interfaces:
      description: List of interface names
      returned: success
      type: str
      sample: eth0 eth1 eth2 eth3 eth4 eth5
    lang:
      description: The unit's language
      returned: success
      type: str
      sample: en
    lic_email:
      description: License email information
      returned: success
      type: str
      sample: example@example.com
    lic_mac:
      description: License MAC information
      returned: success
      type: str
      sample: any
    lic_name:
      description: License name information
      returned: success
      type: str
      sample: Example Inc
    macaddr:
      description: The MAC address of the first interface
      returned: success
      type: str
      sample: 52:54:00:4c:e2:07
    mode:
      description: Operational mode of the unit
      returned: success
      type: str
      sample: Siparator
    modules:
      description: Installed module licenses
      returned: success
      type: str
      sample: failover vpn sip qturn ems qos rsc voipsm
    patches:
      description: Installed patches on the unit
      returned: success
      type: list
      sample: []
    product:
      description: The product name
      returned: success
      type: str
      sample: Software SIParator/Firewall
    serial:
      description: The serial number of the unit
      returned: success
      type: str
      sample: IG-200-839-2008-0
    systemid:
      description: The system identifier of the unit
      returned: success
      type: str
      sample: IG-200-839-2008-0
    unitname:
      description: The name of the unit
      returned: success
      type: str
      sample: Testname
    version:
      description: Firmware version
      returned: success
      type: str
      sample: 6.2.0-beta2
error:
  description: List of error(s) found in the the preliminary configuration
  returned: when C(error) is yes and success
  type: list
  elements: dict
  contains:
    href:
      description: The REST API URL to the affected row
      returned: success
      type: str
      sample: http://192.168.1.1/api/v1/misc/dns_servers/1
    error:
      description: Error information
      returned: success
      type: complex
      contains:
        column:
          description: Column name
          returned: success
          type: str
          sample: lower_ip_dns
        err_id:
          description: Error number
          returned: success
          type: int
          sample: 4
        msg:
          description: Error message
          returned: success
          type: str
          sample: No value given.
        rowid:
          description: Row number
          returned: success
          type: int
          sample: 1
        table:
          description: Table name
          returned: success
          type: str
          sample: firewall.network_groups
        type:
          description: Type of error
          returned: success
          type: str
          sample: VALUE_MISSING
table_describe:
  description: Description of tables and associated information
  returned: when C(table_describe) is yes and success
  type: list
  contains:
    table:
      description: Table information
      returned: success
      type: complex
      contains:
        name:
          description: The name of the table
          returned: success
          type: str
          sample: misc.dns_servers
        href:
          description: The REST API URL to the table
          returned: success
          type: str
          sample: http://192.168.1.1/api/v1/misc/dns_servers
        info:
          description: Column names and associated datatype
          returned: success
          type: complex
          sample: {'cert': 'OptPrivCert', 'name': 'Name'}
table_list:
  description: List of tables and associated information
  returned: when C(table_list) is yes and success
  type: list
  contains:
    table:
      description: Table information
      returned: success
      type: complex
      contains:
        name:
          description: The name of the table
          returned: success
          type: str
          sample: misc.dns_servers
        href:
          description: The REST API URL to the table
          returned: success
          type: str
          sample: http://192.168.1.1/api/v1/misc/dns_servers
        sdk_methods:
          description: A list of allowed SDK methods
          returned: success
          type: list
          sample: add_row
        methods:
          description: A list of allowed HTTP methods
          returned: success
          type: list
          sample: GET
'''

from ansible.module_utils.basic import AnsibleModule
from ..module_utils.common import (ingate_argument_spec,
                                   ingate_create_client,
                                   exit_unknown_response,
                                   exit_empty_response,
                                   is_ingatesdk_installed)

try:
    from ingate import ingatesdk
except ImportError:
    pass


def make_request(module):
    # Create client and authenticate.
    api_client = ingate_create_client(**module.params)

    if module.params.get('unit'):
        # Get unit information.
        response = api_client.unit_information()
        if response:
            try:
                response = response[0]['unit-information']
            except Exception:
                exit_unknown_response(module, response)
            return False, 'unit', response
        else:
            exit_empty_response(module)
    elif module.params.get('error'):
        # List current configuration error(s).
        response = api_client.list_errors()
        return False, 'error', response
    elif module.params.get('table_describe'):
        # Describe all tables.
        response = api_client.describe_tables()
        if response:
            return False, 'table_describe', response
        else:
            exit_empty_response(module)
    elif module.params.get('table_list'):
        # List all tables.
        response = api_client.list_tables()
        if response:
            return False, 'table_list', response
        else:
            exit_empty_response(module)

    return False, '', {}


def main():
    argument_spec = ingate_argument_spec(
        unit=dict(type='bool'),
        error=dict(type='bool'),
        table_describe=dict(type='bool'),
        table_list=dict(type='bool'),
    )

    mutually_exclusive = [('unit', 'error', 'table_describe', 'table_list')]
    module = AnsibleModule(argument_spec=argument_spec,
                           mutually_exclusive=mutually_exclusive,
                           supports_check_mode=False)

    is_ingatesdk_installed(module)

    result = dict(changed=False)
    try:
        changed, command, response = make_request(module)
        if response and command:
            result[command] = response
        result['changed'] = changed
    except ingatesdk.SdkError as e:
        module.fail_json(msg=str(e))
    module.exit_json(**result)


if __name__ == '__main__':
    main()
