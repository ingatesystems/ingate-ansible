# Ansible Collection - Modules and Plugins for Managing an Ingate SBC

## Overview

This Ansible Collection can be installed via [Ansible Galaxy](https://galaxy.ansible.com)
and contains modules and plugins for managing an Ingate SIParator/Firewall.

## Requirements

* ansible >= 2.9
* ingatesdk

The [Ingate Python SDK](https://pypi.org/project/ingatesdk) can be installed by running
`pip install ingatesdk` from your shell.

## Installation

Enter the following command in your shell to install the collection via Ansible Galaxy:

`ansible-galaxy collection install ingatesystems.fuego_modules`

## Available Modules

* [fuego_config](https://ingatesystems.github.io/ingate-docs/ansible/fuego/html/fuego_config_module.html#ansible-collections-ingatesystems-fuego-modules-fuego-config-module) – Manage the configuration database on an Ingate SBC.
* [fuego_datetime](https://ingatesystems.github.io/ingate-docs/ansible/fuego/html/fuego_datetime_module.html#ansible-collections-ingatesystems-fuego-modules-fuego-datetime-module) – Manage date and time on an Ingate SBC.
* [fuego_information](https://ingatesystems.github.io/ingate-docs/ansible/fuego/html/fuego_information_module.html#ansible-collections-ingatesystems-fuego-modules-fuego-information-module) – Retrieve information from an Ingate SBC.
* [fuego_system](https://ingatesystems.github.io/ingate-docs/ansible/fuego/html/fuego_system_module.html#ansible-collections-ingatesystems-fuego-modules-fuego-system-module) – Manage system near functionality such as licenses, patches and upgrades on an Ingate SBC.

## Examples

### Using the fuego_config module
```
---
- name: Examples using fuego_config
  hosts: 192.168.1.1
  connection: local
  collections:
    - ingatesystems.fuego_modules
  gather_facts: no

  vars:
    client_rw:
      version: v1
      address: "{{ inventory_hostname }}"
      scheme: http
      username: userfoo
      password: mypwd

  tasks:
    - name: Revert to last known applied configuration
      fuego_config:
        client: "{{ client_rw }}"
        revert: true
      register: result
    - debug:
        var: result

    - name: Change the unit name
      fuego_config:
        client: "{{ client_rw }}"
        modify: true
        table: misc.unitname
        columns:
          unitname: sip_basic
      register: result
    - debug:
        var: result
```

### Using the fuego_datetime module
```
---
- name: Examples using fuego_datetime
  hosts: 192.168.1.1
  connection: local
  collections:
    - ingatesystems.fuego_modules
  gather_facts: no

  vars:
    client_rw:
      version: v1
      address: "{{ inventory_hostname }}"
      scheme: http
      username: userfoo
      password: mypwd

  tasks:
    - name: Get date, time and timezone
      fuego_datetime:
        client: "{{ client_rw }}"
        get: true
      register: result
    - debug:
        var: result
```

### Using the fuego_information module
```
---
- name: Examples using fuego_information
  hosts: 192.168.1.1
  connection: local
  collections:
    - ingatesystems.fuego_modules
  gather_facts: no

  vars:
    client_rw:
      version: v1
      address: "{{ inventory_hostname }}"
      scheme: http
      username: userfoo
      password: mypwd

  tasks:
    - name: Retrieve information about the unit
      fuego_information:
        client: "{{ client_rw }}"
        unit: true
      register: result
    - debug:
        var: result
```

### Using the fuego_system module
```
---
- name: Examples using fuego_system
  hosts: 192.168.1.1
  connection: local
  collections:
    - ingatesystems.fuego_modules
  gather_facts: no

  vars:
    client_rw:
      version: v1
      address: "{{ inventory_hostname }}"
      scheme: http
      username: userfoo
      password: mypwd

  tasks:
    - name: Upgrade to the latest version available
      fuego_system:
        client: "{{ client_rw }}"
        upgrade_download: true
        username: myaccount
        password: myaccountpwd
        latest: true
      register: result
    - debug:
        var: result
```

## Additional Resources

* [Complete Collection Documentation](https://ingatesystems.github.io/ingate-docs/ansible/fuego/html)
* [More Ansible Information and Examples](https://account.ingate.com/manuals/latest/reference_guide.html#_ansible)
* [Generate Ansible Playbook from an Ingate CLI backup file](https://raw.githubusercontent.com/ingatesystems/ingatesdk/master/utils/cli2python.py)
* [Ingate Session Border Controllers (SBCs)](https://www.ingate.com/session-border-controller-sbc)

## Copyright
Copyright 2022 Ingate Systems AB.

## License

See [license](LICENSE).
