# Fixes a 500 error from a wordpress server
exec { 'fix-wordpress-error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
