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
