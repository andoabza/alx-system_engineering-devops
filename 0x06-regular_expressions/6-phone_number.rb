#!/usr/bin/env ruby
# a script that print 10 digit phone number
puts ARGV[0].scan(/^[0-9\d]{10}/).join

