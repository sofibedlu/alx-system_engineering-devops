# change `phpp` extensions with `php` in /var/www/html/wp-settings.php'

exec { 'replace-phpp-with-php-in-wp-settings':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/bin/'
}
