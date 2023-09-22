#!/usr/bin/pup
# kill a process
exec { 'pkill -f killmenow':
    command => '/usr/bin/pkill -f killmenow'
}
