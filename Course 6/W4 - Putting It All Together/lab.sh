# Fetching supplier data

ls ~/
sudo chmod +x ~/download_drive_file.sh
./download_drive_file.sh 1LePo57dJcgzoK4uiI_48S01Etck7w_5f supplier-data.tar.gz
# extract supplier-date file
tar xf ~/supplier-data.tar.gz
ls ~/supplier-data
cat ~/supplier-data/descriptions/007.txt


# Working with supplier images
nano ~/changeImage.py

sudo chmod +x ~/changeImage.py
./changeImage.py
file ~/supplier-data/images/003.jpeg



# Uploading images to web server
cat ~/example_upload.py
sudo chmod +x ~/example_upload.py
./example_upload.py
[linux-instance-IP-Address]/media/images/

nano ~/supplier_image_upload.py
sudo chmod +x ~/supplier_image_upload.py
./supplier_image_upload.py

# Uploading the descriptions
linux-instance-IP-Address/fruits

nano ~/run.py

sudo chmod +x ~/run.py

./run.py

# Generate a PDF report and send it through email

nano ~/reports.py

nano ~/report_email.py

# Send report through email

nano ~/emails.py

nano ~/report_email.py

sudo chmod +x ~/report_email.py

./report_email.py

[linux-instance-external-IP]/webmail


# Health check

nano ~/health_check.py

sudo chmod +x ~/health_check.py

./health_check.py


sudo apt install stress

stress --cpu 8

crontab -e

1

*/1 * * * * ~/health_check.py



