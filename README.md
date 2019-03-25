TU Libraries Server Bootstrap Ansible Role
=========

This is the role run for applying TU Libraries specific baselines on any new Linode servers. These baselines include things like adding core users, firewall defaults, updating required Centos 7 packages, etc.

Requirements
------------

Use `Pipenv` and `.python-version` files to know the required libraries to run this role.

Role Variables
--------------

The primary variables needed are the authorized public keys of all the users to be added to the new server for authentication purposes.

`ssh_port` The port on which sshd should listen. Defaults to 9229. Override to 2222 for vagrant inventories to allow `vagrant ssh` to continue to work.

Dependencies
------------

- `jeffwidman.yum-cron` is required for adding cron updates for security packages managed by yum on the new servers.
- `geerlingguy.repo-epel` is required for running EPEL (extra packages for enterprise linux) updates on the new servers.


Example Playbook
----------------

See our usage of this Role here: https://github.com/tulibraries/ansible-server-bootstrap. Here is an example of this role's usage taken from there:

```

```

Developing this role
------------------
When you make changes, you should run the tests locally. To do so:

* Run `pipenv install` to install dependencies.
* Run `pipenv run molecule test` to run all tests, including linting, test build, in a local docker environment.

If you want to try just running the role without running all tests, you can run `pipenv run molecule converge`

Unit tests are defined in [molecule/default/tests/test_default.py](molecule/default/tests/test_default.py).

License
-------

BSD
