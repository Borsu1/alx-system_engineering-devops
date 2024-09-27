<<<<<<< HEAD
# 0-strace_is_your_friend.pp
class apache_fix {
  file { '/var/www/html':
    ensure  => directory,
    owner   => 'www-data',
    group   => 'www-data',
    mode    => '0755',
    recurse => true,
  }

  exec { 'check_apache_config':
    command => '/usr/sbin/apachectl configtest',
    path    => ['/bin', '/usr/bin', '/sbin', '/usr/sbin'],
    notify  => Service['apache2'],
  }

  service { 'apache2':
    ensure  => running,
    enable  => true,
    require => Exec['check_apache_config'],
  }
}

include apache_fix
=======
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
>>>>>>> f7cef9c7ba3443efc751693d60a82790daf5ee6c
