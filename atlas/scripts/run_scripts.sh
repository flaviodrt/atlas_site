set -e

#python load_councilman.py /home/flavio/code/atlas/atlas/data/councilman.csv
#python update_councilman_with_sequential_id.py /home/flavio/code/atlas/atlas/data/sequential_id.csv
#python load_councilman.py /home/flavio/code/atlas/atlas/data/secretary-councilman.csv
#python load_donations.py /home/flavio/code/atlas/atlas/data/donations.csv
#python load_expense.py /home/flavio/code/atlas/atlas/data/2017-04-02-expenses.csv
#python load_assets.py /home/flavio/code/atlas/atlas/data/2017-04-02-property.csv
#python load_votes.py /home/flavio/code/atlas/atlas/data/2017-04-02-votes.csv

python load_election_expense.py /home/flavio/code/atlas/atlas/data/2017-04-21-election_expenses.csv
