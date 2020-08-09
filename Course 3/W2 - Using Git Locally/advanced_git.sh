
git commit -a	# Stages files automatically but only updated files
git commit -am
git log -p	# Produces patch text
git log --stat
git log --graph --oneline # show git log in graph one line every commit
git show COMMIT_ID	# Shows various objects
git diff	# Is similar to the Linux `diff` command, and can show the differences in various commits
git diff --staged	# An alias to --cached, this will show all staged files compared to the named commit
git add -p	# Allows a user to interactively review patches to add to the current commit
git mv	# Similar to the Linux `mv` command, this moves a file
git rm	# Similar to the Linux `rm` command, this deletes, or removes a file


# Git Revert Cheat Sheet
git checkout # is effectively used to switch branches.
git reset # basically resets the repo, throwing away some changes.
git commit --amend # is used to make changes to commits after-the-fact, which can be useful for making notes about a given commit.
git revert # makes a new commit which effectively rolls back a previous commit. It’s a bit like an undo command.



# Git Branches and Merging Cheat Sheet
git branch # list all branches
git branch new-feature # create new branch named new-feature
git checkout new-feature # switch to new-feature branch 
git checkout -b new-feature # create new branch named new-feature and switch to it
git branch -d new-feature # delete branch new-feature
git branch -D new-feature # delete branch new-feature even it has changes
git merge new-feature # merge new-feature into checked out branch 
git merge --abort # skip merging and reset your head to previous status 



