import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from mapping.models import Full_table


def run():
    fhand = open('mapping/alias_list.csv',)
    reader = csv.reader(fhand)

    Full_table.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        s = Full_table(alias = row[0], feture_name = row[1])
        s.save()
