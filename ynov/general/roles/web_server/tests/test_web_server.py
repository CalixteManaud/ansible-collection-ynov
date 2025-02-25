import pytest

def test_apache_installed(host):
    assert host.package("apache2").is_installed

def test_apache_running(host):
    assert host.service("apache2").is_running
    assert host.service("apache2").is_enabled

def test_apache_listening(host):
    assert host.socket("tcp://0.0.0.0:80").is_listening

def test_php_installed(host):
    assert host.package("php").is_installed

def test_apache_modules(host):
    modules = ["rewrite", "ssl"]
    for module in modules:
        assert host.run(f"a2query -m {module}").rc == 0
