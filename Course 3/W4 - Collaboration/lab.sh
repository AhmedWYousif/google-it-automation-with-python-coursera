git clone https://github.com/AhmedWYousif/it-cert-automation-practice.git

cd ~/it-cert-automation-practice
git remote -v

git remote add upstream https://github.com/AhmedWYousif/it-cert-automation-practice.git

git remote -v

git config --global user.name "Ahmed W. Yousif"
git config --global user.email "eng.ahmed.w.yousif@hotmail.com"

git branch improve-username-behavior

git checkout improve-username-behavior

cd ~/it-cert-automation-practice/Course3/Lab4
ls

cat validations.py

nano validations.py

print(validate_user("blue.kale", 3)) # True
print(validate_user(".blue.kale", 3)) # Currently True, should be False
print(validate_user("red_quinoa", 4)) # True
print(validate_user("_red_quinoa", 4)) # Currently True, should be False

python3 validations.py

nano validations.py


git status
git add validations.py
git status
git commit

Closes: #1
Updated validations.py python script.
Fixed the behavior of validate_user function in validations.py.

git push origin improve-username-behavior