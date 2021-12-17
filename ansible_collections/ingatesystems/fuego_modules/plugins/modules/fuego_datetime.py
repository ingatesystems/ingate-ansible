#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright: (c) 2021, Ingate Systems AB
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = '''
---
module: fuego_datetime
short_description: Manage date and time on an Ingate SBC.
description:
  - Manage date and time on an Ingate SBC.
version_added: '1.0.0'
extends_documentation_fragment: ingate
options:
  set:
    description:
      - Set the current date, time and timezone.
    type: bool
  datetime:
    description:
      - A dict object containing time information. Use with C(set).
    suboptions:
      date:
        description:
          - A date. E.g. 2018-07-19.
      time:
        description:
          - A time. E.g. 11:59:59.
      zone:
        description:
          - A timezone. E.g. Europe/Stockholm.
  get:
    description:
      - Get the current date, time and timezone.
    type: bool
  timezone_list:
    description:
      - List all available timezones.
    type: bool
author:
  - Ingate Systems AB (@ingatesystems)
'''

EXAMPLES = '''
# Set date, time and timezone
- fuego_datetime:
    client: "{{ stored_client_data }}"
    set: true
    datetime:
      zone: "Europe/Stockholm"
      time: "18:00:00"
      date: "2019-02-12"

# name: Get date, time and timezone
- fuego_datetime:
    client: "{{ stored_client_data }}"
    get: true

# List all available timezones.
- fuego_datetime:
    client: "{{ stored_client_data }}"
    timezone_list: true
'''

RETURN = '''
set:
  description: Current date, time and timezone
  returned: when C(set) is yes and success
  type: complex
  contains:
    msg:
      description: Date, time and timezone information
      returned: success
      type: string
      sample: 2018-07-25 14:24:09 Europe/Stockholm
get:
  description: Current date, time and timezone
  returned: when C(get) is yes and success
  type: complex
  contains:
    msg:
      description: Date, time and timezone information
      returned: success
      type: string
      sample: 2018-07-25 14:25:09 Europe/Stockholm
timezone_list:
  description: List of available timezones
  returned: when C(timezone_list) is yes and success
  type: list
  contains:
    data:
      description: Zone information
      returned: success
      type: complex
      contains:
        zone:
          description: The name of the zone
          returned: success
          type: string
          sample: US/Michigan
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

    if module.params.get('set'):
        # Set current date, time and timezone.
        response = api_client.set_datetime(**module.params['datetime'])
        if response:
            try:
                response = response[0]['datetime']
            except Exception:
                exit_unknown_response(module, response)
            return True, 'set', response
        else:
            exit_empty_response(module)
    elif module.params.get('get'):
        # Get current date, time and timezone.
        response = api_client.get_datetime()
        if response:
            try:
                response = response[0]['datetime']
            except Exception:
                exit_unknown_response(module, response)
            return False, 'get', response
        else:
            exit_empty_response(module)
    elif module.params.get('timezone_list'):
        # List all available timezones.
        response = api_client.list_timezones()
        if response:
            return False, 'timezone_list', response
        else:
            exit_empty_response(module)

    return False, '', {}


def main():
    datetime_options = dict(
        date=dict(),
        time=dict(),
        zone=dict(),
    )
    argument_spec = ingate_argument_spec(
        set=dict(type='bool'),
        get=dict(type='bool'),
        timezone_list=dict(type='bool'),
        datetime=dict(type='dict', options=datetime_options),
    )

    mutually_exclusive = [('set', 'get', 'timezone_list')]
    required_one_of = [['set', 'get', 'timezone_list']]
    required_if = [('set', True, ['datetime'])]
    module = AnsibleModule(argument_spec=argument_spec,
                           mutually_exclusive=mutually_exclusive,
                           required_if=required_if,
                           required_one_of=required_one_of,
                           supports_check_mode=False)

    # Additional argument checks for set.
    if module.params.get('set') and not module.params.get('datetime'):
        module.fail_json(msg='Need at least one of date, time or zone.')

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
