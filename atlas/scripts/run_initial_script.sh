#!/usr/bin/env bash
set -e

echo "Enter the path with CSV files"
read path

sudo su - postgres -c "psql -c \"drop database if exists atlas;\""

sudo su - postgres -c "psql -c \"create database atlas\"";

sudo su - postgres -c "psql -c \"grant all privileges on database atlas to atlas\"";

cd ..
python manage.py migrate

cd scripts
python load_councilman.py $path/councilman.csv
python update_councilman_with_sequential_id.py $path/sequential_id.csv
python load_donations.py $path/2017-04-02-donations.csv
python load_assets.py $path/2017-04-02-property.csv
python load_votes.py $path/2017-04-02-votes.csv
python load_election_expense.py $path/2017-04-21-election_expenses.csv
read -p "Press enter to continue"
