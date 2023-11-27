# Using puppet to make changes to our configuration file

file { '/home/kelechi/alx-projects/alx-system_engineering-devops/0x0B-ssh/file':
  ensure  => present,  # Ensure the file exists
  content => "This is the new content of the file.\n",
  replace => true,
  matches => '^name=kelechi$',
}