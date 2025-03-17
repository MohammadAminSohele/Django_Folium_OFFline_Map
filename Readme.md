## intro

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

## My experience in this project 
I create this project by order of my Ai professor Shamsipoor college 

I search many to how can i get lat and long from user and show location in map to offline mode 

Because I have skill in python language and Django Web framework I focus to handle The project with these technologies 

So I search many in Google search engine and I have many conversations to Ai nlp services such as copoiet,  gemeni , and chatgpt I realised that my best package to Do it this Project it's Folium Package that is python Package that have many ability to make masterpiece feature but I use so many little ability to progress my Project 

I install necessary packages and I create django project and a sample view to test my Django framework work correct

- Let's talk about Django structure :
Django have some necessary files 
Origin file in every django project it's Views.py file that in this file we handle  forms class in forms.py file with this file we can create forms class to user send thir info but with our data type in this project I prefer to use decimal field to get lat and long from user .

I don't use models file because I don't prefer to store data from user or from panel admin these data are temporary and I use them in folium 
And that's it

- Now let's talk about How folium work in this my Project 
I import folium Package to Views.py file 
And use Map method to create our map in location argument you should send you lat and long that user send to create map base on coordination , and for tiles argument I send my dataset path with z x y format , and if you don't use this argument create Map with open street api , and attr argument that is necessary when you use tiles argument 
After that I create map I use Marker method to mark my coordination you should again use location argument , after this argument you can use popup argument when user click on Marker show a message to him and use add method to add location to our map and finally we store our temporary info and necessary dependency to create map and show Marker 

And we do all this for another city but with suitable dataset map

**🌹Thanks and appreciation to the respected teacher sir MojtabaFar🌹**
