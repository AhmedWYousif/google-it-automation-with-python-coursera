git clone https://github.com/AhmedWYousif/github-lab.git
ls
cd github-lab
git config --global user.name "Ahmed W. Yousif"
git config --global user.email "eng.ahmed.w.yousif@hotmail.com"

nano README.md

git status

git commit -m "I am editing the README file."
git push origin master


nano example.py

def git_opeation():
 print("I am adding example.py file to the remote repository.")
git_opeation()


git add example.py
git commit -m "add example.py"


git push origin master

git pull origin master

git push origin master
