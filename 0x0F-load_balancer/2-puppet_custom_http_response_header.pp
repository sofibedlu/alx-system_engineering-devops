#install and configure ngnix server on ubuntu machine

exec { 'apt-get update':
command => 'apt-get update',
path    => '/usr/bin',
}

package { 'nginx':
ensure          => installed,
provider        => 'apt-get',
install_options => '-y',
}

file { '/var/www/html/index.html':
content => 'Hello World!',
}

file { '/var/www/html/404.html':
content => 'Ceci n\'est pas une page\n',
}

$config = @(END)
 server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
        error_page 404 /404.html;
	index index.html index.htm index.nginx-debian.html;
	server_name _;
	if ($request_filename ~ redirect_me){
		rewrite ^ https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
	}
	location / {
		 try_files $uri $uri/ =404;
	}
 }
END

file { '/etc/nginx/sites-enabled/default':
ensure  => 'file',
content => $config,
}

new_string="http {\n\tadd_header X-Served-By \$hostname;"
exec { 'update header':
command => 'sed -i "s|http {|$new_string|" /etc/nginx/nginx.conf',
path    => '/usr/bin',
}

exec { 'restart nginx':
command => 'service nginx restart',
path    => '/usr/sbin',
}

service { 'nginx':
ensure  => running,
require => Package['nginx'],
}
