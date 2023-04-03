#configure nginx for custome http header

exec { 'apt-get update':
command => 'apt-get update',
path    => '/usr/bin',
}

package { 'nginx':
ensure   => installed,
provider => 'apt-get',
}

exec { 'update header':
command => 'sed -i "s|http {|http {\n\tadd_header X-Served-By $hostname;|" /etc/nginx/nginx.conf',
path    => '/usr/bin',
}

exec { 'restart nginx':
command => 'service nginx restart',
path    => '/usr/sbin',
}
