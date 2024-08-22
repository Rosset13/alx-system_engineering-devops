# 1-user_limit.pp
exec { 'change-os-configuration-for-holberton-user':
  command => 'echo "holberton soft nofile 65535" >> /etc/security/limits.conf && echo "holberton hard nofile 65535" >> /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin'],
  onlyif  => 'grep -qv "holberton" /etc/security/limits.conf',
}

