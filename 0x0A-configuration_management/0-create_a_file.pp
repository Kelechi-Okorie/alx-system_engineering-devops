# create a puppet file
file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www',
  content => 'I love Puppet',
}