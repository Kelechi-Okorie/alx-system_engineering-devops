# make nginx to stop dropping requests
exec {'fix':
  command => "sed -i "s/15/4096/" /etc/default/nginx,
  path    => ['/bin', '/usr/sbin'],
}

# restart nginx
exec {'restart':
  command => '/etc/init.d/nginx restart',
  path    => '/etc/init.d',
}
