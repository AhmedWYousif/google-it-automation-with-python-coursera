


echo $PATH

ls /

export PATH=/bin:/usr/bin

ls /

cd /etc/puppet/code/environments/production/modules/profile/manifests

cat init.pp


sudo nano init.pp

# content => "PATH=\$PATH:/java/bin\n"
# mode => 0644

sudo puppet agent -v --test

echo $PATH