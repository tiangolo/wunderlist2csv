wunderlist2csv
==============

Convert from [Wunderlist](https://www.wunderlist.com/) backup json file to a CSV file importable by [TaskCoach](http://taskcoach.org/).

Wunderlist Steps
----------------

1. Go to your account in Wunderlist online: https://www.wunderlist.com/webapp/
2. Click your photo-menu on the upper left corner.
3. Click the option *"Account Settings"*.
4. In the section *"Account Backup"* click the button *"Create Backup"*.
5. That button changes it's name to *"Click to Download"*, click it, it will download a json file with your backup.

wunderlist2csv Steps
--------------------

1. You need to have Python 2.7 installed: https://www.python.org/downloads/
2. Open a Terminal or a Command prompt (In Windows press Windows_key+R, type "cmd", press "Enter").
3. Go to the directory where you downloaded wunderlist2csv.py (e.g. `cd C:\Users\User\Downloads`).
4. Run the script with python, give it the source json file you downloaded from Wunderlist and a name of a file to write the output (e.g. `python wunderlist2csv.py wunderlist-20141217-19-30-22.json output.csv`).
5. Import the generated file (e.g. `output.csv`) with TaskCoach: `File -> Import -> Import CSV...` and follow TaskCoach instructions.
