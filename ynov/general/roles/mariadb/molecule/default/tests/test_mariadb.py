def test_mariadb_installed(host):
    assert host.package("mariadb-server").is_installed

def test_mariadb_running(host):
    assert host.service("mariadb").is_running
    assert host.service("mariadb").is_enabled

def test_mariadb_listening(host):
    assert host.socket("tcp://127.0.0.1:3306").is_listening

def test_wordpress_database(host):
    cmd = host.run("mysql -e 'SHOW DATABASES;'")
    assert "wordpress_db" in cmd.stdout

def test_wordpress_user(host):
    cmd = host.run("mysql -e \"SELECT User FROM mysql.user WHERE User='wordpress_user';\"")
    assert "wordpress_user" in cmd.stdout
