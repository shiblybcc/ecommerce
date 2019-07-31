# source /home/bcc/p3virtualenv/bin/activate
# django-admin.py startproject tryjango19 => creates a new project
# python manage.py runserver
# python manage.py migrate
# python manage.py shell
# change port
python manage.py runserver 8888
# auto move static files, css files
python manage.py collectstatic
# create super user
python manage.py createsuperuser
Username (leave blank to use 'bcc'): adminuser
Email address: my@exampl.com
Password: hello123
Password (again): hello123
# see all list of commands
python manage.py

# New package named music
python manage.py startapp music
python manage.py makemigrations music
python manage.py migrate # alway run this after migration to appy the changes
python manage.py sqlmigrate music 0001  # check the sql command for the migration

**Everytime database migration or database change is done, need to restart server**

# different model fields
https: // docs.djangoproject.com / en / 2.2 / ref / models / fields /
# guids
https://github.com/codingforentrepreneurs/Guides


# Django database API
from music.models import Album, Song
Album.objects.all()
a = Album(artist='Taylor swift', album_title='Red', genre='Country', 'album_logo'='http://www.hipsterpig.com/wp-content/uploads/2014/05/fc550x550orange17.jpg')
a.save()
a.album_title

**Save another way**
b = Album()
b.artist = "Myth"
b.album_title = 'high scholl'
b.genre = 'pubk'
b.album_logo = 'http://www.hipsterpig.com/wp-content/uploads/2014/05/fc550x550orange17.jpg'
b.save()


>>> Album.objects.filter(id=1)
<QuerySet [<Album: Red _ Taylor swift>]>
>>> Album.objects.filter(artist__startswith='Taylor')
<QuerySet [<Album: Red _ Taylor swift>]>

>>> a = Album.objects.all().get(id=1)
<Album: Red _ Taylor swift>
>>> a.song_set.all()
<QuerySet [<Song: Song object (1)>]>

>>> a.song_set.create(song_title="love u", file_type='mp3')
<Song: Song object (2)>

>>> a.song_set.count()
2




























