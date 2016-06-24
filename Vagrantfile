# -*- mode: ruby -*-
# vi: set ft=ruby :

memory_mb = "256"

Vagrant.configure(2) do |config|
  config.ssh.forward_agent = true

  config.vm.define "centos6" do |centos6|
    centos6.vm.provider "virtualbox" do |vb|
      vb.memory   = memory_mb
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end
    centos6.vm.box = "adsy-centos-6.5.box"
    centos6.vm.box_url = "https://adfinis-sygroup.ch/file-exchange-public/adsy-centos-6.5.box"
    centos6.vm.box_download_checksum = "a0f2cc25560495cd927da103659a59d69b2e4f1bf032ee67f35e8ea1b1c88a80"
    centos6.vm.box_download_checksum_type = "sha256"
  end

  config.vm.define "centos7" do |centos7|
    centos7.vm.provider "virtualbox" do |vb|
      vb.memory   = memory_mb
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end
    centos7.vm.box = "adsy-centos-7.2.box"
    centos7.vm.box_url = "https://adfinis-sygroup.ch/file-exchange-public/adsy-centos-7.2.box"
    centos7.vm.box_download_checksum = "b7464b893efeec591e04b3f74adbdd6c2df2c5f044c1c38abfb014b3659e28a6"
    centos7.vm.box_download_checksum_type = "sha256"
  end

  config.vm.define "jessie" do |jessie|
     jessie.vm.provider "virtualbox" do |vb|
      vb.memory   = memory_mb
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end
    jessie.vm.box = "adsy-debian-8.0.0.box"
    jessie.vm.box_url = "https://adfinis-sygroup.ch/file-exchange-public/adsy-debian-8.0.0.box"
    jessie.vm.box_download_checksum = "69ff0f7fe316a78fda94f3ed090a13a84ee25480f38f9d0b12adb1ae8f0ed9a9"
    jessie.vm.box_download_checksum_type = "sha256"
  end

  config.vm.define "wheezy" do |wheezy|
    wheezy.vm.provider "virtualbox" do |vb|
      vb.memory   = memory_mb
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end
    wheezy.vm.box = "adsy-debian-7.7.0.box"
    wheezy.vm.box_url = "https://adfinis-sygroup.ch/file-exchange-public/adsy-debian-7.7.0.box"
    wheezy.vm.box_download_checksum = "c39829c2f21b1081000347eda24234362007690ccb514b77b888e2d213e7b150"
    wheezy.vm.box_download_checksum_type = "sha256"
  end

  config.vm.define "trusty" do |trusty|
    trusty.vm.provider "virtualbox" do |vb|
      vb.memory   = memory_mb
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end
    trusty.vm.box = "adsy-ubuntu-14.04.box"
    trusty.vm.box_url = "https://adfinis-sygroup.ch/file-exchange-public/adsy-ubuntu-14.04.box"
    trusty.vm.box_download_checksum = "a2dbf07b02f95e1c5b2579ccb2bdb2e0138787ead11bcd0c1e29931822039510"
    trusty.vm.box_download_checksum_type = "sha256"
  end

  config.vm.define "vivid" do |vivid|
    vivid.vm.provider "virtualbox" do |vb|
      vb.memory   = memory_mb
      vb.customize ["modifyvm", :id, "--cpus", 2]
      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    end
    vivid.vm.box = "adsy-ubuntu-15.04.box"
    vivid.vm.box_url = "https://adfinis-sygroup.ch/file-exchange-public/adsy-ubuntu-15.04.box"
    vivid.vm.box_download_checksum = "c829507e0e2ded22c16943eeeb913abb835695b72922b2991931bc4aabf991ce"
    vivid.vm.box_download_checksum_type = "sha256"
  end

#  config.vm.define "xenial" do |xenial|
#    xenial.vm.provider "virtualbox" do |vb|
#      vb.memory   = memory_mb
#      vb.customize ["modifyvm", :id, "--cpus", 2]
#      vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
#    end
#    xenial.vm.box = "adsy-ubuntu-16.04.box"
#    xenial.vm.box_url = "https://adfinis-sygroup.ch/file-exchange-public/adsy-ubuntu-16.04.box"
#    xenial.vm.box_download_checksum = "40c31a3df527e0e2264dc3bce7fa0d330fbd49a4b0710512537d6c66353ef712"
#    xenial.vm.box_download_checksum_type = "sha256"
#  end
end
