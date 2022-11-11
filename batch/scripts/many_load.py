import csv

from unesco.models import Category, State, Iso,Region, Site


def run():
    fhead = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhead)

    next(reader)

    Category.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()


    for row in reader:
        print(row)

        c, create = Category.objects.get_or_create(name = row[7])
        s, create = State.objects.get_or_create(name = row[8])
        i, create = Iso.objects.get_or_create(name = row[10])
        r,create = Region.objects.get_or_create(name = row[9])

        try:
            y = int(row[3])
        except:
            y = None
        
        
        try:
            x = float(row[6])
        except:
            x = None

     
        site = Site(name=row[0], description=row[1], year=y, latitude = row[5], longitude = row[4], justification = row[3], area_hectares = x, category = c, region = r, iso = i, state = s)
        site.save()