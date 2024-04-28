# This is a Puppet manifest for managing SSH client configuration
# Ensure the .ssh directory exists
file { '/home/ubuntu/.ssh/':
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
  mode   => '0700',
}

# Then ensure the config file exists
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  require => File['/home/ubuntu/.ssh/'],
  owner   => 'ubuntu',
  group   => 'ubuntu',
  mode    => '0600',
  content => "Host *\n  IdentityFile ~/.ssh/school\n  PasswordAuthentication no\n",
}
