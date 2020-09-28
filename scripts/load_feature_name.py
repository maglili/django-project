import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from mapping.models import ID_table


def run():
    fhand = open('mapping/feature_name.csv',)
    reader = csv.reader(fhand)

    ID_table.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        s = ID_table(feture_name = row[0],) 
        s.save()
