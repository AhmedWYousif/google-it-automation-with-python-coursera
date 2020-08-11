

git clone URL	# Git clone is used to clone a remote repository into a local workspace
git push	# Git push is used to push commits from your local repo to a remote repo
git pull	# Git pull is used to fetch the newest updates from a remote repository

# https://help.github.com/en/articles/caching-your-github-password-in-git
# https://help.github.com/en/articles/generating-an-ssh-key  

git config --global credential.helper cache # allows us to configure the credential helper



git remote 	# Lists remote repos
git remote -v	# List remote repos verbosely
git remote show <name>	# Describes a single remote repo
git remote update	# Fetches the most up-to-date objects
git fetch	# Downloads specific objects
git branch -r	# Lists remote branches; can be combined with other branch arguments to manage remote branches


git push -u origin new-feature # push changes into new-feature remote branch 
# rebase to master
git checkout new-feature # check out new feature branch
git rebase master # rebase current branch to master branch
git checkout mster # checkout master branch
git merge new-feature # merge feature branch with master
git push --delete origin new-feature # delete remote new-feature brnach 
git branch -d new-feature # delete local new-feature brnach 

# rebaase same branch
git fech
git rebase origin/master # rebase your local changes to remote master branch 
# resolve all conflicts
git add .
git rebase --continue # continue rebase
git log --graph --oneline # now history is linear
git push # push changes










