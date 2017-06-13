#!/usr/bin/env bash
set -e

sudo su - postgres -c "psql -c \"drop database if exists atlas;\""

sudo su - postgres -c "psql -c \"create database atlas\"";

sudo su - postgres -c "psql -c \"grant all privileges on database atlas to atlas\"";

cd ..
python manage.py migrate

cd scripts
python load_councilman.py /home/flavio/code/atlas/atlas/data/councilman.csv
python update_councilman_with_sequential_id.py /home/flavio/code/atlas/atlas/data/sequential_id.csv
python load_donations.py /home/flavio/code/atlas/atlas/data/2017-04-02-donations.csv
python load_assets.py /home/flavio/code/atlas/atlas/data/2017-04-02-property.csv
python load_votes.py /home/flavio/code/atlas/atlas/data/2017-04-02-votes.csv
python load_election_expense.py /home/flavio/code/atlas/atlas/data/2017-04-21-election_expenses.csv
python load_expense.py /home/flavio/code/atlas/atlas/data/2017-06-13-expenses.csv
read -p "Press enter to continue"
