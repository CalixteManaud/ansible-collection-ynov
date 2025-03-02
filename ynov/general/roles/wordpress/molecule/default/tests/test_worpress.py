def test_wordpress_files(host):
    assert host.file("/var/www/wordpress").is_directory
    assert host.file("/var/www/wordpress/wp-config.php").exists

def test_wordpress_permissions(host):
    wp_dir = host.file("/var/www/wordpress")
    assert wp_dir.user == "www-data"
    assert wp_dir.group == "www-data"

def test_wordpress_config(host):
    wp_config = host.file("/var/www/wordpress/wp-config.php")
    assert wp_config.contains("DB_NAME")
    assert wp_config.contains("DB_USER")
    assert wp_config.contains("DB_PASSWORD")

def test_wordpress_accessible(host):
    cmd = host.run("curl -s -o /dev/null -w '%{http_code}' http://localhost")
    assert cmd.stdout.strip() == "200"
