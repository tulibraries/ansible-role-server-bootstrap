import os

import testinfra.utils.ansible_runner
import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_ssh_port(host):
    socket = host.socket("tcp://0.0.0.0:9229")
    assert socket.is_listening


@pytest.mark.parametrize('file, content', [
    ("/etc/ssh/sshd_config", "PermitRootLogin prohibit-password"),
    ("/etc/ssh/sshd_config", "Port 9229"),
    ("/home/root/.ssh/root", "RSA PRIVATE KEY")
    ])
def test_ssh_config(host, file, content):
    f = host.file(file)
    assert f.exists
    assert f.contains(content)


@pytest.mark.parametrize('file, content', [
    ("/home/conan_the_deployer/.ssh/conan_the_deployer", "RSA PRIVATE KEY")
    ])
def test_ssh_config_conan(host, file, content):
    f = host.file(file)
    assert not f.exists


@pytest.mark.parametrize('svc', ['firewalld', 'ntpd'])
def test_services_running(host, svc):
    service = host.service(svc)
    assert service.is_running
    assert service.is_enabled
