import sys, os
import pandas as pd

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atlas.settings")

import django
django.setup()

from councilman.models import Councilman, Donation


def save_from_row(row):
    d = Donation(**row)
    d.save()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = str(sys.argv[1])

        print("Reading file " + f)

        councilman = pd.DataFrame().from_records(
            Councilman.objects.all().values('id', 'sequential_id')
        ).rename(columns={'id': 'councilman_id'})

        df = pd.read_csv(f)
        df['from_file'] = f.split("/")[-1]
        df = pd.merge(df, councilman, on='sequential_id')
        df.apply(save_from_row, axis=1)

    else:
        print("Please, provide the file path")
