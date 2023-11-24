# kills a process named killmenow
exec {  'killmenow':
  command => 'user/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
}
