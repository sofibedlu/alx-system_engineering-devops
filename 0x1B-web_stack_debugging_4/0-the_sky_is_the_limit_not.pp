# this manifest increase u limit for nginx
exec { 'set ulimit for nginx':
  command => '/bin/sed -i "s/ULIMIT.*/ULIMIT=\"-n 5000\"/" /etc/default/nginx'
} -> exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
