class ssh_client {
  file { '/home/vagrant/.ssh/config':
    ensure  => 'present',
    content => "IdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
  }
}

include ssh_client
