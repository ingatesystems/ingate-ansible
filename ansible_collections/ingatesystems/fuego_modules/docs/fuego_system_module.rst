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

.. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module:

.. Anchors: short name for ansible.builtin

.. Anchors: aliases



.. Title

ingatesystems.fuego_modules.fuego_system -- Manage licenses, patches and upgrades on an Ingate SBC.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. Collection note

.. note::
    This plugin is part of the `ingatesystems.fuego_modules collection <https://galaxy.ansible.com/ingatesystems/fuego_modules>`_ (version 1.0.0).

    You might already have this collection installed if you are using the ``ansible`` package.
    It is not included in ``ansible-core``.
    To check whether it is installed, run :code:`ansible-galaxy collection list`.

    To install it, use: :code:`ansible-galaxy collection install ingatesystems.fuego_modules`.

    To use it in a playbook, specify: :code:`ingatesystems.fuego_modules.fuego_system`.

.. version_added

.. versionadded:: 1.0.0 of ingatesystems.fuego_modules

.. contents::
   :local:
   :depth: 1

.. Deprecated


Synopsis
--------

.. Description

- Manage licenses, patches and upgrades on an Ingate SBC.


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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/address:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/password:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/port:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/scheme:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/timeout:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/username:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/validate_certs:
      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/verify_ssl:

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

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-client/version:

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
        <div class="ansibleOptionAnchor" id="parameter-filename"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-filename:

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

      Path to a valid Ingate patch or upgrade file.


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-latest"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-latest:

      .. rst-class:: ansible-option-title

      **latest**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-latest" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Upgrade to the latest available version.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-latest_major"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-latest_major:

      .. rst-class:: ansible-option-title

      **latest_major**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-latest_major" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Upgrade to the latest major level.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-latest_minor"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-latest_minor:

      .. rst-class:: ansible-option-title

      **latest_minor**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-latest_minor" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Upgrade to the latest minor level.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-latest_patch"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-latest_patch:

      .. rst-class:: ansible-option-title

      **latest_patch**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-latest_patch" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Upgrade to the latest patch level.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-liccode"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-liccode:

      .. rst-class:: ansible-option-title

      **liccode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-liccode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The license code (e.g. KRJM-Q625-FUVG). Must be set for \ :literal:`license`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-license"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-license:

      .. rst-class:: ansible-option-title

      **license**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-license" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Download and install a license.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-mode"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-mode:

      .. rst-class:: ansible-option-title

      **mode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-mode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The operational mode.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`siparator`
      - :ansible-option-choices-entry:`firewall`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-opmode"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-opmode:

      .. rst-class:: ansible-option-title

      **opmode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-opmode" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Set mode to siparator or firewall.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-password"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-password:

      .. rst-class:: ansible-option-title

      **password**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Password for account login on ingate.com. Must be set for \ :literal:`license`\  and \ :literal:`upgrade\_download`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-patch"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-patch:

      .. rst-class:: ansible-option-title

      **patch**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-patch" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Install a patch.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-reboot"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-reboot:

      .. rst-class:: ansible-option-title

      **reboot**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-reboot" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Reboot the unit.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-upgrade"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-upgrade:

      .. rst-class:: ansible-option-title

      **upgrade**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-upgrade" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Install a firmware upgrade.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-upgrade_abort"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-upgrade_abort:

      .. rst-class:: ansible-option-title

      **upgrade_abort**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-upgrade_abort" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Abort an upgrade after an upgrade has been installed.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-upgrade_accept"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-upgrade_accept:

      .. rst-class:: ansible-option-title

      **upgrade_accept**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-upgrade_accept" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Accept an upgrade after an upgrade has been installed.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-upgrade_downgrade"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-upgrade_downgrade:

      .. rst-class:: ansible-option-title

      **upgrade_downgrade**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-upgrade_downgrade" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Downgrade from a previously installed upgrade.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-upgrade_download"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-upgrade_download:

      .. rst-class:: ansible-option-title

      **upgrade_download**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-upgrade_download" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`boolean`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Download and install a firmware upgrade. The upgrade(s) will be downloaded from the Ingate Websystem. You can upgrade to the latest patch, minor or major version. You can also specify a desired version that is available in the respective level.


      .. rst-class:: ansible-option-line

      :ansible-option-choices:`Choices:`

      - :ansible-option-choices-entry:`no`
      - :ansible-option-choices-entry:`yes`

      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-username"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-username:

      .. rst-class:: ansible-option-title

      **username**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Username for account login on ingate.com. Must be set for \ :literal:`license`\  and \ :literal:`upgrade\_download`\ .


      .. raw:: html

        </div>

  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="parameter-version"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__parameter-version:

      .. rst-class:: ansible-option-title

      **version**

      .. raw:: html

        <a class="ansibleOptionLink" href="#parameter-version" title="Permalink to this option"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      The the desired version to upgrade to.


      .. raw:: html

        </div>


.. Attributes


.. Notes

Notes
-----

.. note::
   - The methods \ :literal:`patch`\  and \ :literal:`upgrade\_download`\  assumes that the the preliminary configuration has been stored to the permanent configuration at least once (see module M(fuego_config) \ :literal:`store`\  method).
   - For the methods \ :literal:`license`\  and \ :literal:`upgrade\_download`\  the Ansible host needs Internet connectivity.
   - When using the the \ :literal:`upgrade`\  method the unit will reboot and you need to do \ :literal:`upgrade accept`\  or \ :literal:`upgrade\_abort`\ .
   - When changing operational mode using \ :literal:`opmode`\ , a reboot is required in order for the change to take effect.
   - This module requires that the Ingate Python SDK is installed on the host. To install the SDK use the pip command from your shell \ :literal:`pip install ingatesdk`\ .

.. Seealso


.. Examples

Examples
--------

.. code-block:: yaml+jinja

    
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
        <div class="ansibleOptionAnchor" id="return-license"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-license:

      .. rst-class:: ansible-option-title

      **license**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-license" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`list` / :ansible-option-elements:`elements=dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A list of information about the installed license.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`license`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-license/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-license/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-license/msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Information regarding the installed license.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Install a Base license."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-opmode"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-opmode:

      .. rst-class:: ansible-option-title

      **opmode**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-opmode" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`opmode`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-opmode/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-opmode/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-opmode/msg" title="Permalink to this return value"></a>

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

      :ansible-option-sample-bold:`Sample:` "Operational mode set to siparator."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-patch"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-patch:

      .. rst-class:: ansible-option-title

      **patch**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-patch" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      Information about the installed patch.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`patch`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-patch/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-patch/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-patch/msg" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`string`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">

      Patch information.


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` success

      .. rst-class:: ansible-option-line
      .. rst-class:: ansible-option-sample

      :ansible-option-sample-bold:`Sample:` "Installed the patch patch-6.2.0-apipatch-1.fup (Test REST API 1)."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-reboot"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-reboot:

      .. rst-class:: ansible-option-title

      **reboot**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-reboot" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`reboot`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-reboot/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-reboot/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-reboot/msg" title="Permalink to this return value"></a>

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

      :ansible-option-sample-bold:`Sample:` "Rebooting the unit now..."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade:

      .. rst-class:: ansible-option-title

      **upgrade**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`upgrade`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade/msg" title="Permalink to this return value"></a>

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

      :ansible-option-sample-bold:`Sample:` "Rebooting with new version. Please contact the unit again once it has rebooted."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade_abort"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade_abort:

      .. rst-class:: ansible-option-title

      **upgrade_abort**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade_abort" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`upgrade\_abort`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade_abort/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade_abort/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade_abort/msg" title="Permalink to this return value"></a>

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

      :ansible-option-sample-bold:`Sample:` "The upgrade has been removed. Rebooting.."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade_accept"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade_accept:

      .. rst-class:: ansible-option-title

      **upgrade_accept**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade_accept" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`upgrade\_accept`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade_accept/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade_accept/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade_accept/msg" title="Permalink to this return value"></a>

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

      :ansible-option-sample-bold:`Sample:` "Made the upgrade permanent."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade_downgrade"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade_downgrade:

      .. rst-class:: ansible-option-title

      **upgrade_downgrade**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade_downgrade" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`upgrade\_downgrade`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade_downgrade/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade_downgrade/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade_downgrade/msg" title="Permalink to this return value"></a>

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

      :ansible-option-sample-bold:`Sample:` "Downgrade in progress (6.2.0). Rebooting..."


      .. raw:: html

        </div>



  * - .. raw:: html

        <div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade_download"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade_download:

      .. rst-class:: ansible-option-title

      **upgrade_download**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade_download" title="Permalink to this return value"></a>

      .. rst-class:: ansible-option-type-line

      :ansible-option-type:`dictionary`

      .. raw:: html

        </div>

    - .. raw:: html

        <div class="ansible-option-cell">

      A command status message


      .. rst-class:: ansible-option-line

      :ansible-option-returned-bold:`Returned:` when \ :literal:`upgrade\_download`\  is yes and success


      .. raw:: html

        </div>

    
  * - .. raw:: html

        <div class="ansible-option-indent"></div><div class="ansible-option-cell">
        <div class="ansibleOptionAnchor" id="return-upgrade_download/msg"></div>

      .. _ansible_collections.ingatesystems.fuego_modules.fuego_system_module__return-upgrade_download/msg:

      .. rst-class:: ansible-option-title

      **msg**

      .. raw:: html

        <a class="ansibleOptionLink" href="#return-upgrade_download/msg" title="Permalink to this return value"></a>

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

      :ansible-option-sample-bold:`Sample:` "Your unit is upgraded to the latest version (6.2.2)"


      .. raw:: html

        </div>




..  Status (Presently only deprecated)


.. Authors

Authors
~~~~~~~

- Ingate Systems AB (@ingatesystems)



.. Parsing errors

