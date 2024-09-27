# This Puppet manifest ensures the Apache service is running and enabled.

# Ensure the Apache service is running
service { 'apache2':
  ensure => running,
  enable => true,
}

# Example fix: Ensure the correct permissions for a directory
file { '/var/www/html':
  ensure  => directory,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0755',
  require => Service['apache2'],
}

# Example fix: Ensure a configuration file is present
file { '/etc/apache2/sites-available/000-default.conf':
  ensure  => file,
  source  => 'puppet:///modules/apache/000-default.conf',
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  require => Service['apache2'],
}

# Notify the Apache service to restart if the configuration changes
exec { 'reload_apache':
  command     => '/usr/sbin/apachectl graceful',
  refreshonly => true,
  subscribe   => File['/etc/apache2/sites-available/000-default.conf'],
}
