#!/usr/bin/env bash
set -e

echo "Enter the path with CSV files"
read path

sudo su - postgres -c "psql << EOF
\c atlas
truncate councilman_expense;
EOF"
python load_expense.py $path/expenses.csv
read -p "Press enter to continue"
