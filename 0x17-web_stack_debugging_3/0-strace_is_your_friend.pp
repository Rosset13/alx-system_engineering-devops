exec { 'create-uploads-directory':
  command => '/bin/mkdir -p /var/www/html/wp-content/uploads && /bin/chown -R www-data:www-data /var/www/html/wp-content/uploads',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'test ! -d /var/www/html/wp-content/uploads',
}

