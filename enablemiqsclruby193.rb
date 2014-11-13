#!/usr/bin/env ruby

class EnableMiqSclRuby193
  def initialize(env, options = {})
    self.root = "/var/lib/enablemiqscl"
    @responses = []
    self.env = env

    options.each { |n, v| public_send("#{n}=", v) }
  end

  def logger
    puts "Invoked EnableMiqScl #run"
  end

  def run
    puts "Invoked EnableMiqScl #run"
  end
end

if __FILE__ == $PROGRAM_NAME
  if ARGV[0] == "--log"
    require 'syslog'
    logger = Syslog
  end

  s = EnableMiqScl.new(ENV, :logger => logger)
  Syslog.open(s.class.name.downcase) if logger
  s.run
  Syslog.close if logger
  print s.response.chomp
  exit s.exit_status
end
