#configure the ssh-client to use private_key ~/.ssh/school and refuse to authenticate using a password
file { '/home/vagrant/.ssh/config':
ensure  => 'present',
content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
}
