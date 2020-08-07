# Redirections, Pipes and Signals
# Managing streams
# These are the redirectors that we can use to take control of the streams of our programs

command > file: # redirects standard output, overwrites file
command >> file: # redirects standard output, appends to file
command < file:  # redirects standard input from file
command 2> file: # redirects standard error to file
command1 | command2: # connects the output of command1 to the input of command2

# Operating with processes
# These are some commands that are useful to know in Linux when interacting with processes. Not all of them are explained in videos, so feel free to investigate them on your own.

ps: # lists the processes executing in the current terminal for the current user
ps ax: # lists all processes currently executing for all users
ps e: # shows the environment for the processes listed
kill PID: # sends the SIGTERM signal to the process identified by PID
fg: # causes a job that was stopped or in the background to return to the foreground
bg: # causes a job that was stopped to go to the background
jobs: # lists the jobs currently running or stopped
top: # shows the processes currently using the most CPU time (press "q" to quit)