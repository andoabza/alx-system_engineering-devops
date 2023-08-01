#!/usr/bin/env ruby
# a script that print 10 digit phone number
puts ARGV[0].scan(/\d{10}/).join
