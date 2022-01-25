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

.. raw:: html

  <table class="colwidths-auto ansible-option-table docutils align-default" style="width: 100%">
  <thead>
  <tr class="row-odd">
    <th class="head"><p>Parameter</p></th>
    <th class="head"><p>Comments</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-add"></div>
      <p class="ansible-option-title"><strong>add</strong></p>
      <a class="ansibleOptionLink" href="#parameter-add" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Add a row to a table.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client"></div>
      <p class="ansible-option-title"><strong>client</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A dict object containing connection details.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client/address"></div>
      <p class="ansible-option-title"><strong>address</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client/address" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The hostname or IP address to the unit.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client/password"></div>
      <p class="ansible-option-title"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client/password" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The password for the REST API user.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client/port"></div>
      <p class="ansible-option-title"><strong>port</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client/port" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Which HTTP(S) port to connect to.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client/scheme"></div>
      <p class="ansible-option-title"><strong>scheme</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client/scheme" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Which HTTP protocol to use.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">http</span></p></li>
        <li><p><span class="ansible-option-choices-entry">https</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client/timeout"></div>
      <p class="ansible-option-title"><strong>timeout</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client/timeout" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The timeout (in seconds) for REST API requests.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client/username"></div>
      <p class="ansible-option-title"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client/username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
        / <span class="ansible-option-required">required</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The username of the REST API user.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client/validate_certs"></div>
      <div class="ansibleOptionAnchor" id="parameter-client/verify_ssl"></div>
      <p class="ansible-option-title"><strong>validate_certs</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client/validate_certs" title="Permalink to this option"></a>
      <p class="ansible-option-type-line"><span class="ansible-option-aliases">aliases: verify_ssl</p>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Verify the unit&#x27;s HTTPS certificate.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-default-bold">yes</span> <span class="ansible-option-default">← (default)</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-client/version"></div>
      <p class="ansible-option-title"><strong>version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-client/version" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>REST API version.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">v1</span> <span class="ansible-option-default">← (default)</span></p></li>
      </ul>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-columns"></div>
      <p class="ansible-option-title"><strong>columns</strong></p>
      <a class="ansibleOptionLink" href="#parameter-columns" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A dict containing column names/values.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-delete"></div>
      <p class="ansible-option-title"><strong>delete</strong></p>
      <a class="ansibleOptionLink" href="#parameter-delete" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Delete all rows in a table or a specific row.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-download"></div>
      <p class="ansible-option-title"><strong>download</strong></p>
      <a class="ansibleOptionLink" href="#parameter-download" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Download the configuration database from the unit.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-factory"></div>
      <p class="ansible-option-title"><strong>factory</strong></p>
      <a class="ansibleOptionLink" href="#parameter-factory" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Reset the preliminary configuration to its factory defaults.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-filename"></div>
      <p class="ansible-option-title"><strong>filename</strong></p>
      <a class="ansibleOptionLink" href="#parameter-filename" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The name of the file to store the downloaded configuration in. Refer to the <code class='docutils literal notranslate'>download</code> option.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-get"></div>
      <p class="ansible-option-title"><strong>get</strong></p>
      <a class="ansibleOptionLink" href="#parameter-get" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Return all rows in a table or a specific row.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-modify"></div>
      <p class="ansible-option-title"><strong>modify</strong></p>
      <a class="ansibleOptionLink" href="#parameter-modify" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Modify a row in a table.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-no_response"></div>
      <p class="ansible-option-title"><strong>no_response</strong></p>
      <a class="ansibleOptionLink" href="#parameter-no_response" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Expect no response when storing the preliminary configuration. Refer to the <code class='docutils literal notranslate'>store</code> option.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">no</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-path"></div>
      <p class="ansible-option-title"><strong>path</strong></p>
      <a class="ansibleOptionLink" href="#parameter-path" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Where in the filesystem to store the downloaded configuration. Refer to the <code class='docutils literal notranslate'>download</code> option.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-return_rowid"></div>
      <p class="ansible-option-title"><strong>return_rowid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-return_rowid" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Get rowid(s) from a table where the columns match.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-revert"></div>
      <p class="ansible-option-title"><strong>revert</strong></p>
      <a class="ansibleOptionLink" href="#parameter-revert" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Reset the preliminary configuration.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-rowid"></div>
      <p class="ansible-option-title"><strong>rowid</strong></p>
      <a class="ansibleOptionLink" href="#parameter-rowid" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A row id.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-store"></div>
      <p class="ansible-option-title"><strong>store</strong></p>
      <a class="ansibleOptionLink" href="#parameter-store" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Store the preliminary configuration.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-store_download"></div>
      <p class="ansible-option-title"><strong>store_download</strong></p>
      <a class="ansibleOptionLink" href="#parameter-store_download" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>If the downloaded configuration should be stored on disk. Refer to the <code class='docutils literal notranslate'>download</code> option.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-default-bold">no</span> <span class="ansible-option-default">← (default)</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-table"></div>
      <p class="ansible-option-title"><strong>table</strong></p>
      <a class="ansibleOptionLink" href="#parameter-table" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The name of the table.</p>
    </div></td>
  </tr>
  </tbody>
  </table>



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

.. raw:: html

  <table class="colwidths-auto ansible-option-table docutils align-default" style="width: 100%">
  <thead>
  <tr class="row-odd">
    <th class="head"><p>Key</p></th>
    <th class="head"><p>Description</p></th>
  </tr>
  </thead>
  <tbody>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-add"></div>
      <p class="ansible-option-title"><strong>add</strong></p>
      <a class="ansibleOptionLink" href="#return-add" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A list containing information about the added row</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>add</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-add/data"></div>
      <p class="ansible-option-title"><strong>data</strong></p>
      <a class="ansibleOptionLink" href="#return-add/data" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Column names/values</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> {"number": "2", "server": "10.48.254.33"}</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-add/href"></div>
      <p class="ansible-option-title"><strong>href</strong></p>
      <a class="ansibleOptionLink" href="#return-add/href" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The REST API URL to the added row</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "http://192.168.1.1/api/v1/misc/dns_servers/2"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-add/id"></div>
      <p class="ansible-option-title"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#return-add/id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The row id</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 22</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-delete"></div>
      <p class="ansible-option-title"><strong>delete</strong></p>
      <a class="ansibleOptionLink" href="#return-delete" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A list containing information about the deleted row(s)</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>delete</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-delete/data"></div>
      <p class="ansible-option-title"><strong>data</strong></p>
      <a class="ansibleOptionLink" href="#return-delete/data" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Column names/values</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> {"number": "2", "server": "10.48.254.33"}</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-delete/id"></div>
      <p class="ansible-option-title"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#return-delete/id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The row id</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 22</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-delete/table"></div>
      <p class="ansible-option-title"><strong>table</strong></p>
      <a class="ansibleOptionLink" href="#return-delete/table" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The name of the table</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "misc.dns_servers"</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-download"></div>
      <p class="ansible-option-title"><strong>download</strong></p>
      <a class="ansibleOptionLink" href="#return-download" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Configuration database and meta data</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>download</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-download/config"></div>
      <p class="ansible-option-title"><strong>config</strong></p>
      <a class="ansibleOptionLink" href="#return-download/config" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The configuration database</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-download/filename"></div>
      <p class="ansible-option-title"><strong>filename</strong></p>
      <a class="ansibleOptionLink" href="#return-download/filename" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>A suggested name for the configuration</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "testname_2018-10-01T214040.cfg"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-download/mimetype"></div>
      <p class="ansible-option-title"><strong>mimetype</strong></p>
      <a class="ansibleOptionLink" href="#return-download/mimetype" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The mimetype</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "application/x-config-database"</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-factory"></div>
      <p class="ansible-option-title"><strong>factory</strong></p>
      <a class="ansibleOptionLink" href="#return-factory" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>factory</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-factory/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-factory/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "reverted the configuration to the factory configuration."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-get"></div>
      <p class="ansible-option-title"><strong>get</strong></p>
      <a class="ansibleOptionLink" href="#return-get" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A list containing information about the row(s)</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>get</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-get/data"></div>
      <p class="ansible-option-title"><strong>data</strong></p>
      <a class="ansibleOptionLink" href="#return-get/data" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Column names/values</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> {"number": "2", "server": "10.48.254.33"}</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-get/href"></div>
      <p class="ansible-option-title"><strong>href</strong></p>
      <a class="ansibleOptionLink" href="#return-get/href" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The REST API URL to the row</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "http://192.168.1.1/api/v1/misc/dns_servers/1"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-get/id"></div>
      <p class="ansible-option-title"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#return-get/id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The row id</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 1</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-get/table"></div>
      <p class="ansible-option-title"><strong>table</strong></p>
      <a class="ansibleOptionLink" href="#return-get/table" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The name of the table</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Testname"</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-modify"></div>
      <p class="ansible-option-title"><strong>modify</strong></p>
      <a class="ansibleOptionLink" href="#return-modify" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A list containing information about the modified row</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>modify</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-modify/data"></div>
      <p class="ansible-option-title"><strong>data</strong></p>
      <a class="ansibleOptionLink" href="#return-modify/data" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Column names/values</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> {"number": "2", "server": "10.48.254.33"}</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-modify/href"></div>
      <p class="ansible-option-title"><strong>href</strong></p>
      <a class="ansibleOptionLink" href="#return-modify/href" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The REST API URL to the modified row</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "http://192.168.1.1/api/v1/misc/dns_servers/1"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-modify/id"></div>
      <p class="ansible-option-title"><strong>id</strong></p>
      <a class="ansibleOptionLink" href="#return-modify/id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The row id</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 10</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-modify/table"></div>
      <p class="ansible-option-title"><strong>table</strong></p>
      <a class="ansibleOptionLink" href="#return-modify/table" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The name of the table</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Testname"</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-return_rowid"></div>
      <p class="ansible-option-title"><strong>return_rowid</strong></p>
      <a class="ansibleOptionLink" href="#return-return_rowid" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The matched row id(s).</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>return_rowid</code> is yes and success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> [1, 3]</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-revert"></div>
      <p class="ansible-option-title"><strong>revert</strong></p>
      <a class="ansibleOptionLink" href="#return-revert" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>revert</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-revert/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-revert/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "reverted the configuration to the last applied configuration."</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-store"></div>
      <p class="ansible-option-title"><strong>store</strong></p>
      <a class="ansibleOptionLink" href="#return-store" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>store</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-store/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-store/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Successfully applied and saved the configuration."</p>
    </div></td>
  </tr>

  </tbody>
  </table>



..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Ingate Systems AB (@ingatesystems)



.. Parsing errors

