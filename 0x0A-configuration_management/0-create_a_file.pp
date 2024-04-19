# This Puppet manifest ensures the existence of a file at '/tmp/school'.
file { '/tmp/school':
  # 'ensure => file' makes sure the resource is a file.
  ensure  => 'file',
  # 'mode => 0744' sets the file permissions to 0744.
  mode    => '0744',
  # 'owner => www-data' sets the file's owner to the 'www-data' user.
  owner   => 'www-data',
  # 'group => www-data' sets the file's group to 'www-data'.
  group   => 'www-data',
  # 'content => I love Puppet' sets the file's content to 'I love Puppet'.
  content => 'I love Puppet',
}
