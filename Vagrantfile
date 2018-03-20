# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.provision "shell", path: "dev_config.sh"
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 8000, host: 5000

  config.vm.synced_folder ".", "/home/vagrant/spinthewheel.gr"
end
