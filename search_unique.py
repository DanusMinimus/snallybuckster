artifact_dict = {
    'standard_php': ['index.php', 'wp-config.php', 'configuration.php', 'config.php', 'config.inc.php', 'settings.php'],
    'lazy_file_manager': '/lfm.php',
    'idea_webserver': '/WebServers.xml',
    'symfony_database': '/config/databases.yml',
    'git_config': '/.git',
    'svn_repo': '/.svn/entries',
    'apache_server_status': '/server-status',
    'apache_server_info': '/server-info',
    'core_dump': '/core',
    'sftp_config': '/sftp-config.json',
    'wstp_config': ['WS_FTP.ini', 'ws_ftp.ini', 'WS_FTP.INI'],
    'filezilla_config': ['filezilla.xml', 'sitemanager.xml', 'FileZilla.xml'],
    'winscp_config': 'winscp.ini',
    'appe_desktop_service': '/.DS_Store',
    'php_cache': ['/.php_cs.cache', '/.php-cs-fixer.cache'],
    'file_backup': ['_FILE_.bak', '_FILE_~', '._FILE_.swp', '%23_FILE_%23', '_FILE_.save', '_FILE_.orig'],
    'apache_dir': ['/backup/', '/www/', '/wwwdata/', '/db/', '/htdocs/'],
    'zip_archive': ['.zip', '.tar', '.rar', '.7zip', '.7z', '.xz'],
    'deadjoe_config': '/DEADJOE',
    'sql_data': '.sql',
    'crypto_wallet': '/wallet.dat',
    'drupal_backup': '/sites/default/private/files/backup_migrate/scheduled/test.txt',
    'magento_config': '/app/etc/local.xml',
    'private_keys': ['server.key', 'privatekey.key', 'myserver.key', 'key.pem'],
    'ssh_keys': ['id_rsa', 'id_dsa', '.ssh/id_rsa', '.ssh/id_dsa'],
    'enviroment_variables': '/.env',
    'ilias_php': ['/ilias.php', '/login.php'],
    'cgi_echo': ['/cgi-bin/cgiecho', '/cgi-sys/cgiecho'],
    'php_unit': '/vendor/phpunit/phpunit/src/Util/PHP/eval-stdin.php',
    'acme_challenge': '/.well-known/acme-challenge/reflect',
    'drupal_db': ['/sites/default/files/.ht.sqlite','/core/CHANGELOG.txt'],
    'adminer': ['/adminer.php', 'adminer.org'],
    'elmah': '/elmah.axd',
    'vpn_tips': '/vpns/portal/tips.html',
    'setup_config': ['wp-admin/setup-config.php', 'installation/index.php', 'typo3/install.php', 'serendipity_admin.php', 'wp-admin/css/install.css'],
    'telescope_dir': '/telescope',
    'vbulletin_config': '/vb_test.php',
    'wordpress_debug': '/wp-content/debug.log',
    'thumbs_db': '/thumbs.db',
    'duplicator_installer': ['installer-backup.php', '/dup-installer/main.installer.php'],
    'desktop_ini': '/desktop.ini',
    'mail_config': '/mailman/listinfo',
    'composer': ['composer.json', 'composer.lock'],
    'php_info': ['phpinfo.php', 'info.php', 'i.php', 'test.php'],
    'possible_credentials': 'credentials.ini',
    'config_data': 'config.ini',
    'rdp_config': '.rdp',
    'cretifications': ['.pfx','.cer','.spc', '.key', '.crt', '.pem'],
    'csv_file': '.csv'
    }

def search_files(url: str):
    for k, v in artifact_dict.items():

        if type(v) is list:
            for v_item in v:
                if v_item in url:
                    print(k+":"+url)
        else:
            if v in url:
                print(k+":"+url)
