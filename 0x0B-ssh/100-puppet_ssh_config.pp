#!/usr/bin/pup
# connect without paswd
file { '/home/ubuntu/.ssh/config':
  ensure  => file,
  content => "
    Host your_server
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
