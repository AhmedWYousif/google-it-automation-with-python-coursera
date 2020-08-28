
git clone https://www.github.com/google/it-cert-automation-practice.git
cd ~/it-cert-automation-practice/Course5/Lab3
ls
sudo cp hello_cloud.py /usr/local/bin/
sudo cp hello_cloud.service /etc/systemd/system
sudo systemctl enable hello_cloud.service



gcloud compute instances create --zone us-west1-b --source-instance-template vm1-template vm2 vm3 vm4 vm5 vm6 vm7 vm8

gcloud compute instances list