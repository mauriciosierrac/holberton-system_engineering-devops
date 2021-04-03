# create holberton file in /tmp
# assigns 0744 permissions and asigns www-data that user and group

file { 'holberton':
  ensure  => 'present',
  path    => '/tmp/holberton',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  content => 'I love Puppet',
}
