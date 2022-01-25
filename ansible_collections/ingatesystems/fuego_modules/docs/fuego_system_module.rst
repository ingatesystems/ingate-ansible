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
      <div class="ansibleOptionAnchor" id="parameter-filename"></div>
      <p class="ansible-option-title"><strong>filename</strong></p>
      <a class="ansibleOptionLink" href="#parameter-filename" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Path to a valid Ingate patch or upgrade file.</p>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-latest"></div>
      <p class="ansible-option-title"><strong>latest</strong></p>
      <a class="ansibleOptionLink" href="#parameter-latest" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Upgrade to the latest available version.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-latest_major"></div>
      <p class="ansible-option-title"><strong>latest_major</strong></p>
      <a class="ansibleOptionLink" href="#parameter-latest_major" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Upgrade to the latest major level.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-latest_minor"></div>
      <p class="ansible-option-title"><strong>latest_minor</strong></p>
      <a class="ansibleOptionLink" href="#parameter-latest_minor" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Upgrade to the latest minor level.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-latest_patch"></div>
      <p class="ansible-option-title"><strong>latest_patch</strong></p>
      <a class="ansibleOptionLink" href="#parameter-latest_patch" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Upgrade to the latest patch level.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-liccode"></div>
      <p class="ansible-option-title"><strong>liccode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-liccode" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The license code (e.g. KRJM-Q625-FUVG). Must be set for <code class='docutils literal notranslate'>license</code>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-license"></div>
      <p class="ansible-option-title"><strong>license</strong></p>
      <a class="ansibleOptionLink" href="#parameter-license" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Download and install a license.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-mode"></div>
      <p class="ansible-option-title"><strong>mode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-mode" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The operational mode.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">siparator</span></p></li>
        <li><p><span class="ansible-option-choices-entry">firewall</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-opmode"></div>
      <p class="ansible-option-title"><strong>opmode</strong></p>
      <a class="ansibleOptionLink" href="#parameter-opmode" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Set mode to siparator or firewall.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-password"></div>
      <p class="ansible-option-title"><strong>password</strong></p>
      <a class="ansibleOptionLink" href="#parameter-password" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Password for account login on ingate.com. Must be set for <code class='docutils literal notranslate'>license</code> and <code class='docutils literal notranslate'>upgrade_download</code>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-patch"></div>
      <p class="ansible-option-title"><strong>patch</strong></p>
      <a class="ansibleOptionLink" href="#parameter-patch" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Install a patch.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-reboot"></div>
      <p class="ansible-option-title"><strong>reboot</strong></p>
      <a class="ansibleOptionLink" href="#parameter-reboot" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Reboot the unit.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-upgrade"></div>
      <p class="ansible-option-title"><strong>upgrade</strong></p>
      <a class="ansibleOptionLink" href="#parameter-upgrade" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Install a firmware upgrade.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-upgrade_abort"></div>
      <p class="ansible-option-title"><strong>upgrade_abort</strong></p>
      <a class="ansibleOptionLink" href="#parameter-upgrade_abort" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Abort an upgrade after an upgrade has been installed.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-upgrade_accept"></div>
      <p class="ansible-option-title"><strong>upgrade_accept</strong></p>
      <a class="ansibleOptionLink" href="#parameter-upgrade_accept" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Accept an upgrade after an upgrade has been installed.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-upgrade_downgrade"></div>
      <p class="ansible-option-title"><strong>upgrade_downgrade</strong></p>
      <a class="ansibleOptionLink" href="#parameter-upgrade_downgrade" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Downgrade from a previously installed upgrade.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-upgrade_download"></div>
      <p class="ansible-option-title"><strong>upgrade_download</strong></p>
      <a class="ansibleOptionLink" href="#parameter-upgrade_download" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">boolean</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Download and install a firmware upgrade. The upgrade(s) will be downloaded from the Ingate Websystem. You can upgrade to the latest patch, minor or major version. You can also specify a desired version that is available in the respective level.</p>
      <p class="ansible-option-line"><span class="ansible-option-choices">Choices:</span></p>
      <ul class="simple">
        <li><p><span class="ansible-option-choices-entry">no</span></p></li>
        <li><p><span class="ansible-option-choices-entry">yes</span></p></li>
      </ul>
    </div></td>
  </tr>
  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-username"></div>
      <p class="ansible-option-title"><strong>username</strong></p>
      <a class="ansibleOptionLink" href="#parameter-username" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Username for account login on ingate.com. Must be set for <code class='docutils literal notranslate'>license</code> and <code class='docutils literal notranslate'>upgrade_download</code>.</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="parameter-version"></div>
      <p class="ansible-option-title"><strong>version</strong></p>
      <a class="ansibleOptionLink" href="#parameter-version" title="Permalink to this option"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>The the desired version to upgrade to.</p>
    </div></td>
  </tr>
  </tbody>
  </table>



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
      <div class="ansibleOptionAnchor" id="return-license"></div>
      <p class="ansible-option-title"><strong>license</strong></p>
      <a class="ansibleOptionLink" href="#return-license" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">list</span>
        / <span class="ansible-option-elements">elements=dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A list of information about the installed license.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>license</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-license/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-license/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Information regarding the installed license.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Install a Base license."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-opmode"></div>
      <p class="ansible-option-title"><strong>opmode</strong></p>
      <a class="ansibleOptionLink" href="#return-opmode" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>opmode</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-opmode/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-opmode/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Operational mode set to siparator."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-patch"></div>
      <p class="ansible-option-title"><strong>patch</strong></p>
      <a class="ansibleOptionLink" href="#return-patch" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>Information about the installed patch.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>patch</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-patch/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-patch/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>Patch information.</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Installed the patch patch-6.2.0-apipatch-1.fup (Test REST API 1)."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-reboot"></div>
      <p class="ansible-option-title"><strong>reboot</strong></p>
      <a class="ansibleOptionLink" href="#return-reboot" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>reboot</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-reboot/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-reboot/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Rebooting the unit now..."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade"></div>
      <p class="ansible-option-title"><strong>upgrade</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>upgrade</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Rebooting with new version. Please contact the unit again once it has rebooted."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade_abort"></div>
      <p class="ansible-option-title"><strong>upgrade_abort</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade_abort" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>upgrade_abort</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade_abort/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade_abort/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "The upgrade has been removed. Rebooting.."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade_accept"></div>
      <p class="ansible-option-title"><strong>upgrade_accept</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade_accept" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>upgrade_accept</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade_accept/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade_accept/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Made the upgrade permanent."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade_downgrade"></div>
      <p class="ansible-option-title"><strong>upgrade_downgrade</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade_downgrade" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>upgrade_downgrade</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade_downgrade/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade_downgrade/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Downgrade in progress (6.2.0). Rebooting..."</p>
    </div></td>
  </tr>

  <tr class="row-even">
    <td><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade_download"></div>
      <p class="ansible-option-title"><strong>upgrade_download</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade_download" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">dictionary</span>
      </p>
    </div></td>
    <td><div class="ansible-option-cell">
      <p>A command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> when <code class='docutils literal notranslate'>upgrade_download</code> is yes and success</p>
    </div></td>
  </tr>
  <tr class="row-odd">
    <td><div class="ansible-option-indent"></div><div class="ansible-option-cell">
      <div class="ansibleOptionAnchor" id="return-upgrade_download/msg"></div>
      <p class="ansible-option-title"><strong>msg</strong></p>
      <a class="ansibleOptionLink" href="#return-upgrade_download/msg" title="Permalink to this return value"></a>
      <p class="ansible-option-type-line">
        <span class="ansible-option-type">string</span>
      </p>
    </div></td>
    <td><div class="ansible-option-indent-desc"></div><div class="ansible-option-cell">
      <p>The command status message</p>
      <p class="ansible-option-line"><span class="ansible-option-returned-bold">Returned:</span> success</p>
      <p class="ansible-option-line ansible-option-sample"><span class="ansible-option-sample-bold">Sample:</span> "Your unit is upgraded to the latest version (6.2.2)"</p>
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

