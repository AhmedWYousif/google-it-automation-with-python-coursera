

# Install packages
cd /etc/puppet/code/environments/production/modules/packages
cat manifests/init.pp
sudo chmod 646 manifests/init.pp

# update init.pp content

# This command outputs the external IP address of linux-instance. 
gcloud compute instances describe linux-instance --zone=us-central1-a --format='get(networkInterfaces[0].accessConfigs[0].natIP)'
sudo puppet agent -v --test
apt policy golang



#Fetch machine information
cd /etc/puppet/code/environments/production/modules/machine_info
cat manifests/init.pp
sudo chmod 646 manifests/init.pp

cat templates/info.erb
sudo chmod 646 templates/info.erb

sudo puppet agent -v --test
cat /tmp/machine_info.txt

#Reboot machine
sudo mkdir -p /etc/puppet/code/environments/production/modules/reboot/manifests
cd /etc/puppet/code/environments/production/modules/reboot/manifests
sudo touch init.pp
sudo nano init.pp

sudo nano /etc/puppet/code/environments/production/manifests/site.pp

#Run the client on linux-instance VM terminal
sudo puppet agent -v --test



