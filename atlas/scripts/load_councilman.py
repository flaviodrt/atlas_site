import sys, os
import pandas as pd

sys.path.append("../")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "atlas.settings")

import django
django.setup()

from councilman.models import Councilman


def save_from_row(row):
    c = Councilman(**row)
    c.save()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        f = str(sys.argv[1])

        print("Reading file " + f)

        df = pd.read_csv(f)
        df['from_file'] = f.split("/")[-1]
        df.apply(save_from_row, axis=1)

    else:
        print("Please, provide the file path")
