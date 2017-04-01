set -e

python load_councilman.py /home/flavio/code/atlas/atlas/data/councilman.csv
python update_councilman_with_sequential_id.py /home/flavio/code/atlas/atlas/data/sequential_id.csv
python load_donations.py /home/flavio/code/atlas/atlas/data/donations.csv
