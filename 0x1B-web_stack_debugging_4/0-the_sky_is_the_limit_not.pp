# fix number of request
exec { 'More_Request':
        command => 'sed -i s/15/5000/ /etc/default/nginx',
        path => '/usr/local/bin/:/bin/',
        provider => shell,
 }
 
exec { 'restart-nginx-service':
  command => 'nginx restart',
  path    => '/etc/init.d/',
  provider => shell,
}
