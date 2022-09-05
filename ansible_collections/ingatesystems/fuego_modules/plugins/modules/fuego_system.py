#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright: (c) 2022, Ingate Systems AB
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


DOCUMENTATION = '''
---
module: fuego_system
short_description: Manage system near functionality such as licenses, patches
                   and upgrades on an Ingate SBC.
description:
  - Manage system near functionality such as licenses, patches
    and upgrades on an Ingate SBC.
version_added: '1.0.0'
extends_documentation_fragment:
  - ingatesystems.fuego_modules.common_options
options:
  license:
    description:
      - Download and install a license.
    type: bool
  patch:
    description:
      - Install a patch.
    type: bool
  upgrade:
    description:
      - Install a firmware upgrade.
    type: bool
  upgrade_accept:
    description:
      - Accept an upgrade after an upgrade has been installed.
    type: bool
  upgrade_abort:
    description:
      - Abort an upgrade after an upgrade has been installed.
    type: bool
  upgrade_downgrade:
    description:
      - Downgrade from a previously installed upgrade.
    type: bool
  upgrade_download:
    description:
      - Download and install a firmware upgrade. The upgrade(s) will be
        downloaded from the Ingate Websystem. You can upgrade to the latest
        patch, minor or major version. You can also specify a desired version
        that is available in the respective level.
    type: bool
  reboot:
    description:
      - Reboot the unit.
    type: bool
  opmode:
    description:
      - Set mode to siparator or firewall.
    type: bool
  username:
    description:
      - Username for account login on ingate.com. Must be set for C(license)
        and C(upgrade_download).
    type: str
  password:
    description:
      - Password for account login on ingate.com. Must be set for C(license)
        and C(upgrade_download).
    type: str
  liccode:
    description:
      - The license code (e.g. KRJM-Q625-FUVG). Must be set for C(license).
    type: str
  filename:
    description:
      - Path to a valid Ingate patch or upgrade file.
    type: str
  mode:
    description:
      - The operational mode.
    choices: [siparator, firewall]
    type: str
  version:
    description:
      - The the desired version to upgrade to.
    type: str
  latest_patch:
    description:
      - Upgrade to the latest patch level.
    type: bool
  latest_minor:
    description:
      - Upgrade to the latest minor level.
    type: bool
  latest_major:
    description:
      - Upgrade to the latest major level.
    type: bool
  latest:
    description:
      - Upgrade to the latest available version.
    type: bool
  restart_sip:
    version_added: '1.1.0'
    description:
      - Restart the SIP module and remove all state, like registrations etc.
    type: bool

notes:
  - The methods C(patch) and C(upgrade_download) assumes that the the
    preliminary configuration has been stored to the permanent configuration at
    least once (see module fuego_config C(store) method).
  - For the methods C(license) and C(upgrade_download) the Ansible host needs
    Internet connectivity.
  - When using the the C(upgrade) method the unit will reboot and you need
    to do C(upgrade accept) or C(upgrade_abort).
  - When changing operational mode using C(opmode), a reboot is required in
    order for the change to take effect.
author:
  - Ingate Systems AB (@ingatesystems)
'''

EXAMPLES = '''
# Install a license
- fuego_system:
    client: "{{ stored_client_data }}"
    license: true
    username: myusername
    password: mypassword
    liccode: 2STW-2UL8-JWJD

# Install a patch
- fuego_system:
    client: "{{ stored_client_data }}"
    patch: true
    filename: patch-6.2.1-rc2-vm2.fup

# Install an upgrade
- fuego_system:
    client: "{{ stored_client_data }}"
    upgrade: true
    filename: fupgrade.fup.any

# Accept an upgrade
- fuego_system:
    client: "{{ stored_client_data }}"
    upgrade_accept: true

# Abort an upgrade
- fuego_system:
    client: "{{ stored_client_data }}"
    upgrade_abort: true

# Downgrade an upgrade
- fuego_system:
    client: "{{ stored_client_data }}"
    upgrade_downgrade: true

# Upgrade to the latest version available
- fuego_system:
    client: "{{ stored_client_data }}"
    upgrade_download: true
    username: myusername
    password: mypassword
    latest: true

# Change the operational mode to Siparator
- fuego_system:
    client: "{{ stored_client_data }}"
    opmode: true
    mode: siparator

# Reboot the unit
- fuego_system:
    client: "{{ stored_client_data }}"
    reboot: true

# Restart the SIP module
- fuego_system:
    client: "{{ stored_client_data }}"
    restart_sip: true
'''

RETURN = '''
license:
  description: A list of information about the installed license.
  returned: when C(license) is yes and success
  type: list
  elements: dict
  contains:
    msg:
      description: Information regarding the installed license.
      returned: success
      type: str
      sample: Install a Base license.
patch:
  description: Information about the installed patch.
  returned: when C(patch) is yes and success
  type: str
  contains:
    msg:
      description: Patch information.
      returned: success
      type: str
      sample: Installed the patch patch-6.2.0-apipatch-1.fup (Test REST API 1).
upgrade:
  description: A command status message
  returned: when C(upgrade) is yes and success
  type: dict
  contains:
    msg:
      description: The command status message
      returned: success
      type: str
      sample: Rebooting with new version. Please contact the unit again once it has rebooted.
upgrade_accept:
  description: A command status message
  returned: when C(upgrade_accept) is yes and success
  type: dict
  contains:
    msg:
      description: The command status message
      returned: success
      type: str
      sample: Made the upgrade permanent.
upgrade_abort:
  description: A command status message
  returned: when C(upgrade_abort) is yes and success
  type: dict
  contains:
    msg:
      description: The command status message
      returned: success
      type: str
      sample: The upgrade has been removed. Rebooting..
upgrade_downgrade:
  description: A command status message
  returned: when C(upgrade_downgrade) is yes and success
  type: dict
  contains:
    msg:
      description: The command status message
      returned: success
      type: str
      sample: Downgrade in progress (6.2.0). Rebooting...
upgrade_download:
  description: A command status message
  returned: when C(upgrade_download) is yes and success
  type: dict
  contains:
    msg:
      description: The command status message
      returned: success
      type: str
      sample: Your unit is upgraded to the latest version (6.2.2)
reboot:
  description: A command status message
  returned: when C(reboot) is yes and success
  type: dict
  contains:
    msg:
      description: The command status message
      returned: success
      type: str
      sample: Rebooting the unit now...
opmode:
  description: A command status message
  returned: when C(opmode) is yes and success
  type: dict
  contains:
    msg:
      description: The command status message
      returned: success
      type: str
      sample: Operational mode set to siparator.
restart_sip:
  description: A command status message
  returned: when C(restart_sip) is yes and success
  type: dict
  contains:
    msg:
      description: The command status message
      returned: success
      type: str
      sample: Successfully restarted the SIP module.
'''

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_native
from ..module_utils.common import (ingate_argument_spec,
                                   ingate_create_client,
                                   exit_unknown_response,
                                   exit_empty_response,
                                   get_current_version,
                                   is_ingatesdk_installed)

try:
    from ingate import ingatesdk
except ImportError:
    pass


def make_request(module):
    # Create client and authenticate.
    api_client = ingate_create_client(**module.params)

    if module.params.get('license'):
        # Install a license.
        changed = False
        username = module.params.get('username')
        password = module.params.get('password')
        liccode = module.params.get('liccode')

        response = api_client.install_license(username, password, liccode)
        if response:
            try:
                response = response[0]['install-license']
                changed = True
            except Exception:
                exit_unknown_response(module, response)
            return changed, 'license', response
        else:
            exit_empty_response(module)
    elif module.params.get('patch'):
        # Install a patch.
        changed = False
        filename = module.params.get('filename')

        response = api_client.install_patch(filename)
        if response:
            try:
                response = response[0]['install-patch']
                changed = True
            except Exception:
                exit_unknown_response(module, response)
            return changed, 'patch', response
        else:
            exit_empty_response(module)
    elif module.params.get('upgrade'):
        # Install an upgrade.
        changed = False
        filename = module.params.get('filename')

        response = api_client.install_upgrade(filename)
        if response:
            try:
                response = response[0]['install-upgrade']
                changed = True
            except Exception:
                exit_unknown_response(module, response)
            # Wait for the unit to become available.
            api_client.wait_webserver(timeout=300)
            return changed, 'upgrade', response
        else:
            exit_empty_response(module)
    elif module.params.get('upgrade_accept'):
        # Accept the installed upgrade.
        changed = False

        response = api_client.accept_upgrade()
        if response:
            try:
                response = response[0]['accept-upgrade']
                changed = True
            except Exception:
                exit_unknown_response(module, response)
            return changed, 'upgrade_accept', response
        else:
            exit_empty_response(module)
    elif module.params.get('upgrade_abort'):
        # Abort the installed upgrade.
        changed = False

        response = api_client.abort_upgrade()
        if response:
            try:
                response = response[0]['abort-upgrade']
                changed = True
            except Exception:
                exit_unknown_response(module, response)
            return changed, 'upgrade_accept', response
        else:
            exit_empty_response(module)
    elif module.params.get('upgrade_downgrade'):
        # Downgrade a previously installed upgrade.
        changed = False

        response = api_client.downgrade_upgrade()
        if response:
            try:
                response = response[0]['downgrade-upgrade']
                changed = True
            except Exception:
                exit_unknown_response(module, response)
            return changed, 'upgrade_downgrade', response
        else:
            exit_empty_response(module)
    elif module.params.get('reboot'):
        # Reboot the unit.
        response = api_client.reboot()
        if response:
            try:
                response = response[0]['reboot']
            except Exception:
                exit_unknown_response(module, response)
            # Wait for the unit to become available.
            api_client.wait_webserver(timeout=300)
            return False, 'reboot', response
        else:
            exit_empty_response(module)
    elif module.params.get('opmode'):
        # Get the current operational mode.
        changed = False
        mode = module.params['mode']

        response = api_client.unit_information()
        try:
            info = response[0]['unit-information']
        except Exception:
            exit_unknown_response(module, response)
        if info:
            if info['mode'].lower() == mode.lower():
                response = {'msg': 'Operational mode is already %s.' % mode}
                return False, 'opmode', response
        else:
            exit_empty_response(module)

        # Change the operational mode.
        response = api_client.operational_mode(mode=mode)
        if response:
            try:
                response = response[0]['operational-mode']
                changed = True
            except Exception:
                exit_unknown_response(module, response)
            return changed, 'opmode', response
        else:
            exit_empty_response(module)
    elif module.params.get('upgrade_download'):
        # Store the current version.
        old_version = get_current_version(api_client)
        if not old_version:
            module.fail_json(msg='Failed to retrieve the running version.')

        # Download and install upgrade(s).
        changed = False
        username = module.params.get('username')
        password = module.params.get('password')
        version = module.params.get('version')
        latest_patch = module.params.get('latest_patch')
        latest_minor = module.params.get('latest_minor')
        latest_major = module.params.get('latest_major')
        latest = module.params.get('latest')
        response = (api_client.
                    download_install_upgrade(username, password,
                                             version=version,
                                             latest_patch=latest_patch,
                                             latest_minor=latest_minor,
                                             latest_major=latest_major,
                                             latest=latest))
        if response:
            try:
                response = response[0]['download-install-upgrade']
                current_version = get_current_version(api_client)
                if current_version != old_version:
                    changed = True
            except Exception:
                exit_unknown_response(module, response)
            return changed, 'upgrade_download', response
        else:
            exit_empty_response(module)
    elif module.params.get('restart_sip'):
        # Restart the SIP module.
        response = api_client.restart_sip()
        if response:
            try:
                response = response[0]['restart-sip']
            except Exception:
                exit_unknown_response(module, response)
            return True, 'restart_sip', response
        else:
            exit_empty_response(module)

    return False, '', {}


def main():
    argument_spec = ingate_argument_spec(
        license=dict(type='bool'),
        patch=dict(type='bool'),
        upgrade=dict(type='bool'),
        upgrade_accept=dict(type='bool'),
        upgrade_abort=dict(type='bool'),
        upgrade_downgrade=dict(type='bool'),
        upgrade_download=dict(type='bool'),
        reboot=dict(type='bool'),
        opmode=dict(type='bool'),
        username=dict(),
        password=dict(no_log=True),
        liccode=dict(),
        filename=dict(),
        mode=dict(choices=['siparator', 'firewall']),
        version=dict(),
        latest_patch=dict(type='bool'),
        latest_minor=dict(type='bool'),
        latest_major=dict(type='bool'),
        latest=dict(type='bool'),
        restart_sip=dict(type='bool'),
    )

    mutually_exclusive = [('license', 'patch', 'upgrade', 'upgrade_accept',
                           'upgrade_abort', 'upgrade_downgrade',
                           'upgrade_download', 'reboot', 'opmode',
                           'restart_sip')]
    required_one_of = [['license', 'patch', 'upgrade', 'upgrade_accept',
                        'upgrade_abort', 'upgrade_downgrade',
                        'upgrade_download', 'reboot', 'opmode', 'restart_sip']]
    required_if = [('license', True, ['username', 'password', 'liccode']),
                   ('patch', True, ['filename']),
                   ('upgrade', True, ['filename']),
                   ('opmode', True, ['mode']),
                   ('upgrade_download', True, ['username', 'password'])]

    module = AnsibleModule(argument_spec=argument_spec,
                           mutually_exclusive=mutually_exclusive,
                           required_if=required_if,
                           required_one_of=required_one_of,
                           supports_check_mode=False)

    # Additional argument checks for upgrade_download.
    if module.params.get('upgrade_download'):
        latest_major = module.params.get('latest_major')
        latest_minor = module.params.get('latest_minor')
        latest_patch = module.params.get('latest_patch')
        latest = module.params.get('latest')
        version = module.params.get('version')

        exclusive = [latest, latest_major, latest_minor, latest_patch]
        if len([x for x in exclusive if x]) > 1:
            module.fail_json(msg='latest, latest_patch, latest_minor and'
                             ' latest_major are mutually exclusive.')
        if not version and len([x for x in exclusive if x]) == 0:
            module.fail_json(msg='Need at least version and/or latest,'
                             ' latest_major, latest_minor or latest_patch.')
        if version and latest:
            module.fail_json(msg='latest and version are mutually exclusive.')

    is_ingatesdk_installed(module)

    result = dict(changed=False)
    try:
        changed, command, response = make_request(module)
        if response and command:
            result[command] = response
        result['changed'] = changed
    except ingatesdk.SdkError as e:
        module.fail_json(msg=to_native(e))
    module.exit_json(**result)


if __name__ == '__main__':
    main()
