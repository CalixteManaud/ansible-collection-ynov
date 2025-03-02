def test_essential_packages(host):
    packages = ["curl", "vim", "htop", "ufw"]
    for package in packages:
        assert host.package(package).is_installed

def test_ufw_enabled(host):
    assert host.service("ufw").is_enabled
    assert host.service("ufw").is_running

def test_ssh_config(host):
    ssh_config = host.file("/etc/ssh/sshd_config")
    assert ssh_config.contains("PermitRootLogin no")
    assert ssh_config.contains("PasswordAuthentication no")

def test_webadmin_user(host):
    assert host.user("webadmin").exists
    assert "sudo" in host.user("webadmin").groups
