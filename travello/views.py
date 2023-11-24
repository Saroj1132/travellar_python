from django.shortcuts import render
from .models import Destination,News

# Create your views here.

def index(request):

    dest1 = Destination()
    dest1.name = 'Mumbai'
    dest1.desc = 'The City That Never Sleeps'
    dest1.img = 'destination_1.jpg'
    dest1.price = 700
    dest1.offer = True

    dest2 = Destination()
    dest2.name = 'Hyderabad'
    dest2.desc = 'First Biryani, Then Sherwani'
    dest2.img = 'destination_2.jpg'
    dest2.price = 650
    dest2.offer = True

    dest3 = Destination()
    dest3.name = 'Bengaluru'
    dest3.desc = 'Beautiful City'
    dest3.img = 'destination_3.jpg'
    dest3.price = 750
    dest3.offer = False

    dest4 = Destination()
    dest4.name = "Surat"
    dest4.desc = "clean city"
    dest4.img = "destination_4.jpg"
    dest4.price = "895"
    dest4.offer = False

    dest5 = Destination()
    dest5.name = "Ahmedabad"
    dest5.desc = "Famous city"
    dest5.img = "destination_5.jpg"
    dest5.price = "910"
    dest5.offer = False

    dest6 = Destination()
    dest6.name = "Jaipur"
    dest6.desc = "Simple city"
    dest6.img = "destination_6.jpg"
    dest6.price = "485"
    dest6.offer = True

    dest7 = Destination()
    dest7.name = "Haridwar"
    dest7.desc = "Haridwar city"
    dest7.img = "destination_7.jpg"
    dest7.price = "420"
    dest7.offer = True

    dest8 = Destination()
    dest8.name = "Rajkot"
    dest8.desc = "Rajveer city"
    dest8.img = "destination_8.jpg"
    dest8.price = "350"
    dest8.offer = False

    dest9 = Destination()
    dest9.name = "kutch"
    dest9.desc = "registan city"
    dest9.img = "destination_9.jpg"
    dest9.price = "895"
    dest9.offer = True

    dests = [dest1, dest2, dest3, dest4, dest5, dest6, dest7, dest8, dest9]


    news1 = News()
    news1.img = "news_1.jpg"
    news1.day = "2"
    news1.month = "June"
    news1.title = "news 1 title"
    news1.text = "Pellentesque sit amet elementum ccumsan sit amet mattis eget, tristique at leo. Vivamus massa.Tempor massa et laoreet"

    news2 = News()
    news2.img = "news_2.jpg"
    news2.day = "1"
    news2.month = "June"
    news2.title = "news 2 title"
    news2.text = "Vivamus massa.Tempor massa et laoreet malesuada. Aliquam nulla nisl, accumsan sit amet mattis."

    news3 = News()
    news3.img = "news_3.jpg"
    news3.day = "31"
    news3.month = "May"
    news3.title = "news 3 title"
    news3.text = "Tempor massa et laoreet malesuada. Pellentesque sit amet elementum ccumsan sit amet mattis eget, tristique at leo."

    newses = [news1, news2, news3]

    return render(request, 'index.html', {'dests': dests, 'newses': newses})

def elements(request):
    return render(request, 'elements.html')

def news(request):
    return render(request, 'news.html')

def destinations(request):
    return render(request, 'destinations.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')