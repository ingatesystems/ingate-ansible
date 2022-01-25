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

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Parameter
    - Comments

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-client"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/address:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/password:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/port:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/scheme:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/timeout:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/username:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/validate_certs:
      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/verify_ssl:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-client/version:

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
        <div class="ansibleOptionAnchor" id="parameter-error"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-error:

      .. rst-class:: ansible-option-title

      **error**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-error" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List all errors in all tables in the preliminary configuration.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-table_describe"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-table_describe:

      .. rst-class:: ansible-option-title

      **table_describe**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-table_describe" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Describe all configuration tables, listing its columns and their types.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-table_list"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-table_list:

      .. rst-class:: ansible-option-title

      **table_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-table_list" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List all tables.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-unit"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__parameter-unit:

      .. rst-class:: ansible-option-title

      **unit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-unit" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Retrieve information about the unit.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>


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

.. rst-class:: ansible-option-table

.. list-table::
  :width: 100%
  :widths: auto
  :header-rows: 1

  * - Key
    - Description

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error:

      .. rst-class:: ansible-option-title

      **error**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of error(s) found in the the preliminary configuration


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`error`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error/error"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error/error:

      .. rst-class:: ansible-option-title

      **error**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error/error" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Error information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error/error/column"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error/error/column:

      .. rst-class:: ansible-option-title

      **column**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error/error/column" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Column name


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "lower\_ip\_dns"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error/error/err_id"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error/error/err_id:

      .. rst-class:: ansible-option-title

      **err_id**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error/error/err_id" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Error number


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 4


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error/error/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error/error/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error/error/msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Error message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "No value given."


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error/error/rowid"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error/error/rowid:

      .. rst-class:: ansible-option-title

      **rowid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error/error/rowid" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`integer`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Row number


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` 1


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error/error/table"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error/error/table:

      .. rst-class:: ansible-option-title

      **table**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error/error/table" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Table name


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "firewall.network\_groups"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error/error/type"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error/error/type:

      .. rst-class:: ansible-option-title

      **type**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error/error/type" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Type of error


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "VALUE\_MISSING"


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-error/href"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-error/href:

      .. rst-class:: ansible-option-title

      **href**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-error/href" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The REST API URL to the affected row


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "http://192.168.1.1/api/v1/misc/dns\_servers/1"


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_describe"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_describe:

      .. rst-class:: ansible-option-title

      **table_describe**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_describe" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Description of tables and associated information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`table\_describe`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_describe/table"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_describe/table:

      .. rst-class:: ansible-option-title

      **table**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_describe/table" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Table information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_describe/table/href"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_describe/table/href:

      .. rst-class:: ansible-option-title

      **href**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_describe/table/href" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The REST API URL to the table


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "http://192.168.1.1/api/v1/misc/dns\_servers"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_describe/table/info"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_describe/table/info:

      .. rst-class:: ansible-option-title

      **info**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_describe/table/info" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Column names and associated datatype


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` {"cert": "OptPrivCert", "name": "Name"}


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_describe/table/name"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_describe/table/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_describe/table/name" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

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
        <div class="ansibleOptionAnchor" id="return-table_list"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_list:

      .. rst-class:: ansible-option-title

      **table_list**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_list" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      List of tables and associated information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`table\_list`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_list/table"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_list/table:

      .. rst-class:: ansible-option-title

      **table**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_list/table" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Table information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_list/table/href"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_list/table/href:

      .. rst-class:: ansible-option-title

      **href**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_list/table/href" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The REST API URL to the table


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "http://192.168.1.1/api/v1/misc/dns\_servers"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_list/table/methods"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_list/table/methods:

      .. rst-class:: ansible-option-title

      **methods**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_list/table/methods" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A list of allowed HTTP methods


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "GET"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_list/table/name"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_list/table/name:

      .. rst-class:: ansible-option-title

      **name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_list/table/name" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the table


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "misc.dns\_servers"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-table_list/table/sdk_methods"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-table_list/table/sdk_methods:

      .. rst-class:: ansible-option-title

      **sdk_methods**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-table_list/table/sdk_methods" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      A list of allowed SDK methods


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "add\_row"


      .. raw:: html

        </div>




  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit:

      .. rst-class:: ansible-option-title

      **unit**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information about the unit


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`unit`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/installid"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/installid:

      .. rst-class:: ansible-option-title

      **installid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/installid" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The installation identifier


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "any"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/interfaces"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/interfaces:

      .. rst-class:: ansible-option-title

      **interfaces**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/interfaces" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      List of interface names


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "eth0 eth1 eth2 eth3 eth4 eth5"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/lang"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/lang:

      .. rst-class:: ansible-option-title

      **lang**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/lang" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The unit's language


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "en"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/lic_email"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/lic_email:

      .. rst-class:: ansible-option-title

      **lic_email**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/lic_email" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      License email information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "example@example.com"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/lic_mac"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/lic_mac:

      .. rst-class:: ansible-option-title

      **lic_mac**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/lic_mac" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      License MAC information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "any"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/lic_name"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/lic_name:

      .. rst-class:: ansible-option-title

      **lic_name**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/lic_name" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      License name information


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Example Inc"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/macaddr"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/macaddr:

      .. rst-class:: ansible-option-title

      **macaddr**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/macaddr" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The MAC address of the first interface


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "52:54:00:4c:e2:07"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/mode"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/mode" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Operational mode of the unit


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Siparator"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/modules"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/modules:

      .. rst-class:: ansible-option-title

      **modules**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/modules" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Installed module licenses


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "failover vpn sip qturn ems qos rsc voipsm"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/patches"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/patches:

      .. rst-class:: ansible-option-title

      **patches**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/patches" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Installed patches on the unit


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` []


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/product"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/product:

      .. rst-class:: ansible-option-title

      **product**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/product" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The product name


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Software SIParator/Firewall"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/serial"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/serial:

      .. rst-class:: ansible-option-title

      **serial**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/serial" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The serial number of the unit


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "IG-200-839-2008-0"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/systemid"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/systemid:

      .. rst-class:: ansible-option-title

      **systemid**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/systemid" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The system identifier of the unit


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "IG-200-839-2008-0"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/unitname"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/unitname:

      .. rst-class:: ansible-option-title

      **unitname**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/unitname" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      The name of the unit


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Testname"


      .. raw:: html

        </div>


  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-unit/version"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_information_module__return-unit/version:

      .. rst-class:: ansible-option-title

      **version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-unit/version" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Firmware version


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "6.2.0-beta2"


      .. raw:: html

        </div>




..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Ingate Systems AB (@ingatesystems)



.. Parsing errors

