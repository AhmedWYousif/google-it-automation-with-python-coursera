sudo apt install python3-pip

pip3 install psutil

python3

import psutil
psutil.cpu_percent()

psutil.disk_io_counters()
psutil.net_io_counters()

exit()

# rsync [Options] [Source-Files-Dir] [Destination]

# Some of the commonly used options in rsync command are listed below:

# Options Uses
# -v      Verbose output
# -q      Suppress message output
# -a      Archive files and directory while synchronizing
# -r      Sync files and directories recursively
# -b      Take the backup during synchronization
# -z      Compress file data during the transfer


# Example:

# Copy or sync files locally:
# rsync -zvh [Source-Files-Dir] [Destination]

# Copy or sync directory locally:
# rsync -zavh [Source-Files-Dir] [Destination]

# Copy files and directories recursively locally:
# rsync -zrvh [Source-Files-Dir] [Destination]


ls ~/scripts
sudo chmod +x ~/scripts/multisync.py
./scripts/multisync.py
nano ~/scripts/dailysync.py
