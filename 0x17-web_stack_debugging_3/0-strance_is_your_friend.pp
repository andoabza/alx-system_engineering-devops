ure  => present,
  content => template('your_module/apache2.conf.erb'),
  notify  => Service['apache2'],
}
