# Fix and automate Apache using Puppet
exec {'fix and automate':
  command => "sed -i 's/locale.phpp/locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin',
}
