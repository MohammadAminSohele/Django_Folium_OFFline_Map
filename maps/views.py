from django.shortcuts import render

import folium

from .forms import CoordinatesForm

# Create your views here.

def Show_cordination_Pardis(request):    
    if request.method=='POST':
        form=CoordinatesForm(request.POST or None)
        if form.is_valid():
            lat=form.cleaned_data.get('lat')
            long=form.cleaned_data.get('long')
            m=folium.Map(location=[lat,long],tiles='/media/Pardis/{z}/{x}/{y}.png',attr='Pardis',zoom_start=14)
            folium.Marker(location=[lat,long],popup='لوکیشن مختصات وارد شده').add_to(m)
            m.save('Pardisindex.html')
            context={
                'map':m._repr_html_(),
                'form':form
            }
            return render(request,'Pardis.html',context)
    else:
        form=CoordinatesForm()
        context={'form':form}
        return render(request,'Pardis.html',context)

def Show_cordination_Tehran(request):    
    if request.method=='POST':
        form=CoordinatesForm(request.POST or None)
        if form.is_valid():
            lat=form.cleaned_data.get('lat')
            long=form.cleaned_data.get('long')
            m=folium.Map(location=[lat,long],tiles='/media/Tehran/{z}/{x}/{y}.png',attr='Tehran',zoom_start=14)
            folium.Marker(location=[lat,long],popup='لوکیشن مختصات وارد شده').add_to(m)
            m.save('Tehranindex.html')
            context={
                'map':m._repr_html_(),
                'form':form
            }
            return render(request,'Tehran.html',context)
    else:
        form=CoordinatesForm()
        context={'form':form}
        return render(request,'Tehran.html',context)
    
def Show_cordination_Bomehen(request):    
    if request.method=='POST':
        form=CoordinatesForm(request.POST or None)
        if form.is_valid():
            lat=form.cleaned_data.get('lat')
            long=form.cleaned_data.get('long')
            m=folium.Map(location=[lat,long],tiles='/media/Bomehen/{z}/{x}/{y}.png',attr='Bomehen',zoom_start=14)
            folium.Marker(location=[lat,long],popup='لوکیشن مختصات وارد شده').add_to(m)
            m.save('Bomehenindex.html')
            context={
                'map':m._repr_html_(),
                'form':form
            }
            return render(request,'Bomehen.html',context)
    else:
        form=CoordinatesForm()
        context={'form':form}
        return render(request,'Bomehen.html',context)