# this puppet file kill a process call killnenow

exec { 'killnenow':
  command  => 'pkill killmenow',
  provider => shell,
}
