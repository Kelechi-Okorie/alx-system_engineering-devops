# kills a process
exec {  'killmenow':
  command => 'user/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
