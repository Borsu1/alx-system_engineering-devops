# Reconfigure the OS for 'holberton' to login and open a file without any error messages

exec { 'increase-hard-file-limit-holberton-user':
  command => '/bin/echo "holberton hard nofile 4096" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "holberton hard nofile 4096" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}

exec { 'increase-soft-file-limit-holberton-user':
  command => '/bin/echo "holberton soft nofile 2048" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "holberton soft nofile 2048" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
}

exec { 'apply-limits':
  command     => '/sbin/sysctl -p',
  refreshonly => true,
  subscribe   => [Exec['increase-hard-file-limit-holberton-user'], Exec['increase-soft-file-limit-holberton-user']],
  path        => ['/sbin', '/bin', '/usr/bin'],
}
