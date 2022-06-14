from django.db import migrations, models

def populate_houses(apps, schema_editor):
    House = apps.get_model('housePointsApp', 'House')

    slytherin = House(name='Slytherin', points=0, color="green")
    slytherin.save()
    ravenclaw = House(name='Ravenclaw', points=0, color="blue")
    ravenclaw.save()
    hufflepuff = House(name='Hufflepuff', points=0, color="yellow")
    hufflepuff.save()
    gryffindor = House(name='Gryffindor', points=0, color="red")
    gryffindor.save()

class Migration(migrations.Migration):

    dependencies = [
        ('housePointsApp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_houses),
    ]
    
