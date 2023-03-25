file { '/home/vagrant/.ssh/config':
ensure  => 'present',
content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
}
