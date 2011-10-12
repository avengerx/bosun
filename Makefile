pep8:
	pep8 fabfile.py
	pep8 tasks.py

pylint:
	- pylint -d c fabfile.py
	- pylint -d c tasks.py

pyflakes:
	- pyflakes fabfile.py
	- pyflakes tasks.py

clonedigger:
	- clonedigger -o output.html fabfile.py
	- clonedigger -o output.html tasks.py

check: pep8 pylint pyflakes clonedigger

clean:
	- rm output.html
	gfind . -iname *.pyc -exec rm {} +

run:
	fab -H tupa -u ${USER} deploy:name='expbase',exp_repo=\$${ARCHIVE_OCEAN}\/exp_repos

run_named:
	fab -H tupa -u ${USER} deploy:name=${NAME},comp=${COMP},code_dir=\$${HOME}\/run-new-2,submit_dir=\$${SUBMIT_HOME}\/run-new-2

compile:
	fab -H tupa -u ${USER} compilation:comp=${COMP},code_dir=\$${HOME}\/run-new-2,submit_dir=\$${SUBMIT_HOME}\/run-new-2
