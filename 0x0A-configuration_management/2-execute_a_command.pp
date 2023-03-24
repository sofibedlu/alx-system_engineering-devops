#this manifest kills the process named 'killmenow'
exec {'kill-killmenow':
command => '/usr/bin/pkill -f killmenow'
}
