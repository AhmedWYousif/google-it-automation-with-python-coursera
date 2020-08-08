git --version

mkdir my-git-repo
cd my-git-repo
git init

git config --global user.name "Name"
git config --global user.email "user@example.com"

nano README
git status
git add README
git commit -m "This is my first commit!"

nano README
git status
git diff README
git add README
git status
git commit -m "This is my second commit."
git log