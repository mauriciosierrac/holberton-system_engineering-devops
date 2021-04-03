# this puppet file

file { 'ssh_config':
ensure  =>  'present',
} ->

file_line { 'Turn off passwd auth':
  path    =>  '/etc/ssh/ssh_config',
  replace =>  true,
  match   =>  '#   PasswordAuthentication no',
  line    =>  'PasswordAuthentication no',
}

file_line {  'Declare identity file':
  path    =>  '/etc/ssh/ssh_config',
  replace =>  true,
  match   =>  '#   IdentityFile ~/.ssh/holberton',
  line    =>  'IdentityFile ~/.ssh/holberton',
}
