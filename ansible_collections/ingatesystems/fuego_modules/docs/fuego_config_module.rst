.. Document meta

:orphan:

.. |antsibull-internal-nbsp| unicode:: 0xA0
    :trim:

.. role:: ansible-attribute-support-label
.. role:: ansible-attribute-support-property
.. role:: ansible-attribute-support-full
.. role:: ansible-attribute-support-partial
.. role:: ansible-attribute-support-none
.. role:: ansible-attribute-support-na
.. role:: ansible-option-type
.. role:: ansible-option-elements
.. role:: ansible-option-required
.. role:: ansible-option-versionadded
.. role:: ansible-option-aliases
.. role:: ansible-option-choices
.. role:: ansible-option-choices-entry
.. role:: ansible-option-default
.. role:: ansible-option-default-bold
.. role:: ansible-option-configuration
.. role:: ansible-option-returned-bold
.. role:: ansible-option-sample-bold

.. Anchors

.. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ingatesystems.fuego_modules.fuego_config -- Manage the configuration database on an Ingate SBC.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `ingatesystems.fuego_modules collection <https://galaxy.ansible.com/ingatesystems/fuego_modules>`_ (version 1.0.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install ingatesystems.fuego_modules`.

    To use it in a playbook, specify: :code:`ingatesystems.fuego_modules.fuego_config`.

.. version_added

.. versionadded:: 1.0.0 of ingatesystems.fuego_modules

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Manage the configuration database on an Ingate SBC.


.. Aliases


.. Requirements

Requirements
------------
The below requirements are needed on the host that executes this module.

- ingatesdk >= 1.0.6


.. Options

Parameters
----------

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-add"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-add:

      .. rst-class:: ansible-option-title

      **add**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-add" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Add a row to a table.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client:

      .. rst-class:: ansible-option-title

      **client**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dict object containing connection details.


      .. raw:: html

        </div>
    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client/address"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/address:

      .. rst-class:: ansible-option-title

      **address**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client/address" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The hostname or IP address to the unit.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client/password"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client/password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The password for the REST API user.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client/port"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/port:

      .. rst-class:: ansible-option-title

      **port**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client/port" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Which HTTP(S) port to connect to.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client/scheme"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/scheme:

      .. rst-class:: ansible-option-title

      **scheme**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client/scheme" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Which HTTP protocol to use.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`http`
      - :ansible-option-choices-entry:`https`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client/timeout"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/timeout:

      .. rst-class:: ansible-option-title

      **timeout**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client/timeout" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The timeout (in seconds) for REST API requests.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client/username"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/username:

      .. rst-class:: ansible-option-title

      **username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client/username" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string` / :ansible-option-required:`required`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The username of the REST API user.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client/validate_certs"></div>
        <div class="ansibleOptionAnchor" id="parameter-client/verify_ssl"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/validate_certs:
      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/verify_ssl:

      .. rst-class:: ansible-option-title

      **validate_certs**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client/validate_certs" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-aliases:`aliases: verify_ssl`

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Verify the unit's HTTPS certificate.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-default-bold:`yes` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client/version"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-client/version:

      .. rst-class:: ansible-option-title

      **version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-client/version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      REST API version.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`v1` :ansible-option-default:`← (default)`

      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-columns"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-columns:

      .. rst-class:: ansible-option-title

      **columns**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-columns" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A dict containing column names/values.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-delete"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-delete:

      .. rst-class:: ansible-option-title

      **delete**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-delete" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Delete all rows in a table or a specific row.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-download"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-download:

      .. rst-class:: ansible-option-title

      **download**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-download" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Download the configuration database from the unit.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-factory"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-factory:

      .. rst-class:: ansible-option-title

      **factory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-factory" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reset the preliminary configuration to its factory defaults.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-filename"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-filename:

      .. rst-class:: ansible-option-title

      **filename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-filename" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name of the file to store the downloaded configuration in. Refer to the \ :literal:`download`\  option.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-get"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-get:

      .. rst-class:: ansible-option-title

      **get**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-get" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Return all rows in a table or a specific row.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-modify"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-modify:

      .. rst-class:: ansible-option-title

      **modify**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-modify" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Modify a row in a table.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-no_response"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-no_response:

      .. rst-class:: ansible-option-title

      **no_response**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-no_response" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Expect no response when storing the preliminary configuration. Refer to the \ :literal:`store`\  option.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-path"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-path:

      .. rst-class:: ansible-option-title

      **path**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-path" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Where in the filesystem to store the downloaded configuration. Refer to the \ :literal:`download`\  option.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-return_rowid"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-return_rowid:

      .. rst-class:: ansible-option-title

      **return_rowid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-return_rowid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Get rowid(s) from a table where the columns match.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-revert"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-revert:

      .. rst-class:: ansible-option-title

      **revert**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-revert" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reset the preliminary configuration.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-rowid"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-rowid:

      .. rst-class:: ansible-option-title

      **rowid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-rowid" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A row id.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-store"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-store:

      .. rst-class:: ansible-option-title

      **store**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-store" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Store the preliminary configuration.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-store_download"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-store_download:

      .. rst-class:: ansible-option-title

      **store_download**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-store_download" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      If the downloaded configuration should be stored on disk. Refer to the \ :literal:`download`\  option.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-default-bold:`no` :ansible-option-default:`← (default)`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-table"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__parameter-table:

      .. rst-class:: ansible-option-title

      **table**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-table" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The name of the table.


      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - If \ :literal:`store\_download`\  is set to True, and \ :literal:`path`\  and \ :literal:`filename`\  is omitted, the file will be stored in the current directory with an automatic filename.
   - This module requires that the Ingate Python SDK is installed on the host. To install the SDK use the pip command from your shell \ :literal:`pip install ingatesdk`\ .

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
    - name: Add/remove DNS servers
      hosts: 192.168.1.1
      connection: local
      vars:
        client_rw:
          version: v1
          address: "{{ inventory_hostname }}"
          scheme: http
          username: alice
          password: foobar
      tasks:

      - name: Load factory defaults
        fuego_config:
          client: "{{ client_rw }}"
          factory: true
        register: result
      - debug:
          var: result

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
            unitname: "Test Ansible"
        register: result
      - debug:
          var: result

      - name: Add a DNS server
        fuego_config:
          client: "{{ client_rw }}"
          add: true
          table: misc.dns_servers
          columns:
            server: 192.168.1.21
        register: result
      - debug:
          var: result

      - name: Add a DNS server
        fuego_config:
          client: "{{ client_rw }}"
          add: true
          table: misc.dns_servers
          columns:
            server: 192.168.1.22
        register: result
      - debug:
          var: result

      - name: Add a DNS server
        fuego_config:
          client: "{{ client_rw }}"
          add: true
          table: misc.dns_servers
          columns:
            server: 192.168.1.23
        register: last_dns
      - debug:
          var: last_dns

      - name: Modify the last added DNS server
        fuego_config:
          client: "{{ client_rw }}"
          modify: true
          table: misc.dns_servers
          rowid: "{{ last_dns['add'][0]['id'] }}"
          columns:
            server: 192.168.1.24
        register: result
      - debug:
          var: result

      - name: Return the last added DNS server
        fuego_config:
          client: "{{ client_rw }}"
          get: true
          table: misc.dns_servers
          rowid: "{{ last_dns['add'][0]['id'] }}"
        register: result
      - debug:
          var: result

      - name: Remove last added DNS server
        fuego_config:
          client: "{{ client_rw }}"
          delete: true
          table: misc.dns_servers
          rowid: "{{ last_dns['add'][0]['id'] }}"
        register: result
      - debug:
          var: result

      - name: Return the all rows from table misc.dns_servers
        fuego_config:
          client: "{{ client_rw }}"
          get: true
          table: misc.dns_servers
        register: result
      - debug:
          var: result

      - name: Remove remaining DNS servers
        fuego_config:
          client: "{{ client_rw }}"
          delete: true
          table: misc.dns_servers
        register: result
      - debug:
          var: result

      - name: Get rowid for interface eth0
        fuego_config:
          client: "{{ client_rw }}"
          return_rowid: true
          table: network.local_nets
          columns:
            interface: eth0
        register: result
      - debug:
          var: result

      - name: Store the preliminary configuration
        fuego_config:
          client: "{{ client_rw }}"
          store: true
        register: result
      - debug:
          var: result

      - name: Do backup of the configuration database
        fuego_config:
          client: "{{ client_rw }}"
          download: true
          store_download: true
        register: result
      - debug:
          var: result




.. Facts


.. Return values

Return Values
-------------
Common return values are documented :ref:`here <common_return_values>`, the following are the fields unique to this module:

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-add"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-add:

      .. rst-class:: ansible-option-title

      **add**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-add" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A list containing information about the added row


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`add`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-add/data"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-add/data:

      .. rst-class:: ansible-option-title

      **data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-add/data" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Column names/values


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` {"number": "2", "server": "10.48.254.33"}


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-add/href"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-add/href:

      .. rst-class:: ansible-option-title

      **href**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-add/href" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The REST API URL to the added row


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "http://192.168.1.1/api/v1/misc/dns\_servers/2"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-add/id"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-add/id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-add/id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The row id


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 22


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-delete"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-delete:

      .. rst-class:: ansible-option-title

      **delete**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-delete" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A list containing information about the deleted row(s)


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`delete`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-delete/data"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-delete/data:

      .. rst-class:: ansible-option-title

      **data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-delete/data" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Column names/values


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` {"number": "2", "server": "10.48.254.33"}


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-delete/id"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-delete/id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-delete/id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The row id


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 22


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-delete/table"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-delete/table:

      .. rst-class:: ansible-option-title

      **table**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-delete/table" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the table


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "misc.dns\_servers"


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-download"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-download:

      .. rst-class:: ansible-option-title

      **download**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-download" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Configuration database and meta data


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`download`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-download/config"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-download/config:

      .. rst-class:: ansible-option-title

      **config**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-download/config" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The configuration database


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-download/filename"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-download/filename:

      .. rst-class:: ansible-option-title

      **filename**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-download/filename" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A suggested name for the configuration


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "testname\_2018-10-01T214040.cfg"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-download/mimetype"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-download/mimetype:

      .. rst-class:: ansible-option-title

      **mimetype**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-download/mimetype" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The mimetype


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "application/x-config-database"


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-factory"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-factory:

      .. rst-class:: ansible-option-title

      **factory**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-factory" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`factory`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-factory/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-factory/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-factory/msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "reverted the configuration to the factory configuration."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-get"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-get:

      .. rst-class:: ansible-option-title

      **get**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-get" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A list containing information about the row(s)


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`get`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-get/data"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-get/data:

      .. rst-class:: ansible-option-title

      **data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-get/data" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Column names/values


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` {"number": "2", "server": "10.48.254.33"}


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-get/href"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-get/href:

      .. rst-class:: ansible-option-title

      **href**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-get/href" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The REST API URL to the row


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "http://192.168.1.1/api/v1/misc/dns\_servers/1"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-get/id"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-get/id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-get/id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The row id


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 1


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-get/table"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-get/table:

      .. rst-class:: ansible-option-title

      **table**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-get/table" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the table


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Testname"


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-modify"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-modify:

      .. rst-class:: ansible-option-title

      **modify**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-modify" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A list containing information about the modified row


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`modify`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-modify/data"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-modify/data:

      .. rst-class:: ansible-option-title

      **data**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-modify/data" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Column names/values


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` {"number": "2", "server": "10.48.254.33"}


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-modify/href"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-modify/href:

      .. rst-class:: ansible-option-title

      **href**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-modify/href" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The REST API URL to the modified row


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "http://192.168.1.1/api/v1/misc/dns\_servers/1"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-modify/id"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-modify/id:

      .. rst-class:: ansible-option-title

      **id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-modify/id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The row id


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 10


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-modify/table"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-modify/table:

      .. rst-class:: ansible-option-title

      **table**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-modify/table" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the table


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Testname"


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-return_rowid"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-return_rowid:

      .. rst-class:: ansible-option-title

      **return_rowid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-return_rowid" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The matched row id(s).


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`return\_rowid`\  is yes and success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` [1, 3]


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-revert"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-revert:

      .. rst-class:: ansible-option-title

      **revert**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-revert" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`revert`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-revert/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-revert/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-revert/msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "reverted the configuration to the last applied configuration."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-store"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-store:

      .. rst-class:: ansible-option-title

      **store**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-store" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`store`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-store/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_config_module__return-store/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-store/msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Successfully applied and saved the configuration."


      .. raw:: html

        </div>




..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Ingate Systems AB (@ingatesystems)



.. Parsing errors

