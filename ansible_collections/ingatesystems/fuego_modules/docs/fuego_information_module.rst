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

.. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ingatesystems.fuego_modules.fuego_information -- Retrieve information from an Ingate SBC.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `ingatesystems.fuego_modules collection <https://galaxy.ansible.com/ingatesystems/fuego_modules>`_ (version 1.0.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install ingatesystems.fuego_modules`.

    To use it in a playbook, specify: :code:`ingatesystems.fuego_modules.fuego_information`.

.. version_added

.. versionadded:: 1.0.0 of ingatesystems.fuego_modules

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Retrieve information from an Ingate SBC.


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
  <tr class="row-odd">
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
  <tr class="row-even">
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
  <tr class="row-odd">
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
  <tr class="row-even">
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
  <tr class="row-odd">
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
  <tr class="row-even">
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
  <tr class="row-odd">
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
  <tr class="row-even">
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

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-error"></div>
      <p class="ansible-option-title"><strong>error</strong></p>
      <a class="ansibleOptionLink" href="#parameter-error" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List all errors in all tables in the preliminary configuration.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-table_describe"></div>
      <p class="ansible-option-title"><strong>table_describe</strong></p>
      <a class="ansibleOptionLink" href="#parameter-table_describe" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Describe all configuration tables, listing its columns and their types.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-table_list"></div>
      <p class="ansible-option-title"><strong>table_list</strong></p>
      <a class="ansibleOptionLink" href="#parameter-table_list" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List all tables.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-unit"></div>
      <p class="ansible-option-title"><strong>unit</strong></p>
      <a class="ansibleOptionLink" href="#parameter-unit" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Retrieve information about the unit.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  </tbody>
  </table>



.. Attributes


.. Notes

Notes
-----

.. note::
   - This module requires that the Ingate Python SDK is installed on the host. To install the SDK use the pip command from your shell \ :literal:`pip install ingatesdk`\ .

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
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
      <div class="ansibleOptionAnchor" id="return-error"></div>
      <p class="ansible-option-title"><strong>error</strong></p>
      <a class="ansibleOptionLink" href="#return-error" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of error(s) found in the the preliminary configuration</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>error</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-error/error"></div>
      <p class="ansible-option-title"><strong>error</strong></p>
      <a class="ansibleOptionLink" href="#return-error/error" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Error information</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-error/error/column"></div>
      <p class="ansible-option-title"><strong>column</strong></p>
      <a class="ansibleOptionLink" href="#return-error/error/column" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Column name</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "lower_ip_dns"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-error/error/err_id"></div>
      <p class="ansible-option-title"><strong>err_id</strong></p>
      <a class="ansibleOptionLink" href="#return-error/error/err_id" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Error number</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 4</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-error/error/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-error/error/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Error message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "No value given."</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-error/error/rowid"></div>
      <p class="ansible-option-title"><strong>rowid</strong></p>
      <a class="ansibleOptionLink" href="#return-error/error/rowid" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">integer</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Row number</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> 1</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-error/error/table"></div>
      <p class="ansible-option-title"><strong>table</strong></p>
      <a class="ansibleOptionLink" href="#return-error/error/table" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Table name</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "firewall.network_groups"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-error/error/type"></div>
      <p class="ansible-option-title"><strong>type</strong></p>
      <a class="ansibleOptionLink" href="#return-error/error/type" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Type of error</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "VALUE_MISSING"</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-error/href"></div>
      <p class="ansible-option-title"><strong>href</strong></p>
      <a class="ansibleOptionLink" href="#return-error/href" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The REST API URL to the affected row</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "http://192.168.1.1/api/v1/misc/dns_servers/1"</p>
    </div></td>
  </tr>

  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_describe"></div>
      <p class="ansible-option-title"><strong>table_describe</strong></p>
      <a class="ansibleOptionLink" href="#return-table_describe" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Description of tables and associated information</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>table_describe</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_describe/table"></div>
      <p class="ansible-option-title"><strong>table</strong></p>
      <a class="ansibleOptionLink" href="#return-table_describe/table" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Table information</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_describe/table/href"></div>
      <p class="ansible-option-title"><strong>href</strong></p>
      <a class="ansibleOptionLink" href="#return-table_describe/table/href" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The REST API URL to the table</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "http://192.168.1.1/api/v1/misc/dns_servers"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_describe/table/info"></div>
      <p class="ansible-option-title"><strong>info</strong></p>
      <a class="ansibleOptionLink" href="#return-table_describe/table/info" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Column names and associated datatype</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> {"cert": "OptPrivCert", "name": "Name"}</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_describe/table/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#return-table_describe/table/name" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The name of the table</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "misc.dns_servers"</p>
    </div></td>
  </tr>


  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_list"></div>
      <p class="ansible-option-title"><strong>table_list</strong></p>
      <a class="ansibleOptionLink" href="#return-table_list" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>List of tables and associated information</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>table_list</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_list/table"></div>
      <p class="ansible-option-title"><strong>table</strong></p>
      <a class="ansibleOptionLink" href="#return-table_list/table" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Table information</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_list/table/href"></div>
      <p class="ansible-option-title"><strong>href</strong></p>
      <a class="ansibleOptionLink" href="#return-table_list/table/href" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The REST API URL to the table</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "http://192.168.1.1/api/v1/misc/dns_servers"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_list/table/methods"></div>
      <p class="ansible-option-title"><strong>methods</strong></p>
      <a class="ansibleOptionLink" href="#return-table_list/table/methods" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>A list of allowed HTTP methods</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "GET"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_list/table/name"></div>
      <p class="ansible-option-title"><strong>name</strong></p>
      <a class="ansibleOptionLink" href="#return-table_list/table/name" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The name of the table</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "misc.dns_servers"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-table_list/table/sdk_methods"></div>
      <p class="ansible-option-title"><strong>sdk_methods</strong></p>
      <a class="ansibleOptionLink" href="#return-table_list/table/sdk_methods" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>A list of allowed SDK methods</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "add_row"</p>
    </div></td>
  </tr>


  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit"></div>
      <p class="ansible-option-title"><strong>unit</strong></p>
      <a class="ansibleOptionLink" href="#return-unit" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Information about the unit</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>unit</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/installid"></div>
      <p class="ansible-option-title"><strong>installid</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/installid" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The installation identifier</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "any"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/interfaces"></div>
      <p class="ansible-option-title"><strong>interfaces</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/interfaces" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>List of interface names</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "eth0 eth1 eth2 eth3 eth4 eth5"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/lang"></div>
      <p class="ansible-option-title"><strong>lang</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/lang" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The unit&#x27;s language</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "en"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/lic_email"></div>
      <p class="ansible-option-title"><strong>lic_email</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/lic_email" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>License email information</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "example@example.com"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/lic_mac"></div>
      <p class="ansible-option-title"><strong>lic_mac</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/lic_mac" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>License MAC information</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "any"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/lic_name"></div>
      <p class="ansible-option-title"><strong>lic_name</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/lic_name" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>License name information</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Example Inc"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/macaddr"></div>
      <p class="ansible-option-title"><strong>macaddr</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/macaddr" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The MAC address of the first interface</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "52:54:00:4c:e2:07"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/mode"></div>
      <p class="ansible-option-title"><strong>mode</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/mode" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Operational mode of the unit</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Siparator"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/modules"></div>
      <p class="ansible-option-title"><strong>modules</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/modules" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Installed module licenses</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "failover vpn sip qturn ems qos rsc voipsm"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/patches"></div>
      <p class="ansible-option-title"><strong>patches</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/patches" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Installed patches on the unit</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> []</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/product"></div>
      <p class="ansible-option-title"><strong>product</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/product" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The product name</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Software SIParator/Firewall"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/serial"></div>
      <p class="ansible-option-title"><strong>serial</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/serial" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The serial number of the unit</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "IG-200-839-2008-0"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/systemid"></div>
      <p class="ansible-option-title"><strong>systemid</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/systemid" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The system identifier of the unit</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "IG-200-839-2008-0"</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/unitname"></div>
      <p class="ansible-option-title"><strong>unitname</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/unitname" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The name of the unit</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Testname"</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-unit/version"></div>
      <p class="ansible-option-title"><strong>version</strong></p>
      <a class="ansibleOptionLink" href="#return-unit/version" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Firmware version</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "6.2.0-beta2"</p>
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

