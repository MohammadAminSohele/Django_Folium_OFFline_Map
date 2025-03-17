**intro**

Hello guy's 
In this project user can send latitude and longitude coordination to show location and mark it offline to in this project

And I support 3 city's in iran 🇮🇷 such as :
1.Pardis
2.Tehran
3.Boomehen

**technology**

In this project I use several technology's such as :
- Django : this is my Web framework to handle request and response and show map to offline
- Folium : to analyse user lat and long coordination , create map and mark coordination in offline mode
- Mobile atlas creator : this is a application that I use to create my own map with z x y format file it's mean in final of convert map you may see a zip file and when you extract it you see several folder in folders to final see some jpg picture format , this our offline map these pictures are changed by zoom in and zoom out in map 

**Start The project**
1.For first time you should create a virtualenv to install projects package with this command 
```
python -m venv venv
```

2. In this step you should install packages that exist in requirements file in project with this command:
```
pip install -r reqirments.txt
```
3. After previous step you should some initial command that relation to Django Web framework: 

to collect some static file that is emergency for my template project use this command: 
```
python manage.py collectstatic
```
Now in this step you should download some zip file that Is my dataset to use this for work map offline with this link:
[]()https://drive.google.com/drive/folders/1Vrb8kbJUjS1-pIKkt9-uTA2O4d1kPgon?usp=sharing

If you are interested to see process of download these file you can see these pictures in this link:
[]()https://drive.google.com/drive/folders/16Nwqjpq5jFhvnS-OLJyrn_X2qyiiqkRu?usp=sharing

So let's continue 

After that you collectstatic with top command you should create folder In static_cdn folder called media I set this folder in my settings to use media files in this path , extract zip file put them in this folder be careful that every extract folder doesn't have fatherfolder it's alone forexample Tehran with another sub folders  

And after this step you should run The project with this command;
```
python manage.py runserver
```
With this command The project it is run in port 8000
