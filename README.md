TU Libraries Server Bootstrap Ansible Role
=========

This is the role run for applying TU Libraries specific baselines on any new Linode servers. These baselines include things like adding core users, firewall defaults, updating required Centos 7 packages, etc.

Role Variables
--------------

The primary variables needed are the authorized public keys of all the users to be added to the new server for authentication purposes.

Dependencies
------------

- `jeffwidman.yum-cron` is required for adding cron updates for security packages managed by yum on the new servers.
- `geerlingguy.repo-epel` is required for running EPEL (extra packages for enterprise linux) updates on the new servers.

Example Playbook
----------------

See our usage of this Role here: https://github.com/tulibraries/ansible-server-bootstrap. Here is an example of this role's usage taken from there:

```

```

License
-------

BSD