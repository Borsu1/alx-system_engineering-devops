# This Puppet manifest ensures the Flask Python package is installed via pip3.
package { 'flask':
  ensure   => '2.1.0',  # Ensures Flask version 2.1.0 is installed.
  provider => 'pip3',  # Specifies pip3 as the package provider.
}
