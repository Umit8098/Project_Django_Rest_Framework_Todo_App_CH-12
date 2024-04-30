
## Project ToDo_App
```bash
- py -m venv env
# - python3.10 -m venv env
- ./env/Scripts/activate
- pip install djangorestframework
- pip install python-decouple
- pip freeze > requirements.txt
- django-admin startproject main .
```


- go to settings.py and add rest_framework;

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    # my_apps
    
    # 3rd_party_packages
    'rest_framework',
]
```

- create .env and .gitignore files, hidden to SECRET_KEY.
  
- Create .env file on root directory. We will collect our variables in this file.
- 
```py
from decouple import config

SECRET_KEY = config('SECRET_KEY')
```

```py
SECRET_KEY = o5o9...
```

- create app

```powershell
- py manage.py startapp todo
```

- go to settings.py and add our app;

```py
INSTALLED_APPS = [
    'django.contrib.admin',
    # my_apps
    'todo',
    # 3rd_party_packages
    'rest_framework',
]
```

- Migrate dbs:
```powershell
- python manage.py migrate
- py manage.py runserver
```

- Create superuser:
```powershell
- python manage.py createsuperuser
```

- Backend yazıyorsak bir application a ait db de birşeyler tutmak istiyoruzdur. Backend aslında db işlemleri, CRUD işlemleridir. db siz backend olmaz, relational olur non-relational olur farketmez, db de data tutacağımız anlamına gelir. Onun için ilk iş tabloları/modelleri ve relational ları belirlemektir.

- Modelimizi oluşturuyoruz;
models.py
```py
from django.db import models

# Create your models here.

class Todo(models.Model):
    PRIORITY = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]
    task = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    priority = models.SmallIntegerField(choices=PRIORITY, default=3)
    is_done = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.task
```

```text
[31/Dec/2022 17:07:48] "GET /admin/jsi18n/ HTTP/1.1" 200 3343
                                                      OK (karakter sayısı)
```

- karşılama sayfası için bir HttpResponse dönen function base bir view yazıp, endpoint ini tanımlayacağız. Sade olsun diye view imizi proje klasörü içinde oluşturacağız.
proj./views.py ->
```py
from django.http import HttpResponse

def home(request):
    return HttpResponse('<center><h1 style="background-color:powderblue; color:deeppink; padding:5px">Welcome to ApiTodo</h1></center>')
```

proj./urls.py ->
```py
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('todo/', include('todo.urls')),
]
```

- todo app imize de bir home page yazalım da kafalar karışmasın;
todo/views.py
```py 
@api_view()  # default GET
def todo_home(request):
    return Response({'home': 'This is todo home page.'})
``` 

todo/urls.py
```py 
from django.urls import path
from .views import todo_home

urlpatterns = [
    path('', todo_home, name='todo_home'),
]

``` 


- Şimdi todo app imizin viewlerini önce uzun uzun Function base olarak, daha sonra Concrete View ve ModelViewSet kullanarak kısa şekilde class base olarak yazacağız.

### Function Base Views leri ile yazalım;

- serializers dosyası create edip serializer ımızı yazıyoruz;

```py
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Todo
        fields = (  # normalde list içinde ama böyle de olur.
            'id',
            'task',
            'description',
            'priority',
            'is_done',
            'created_date',
        )
```

- views.py a gidip modelimizi ve serializer ımızı import ediyoruz,
- function base view de rest_framework kullanabilmemiz için @api_view() decoratoru kullanıyoruz, eğer kullanmazsak Response içerisine koyduğumuz dataları dönemiyor. Algılamıyor bunun bir json Response olduğunu.
- rest_framework ten api_view i import ediyoruz,
- rest_framework.response dan Response u import ediyoruz,
- Response mesajı için rest_framework ten status ü import ediyoruz,
        
```py
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

@api_view()  # default GET
def todo_home(request):
    return Response({'home': 'This is todo home page.'})


@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method == 'GET':
        # todos = Todo.objects.all()
        todos = Todo.objects.filter(is_done=False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)  # dışarıdan response ile gelen datayı serialize ediyoruz. data keywordü önemli.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

- Şimdi endpointimizi yazıyoruz;
todo/urls.py
```py
from django.urls import path
from .views import todo_home, todo_list_create

urlpatterns = [
    path('', todo_home, name='todo_home'),
    path('list-create/', todo_list_create, name='list'),
]
```

- test ettik çalıştı.
- Şimdi diğer view i mize geçiyoruz, neydi o detail e gitmemiz gereken endpointler

```py
@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, pk):
    
    todo = get_object_or_404(Todo, pk=pk)  # alttaki satırlarda kullandığımız aynı kodu tekrara düşmemek için yukarıda tanımlayıp buradan çekiyoruz.
    
    if request.method == 'GET':
        # todo = Todo.objects.get(pk=pk)  # eğer db de olmayan bir id ile istek atılırsa db hatası verir.Try exept içinde yazmalıyız.
        # todo = get_object_or_404(Todo, pk=pk)  # Try exept yerine kullandığımız yapı. import ediyoruz.
        serializer = TodoSerializer(todo)  # single bir obje dönüyor, queryset dönmüyor. many=True 'ya gerek yok.
        return Response(serializer.data) # status default 200 olduğu için yazmıyoruz.
    elif request.method == 'PUT':
        # todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoSerializer(data=request.data, instance=todo)  # kwarg alarak yazdığımız için parantez içinde nerede oldukları önemli değil. ama kwargs olarak değilde normal yazsaydık o zaman (todo, request.data) Yazmamız gerekecekti.
        # serializer = TodoSerializer(instance=todo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        todo.delete()
        return Response({'message': 'todo deleted successfully'})
```


- Şimdi endpointimizi yazıyoruz;
todo/urls.py
```py
from django.urls import path
from .views import (
    todo_home, 
    todo_list_create,
    todo_detail
)

urlpatterns = [
    path('', todo_home, name='todo_home'),
    path('list-create/', todo_list_create, name='list'),
    path('detail/<int:pk>', todo_detail, name='detail'),
]
```


### Class Base Views leri ile yazalım;
#### Concrete View Classes

- Genelde ModelViewSet Concrete leri kullanıyoruz.
- Önce rest_framework.generics den ListCreateAPIView ve RetrieveUpdateDestroyAPIView i import ediyoruz;

view.py
```py
#! Concrete View Classes

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class Todos(ListCreateAPIView):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer

class TodoDetail(RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    # lookup_field = 'id'  # default olan pk yerine id kullanılacaksa bunu belirtirsek url de id kullanabiliriz.
```

- Şimdi endpointimizi yazıyoruz;
todo/urls.py
```py
from django.urls import path
from .views import (
    todo_home, 
    # todo_list_create,
    # todo_detail,
    Todos,
    TodoDetail,
)

urlpatterns = [
    path('', todo_home, name='todo_home'),
    # path('list-create/', todo_list_create, name='list'),
    # path('detail/<int:pk>', todo_detail, name='detail'),

    path('list-create/', Todos.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
]
```


#### ViewSets 

- Önce rest_framework.viewsets den ModelViewSet i import ediyoruz;
views.py
```py
#! ViewSet Classes
from rest_framework.viewsets import ModelViewSet

class TodoMVS(ModelViewSet):
    queryset = Todo.objects.filter(is_done=False)
    serializer_class = TodoSerializer
```

- Şimdi endpointimizi yazıyoruz;
- Burada ModelViewSet kullandığımız için router yapısını import edip kullanacağız, 
- routers bir clas ve bizim bu class tan bir instance türetmemiz gerekiyor. Biz routers.DefaultRouter() dan bir instance türetip bunu router değişkenine tanımlıyoruz.
- Sonra b router instance ına register method u ile bir path belirleyip, bu path te hangi view i kullanacaksa onu yazıyoruz.
- En son da bu router ı urlpatterns e include edeceğiz.


todo/urls.py
```py
from django.urls import path, include
from rest_framework import routers

from .views import (
    todo_home,  
    TodoMVS
)

router = routers.DefaultRouter()
router.register('todo', TodoMVS)

urlpatterns = [
    path('', todo_home, name='todo_home'),
    path('', include(router.urls)),
]
# urlpatterns += router.urls
```

## pythonanywhere deployment

- Projeyi github a push layın. reponun görünürlüğünü Public olarak ayarlayın.
- pythonanywhere sign up oluyoruz.
- pythonanywhere free account içinde sadece 1 app konulabiliyor. Birden çok app konulacaksa, birden fazla e-mail ile birden fazla free account oluşturulup ve herbir free account a 1 app konulabilir.
- pythonanywhere default olarak olarak sql3 db sunuyor. free account ta postgresql için para ödemek gerekiyor.
  
- repoda bir değişiklik olduğunda deploy edilmiş app a değişiklikler otomatik yansımıyor. (pipline) Değişiklikleri repoya pushladıktan sonra, pythonanywhere e gidip, terminalden yapılan değişiklikler tekrardan çekilip!!, app i reload etmek gerekiyor.

- pythonanywhere -> dashboard -> New console -> $Bash yeni sekmede açıyoruz.
- pythonanywhere deki bash terminalde;
- rm -rf ....   ile eskilerini siliyoruz. (README.txt kalıyor.)
```bash
rm -rf klkf.txt
```

- github taki deploye edeceğimiz reponun url ini kopyalıyoruz (clonelar gibi)
- pythonanywhere deki bash terminale;

```bash
git clone https://github.com/Umit8098/Project_Django_Rest_Framework_Flight_App.git
```

- project imizi pythonanywhere clonladık.
- terminalde ls komutuyla dosyaları görüyoruz,
- projemizin içine, manage.py dosyasıyla aynı seviyeye geliyoruz (cd komutuyla), yani ls komutunu çalıştırdığımızda manage.py ı görmemiz lazım.

- Türkiyede cloud platformlar çok kullanılmıyor, genelde Dedicated Server lar üzerinden işlemler yapılıyor. Tüm proje o server içerisinde oluyor. Servera girip, projeyi clonlama işlemi yapılıyor, veya pipeline kuruluyor (localde bir değişiklik yapıldı, github a pushlandı, merge oldu, development server ından bu değişikliğin algılanıp canlıda değişiklik yapılması...). Bunun için github hook ları var, bu hooklar ile işlem yapılıyor.  Bir değişiklik olduğunda github hookları takip ediliyor, değişiklik olduğunda trigger ediyor, o trigger ile server ınızda otomatik git pull yapıyor, değişiklikleri çekiyor, projeyi yeni şekliyle ayağa kaldırıyor.

- Localde iken yapmamız gereken işlemlerin aynısını yapıyoruz;
    - virtual environment oluşturuyoruz,
    - bazı eski versiyonlarda python 2. versiyonu gelebiliyor. Önce "python --version" ile kontrol edilip, eğer 2. versiyon geliyorsa "python3 --version" ile bir daha kontrol edip bu sefer 3. versiyonun geldiğini görüp, "python3 -m venv env" ile virtual environment oluşturuyoruz.
    - "source env/bin/activate" komutu ile env yi aktif hale getiriyoruz.(Bu ortam linux ortamı olduğu için windows kullanıcıları da ancak bu komutla env aktif hale getirebilir.)
    - projenin dependency lerini (bağımlılıklarını) kuruyoruz.

```bash
- python --version
- python3 --version
- python3 -m venv env  # python -m venv env 
- source env/bin/activate
- pip install -r requirements.txt
```

  - pythonanywhere -> dashboard -> Web -> Add a new web app -> next -> Manual configuration (including virtualenvs) -> Python 3.10 (python versionu) -> next
        All done! Your web app is now set up. Details below. 
        (Hepsi tamam! Web uygulamanız artık kuruldu. Detaylar aşağıda.)
  - Artık app kuruldu ve app ile ilgili bir dashboard sundu bize. Burada manuel configurations lar yapacağız. 
        Bu site 28 Temmuz 2024 Pazar günü devre dışı bırakılacaktır. Buradan 3 ay daha app i çalıştırmak için bir button var.

- Şimdi yapacağımız işlemler -> 
  - Code:
        Source code: -> source codumuzu koyduğumuz yeri yazacağız.
        Working directory: -> source code ile aynı oluyor, bu directory de çalışacaksın diyoruz.  
        WSGI configuration file: -> manuel olarak update edeceğiz.
  - Virtualenv:
        Enter path to a virtualenv, if desired -> env nin nerede olduğunu göstereceğiz, yolunu vereceğiz.


- Source code: -> bash terminalde app in olduğu klasör içerisinde iken, "pwd" yazıp klasörün yolunu görebiliyoruz.
        /home/umit8098/Project_Django_Rest_Framework_Flight_App
- Working directory: -> Source code kısmına yazdığımız yolu buraya da yazıyoruz.
        /home/umit8098/Project_Django_Rest_Framework_Flight_App
- WSGI configuration file: Manuel configuration yaptığımız için bu WSGY (Web Server Gateway Interface) configuration u da kendimiz yapacağız. django application ile server arasındaki iletişimi sağlayan gateway. Bunda ayarlar yapmalıyız. sağ tıklayıp new tab ile yeni pencerede açıyoruz, Default olarak farmeworklerin ayar template leri var. 74-89 satırları arasında django kısmı var. Bunun haricindeki herşeyi siliyoruz, sadece django ile ilgili kısım kalıyor. İlk iki satır hariç yorumdan kurtarıyoruz.

```py
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/umit8098/mysite/mysite/settings.py'
# and your manage.py is is at '/home/umit8098/mysite/manage.py'
path = '/home/umit8098/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

```

- path kısmında bize manage.py ın yolunu vermemizi istiyor. Aslında source code umuzun olduğu path, biraz önce "pwd" ile almıştık, "/home/umit8098/Project_Django_Rest_Framework_Flight_App". Bunu path değişkenine tanımlıyoruz. Yani manage.py ımız bu klasörün içinde bunu söylüyoruz.

```py
path = '/home/umit8098/Project_Django_Rest_Framework_Flight_App'
```

- os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'  -> settings klasörümüzün bulunduğu yeri belirtiyoruz. Bizim settings klasörümüz main in altında. buraya 'main.settings' yazıyoruz.

```py
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
```


- save ediyoruz.

- Virtualenv: env yolunu vermemiz lazım. Tekrar console a geri dönüyoruz, 
  - env nin olduğu dizne gidiyoruz. (ls yaptığımızda env yi görüyoruz.) 
  - "cd env/" ile env nin dizinine giriyoruz. 
  - pwd yazıp env nin path'ini yani yolunu kopyalıyoruz.
  - kopyaladığımız path i Virtualenv kısmındaki bölüme yazıp tik e tıklıyoruz. env miz de hazır.

```py
/home/umit8098/Project_Django_Rest_Framework_Flight_App/env
```


- Genel olarak ayarlarımız tamam ama birkaç ayar daha kaldı.
  - SECRET_KEY, DEBUG, ENV_NAME, DJANGO_LOG_LEVEL=INFO (bu projeye özel)
  - Bunları ayarlayacağımız yer Source code kısmındaki Go to directory. sağ tıklayarak yeni sekmede açıyoruz,
  - projemizde bu verileri tuttuğumuz yer .env file ı idi. Açılan sekmede Files kısmına .env yazıp New File oluşturuyoruz. bize .env isminde yeni bir file oluşturdu. manage.py, requirements.txt ile aynı seviyede.
  - Eğer dev, prod şeklinde env mizi ayırmadıysak sadece .env deki değişkenleri tanımlamamız yeterli.
  - Ancak env miz dev ve prod olarak ayrılmış ise -> 
    - SECRET_KEY tanımladık, 
    - DEBUG=True  (Önce True yazıyoruz, hataları görebilmek için. daha sonra False a çekebiliriz.)
    - settings klasörünün __init__.py daki env değişkeninin ismine ne verdiysek onu alıp .env file ında değişken ismi olarak kullanıyoruz. ENV_NAME
    - ENV_NAME=dev  
        - prod ayarlarımızda db olarak postgresql var. bizim dev ayarlarını kullanmamız daha iyi. 
        - Ayrıca dev ayarlarını kullanırken de; debug.toolbar sadece localhost ta çalışıyor. Bu yüzden debug.toolbar ayarları ile development çalıştırılırsa hata verecektir. Bu hatayı almamak için dev.py daki debug.toolbar ayarlarını yoruma alıyoruz.
    - Bir de DJANGO_LOG_LEVEL=INFO ayarımız vardı onu da .env file ımıza ekliyoruz.

settings/dev.py
```py
from .base import *

# THIRD_PARTY_APPS = ["debug_toolbar"]

DEBUG = config("DEBUG")

# INSTALLED_APPS += THIRD_PARTY_APPS

# THIRD_PARTY_MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"]

# MIDDLEWARE += THIRD_PARTY_MIDDLEWARE

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# INTERNAL_IPS = [
#     "127.0.0.1",
# ]
```


- .env dosyamızın en son hali -> 

.env
```py
SECRET_KEY=o_zoo)sc$ef3bbctpryhi7pz!i)@)%s!ffg_zsxd^n+z+h5=7i
DEBUG=True
ENV_NAME=dev
DJANGO_LOG_LEVEL=INFO
```

- bash console a gidip db mizdeki tablolarımız oluşturacağız.
- (Biz projemizi github'a pushlarken db.sqlite3' yi de pushlamıştık. Yani db miz var. Eğer db'siz olarak github'a pushlayıp, oradan pythonanywhere'e deploye ediyorsak o zaman migrate ve superuser yapmamız gerekiyor.) 
- bash console da manage.py file ının bulunduğu dizine gidip db miz deki tablolarımızı oluşturuyoruz, superuser oluşturuyoruz,

```bash
python manage.py migrate
python manage.py createsuperuser
```

- dashboard a gidip Reload butonuna tıklıyoruz. Tüm değişiklikleri algılayacaktır. Daha sonra hemen bir üstte verdiği link ile projemizi pythonanywhere de yeni sekmede çalıştırıyoruz. admin panele giriyoruz,
- statics ler olmadan, css ler olmadan sayfamız geldi. 
- statics lerin görünmemesinin sebebi; django admin panel bir application ve bunun static file ları env içerisinde duruyor. Bunu localhost ta çalıştırdığımız zaman sıkıntı yaşamıyoruz ama canlı servera aldığımız zaman static root diye bir directory belirtmemiz gerekiyor. Static root, bütün environment ta olan static file ları veya application içerisinde varsa static file larımızı (css, javascript, image)  bunların hepsini tek bir klasör altında topluyor ve canlıdayken oradan çekiyor. Bu static ayarı nı yapmamız gerekiyor. Nasıl yapacağız;
- dashboadr -> Cource code -> Go to directory -> main -> settings -> base.py  içine STATİC_URL = 'static' altına STATIC_ROOT = BASE_DIR / 'static' yazıyoruz.

settings/base.py
```py
STATİC_URL = 'static'
STATIC_ROOT = BASE_DIR / 'static'
```

- base directory altında static isminde bir klasör oluştur, tüm static file ları bu static folder içerisinde topla demek için şu komutu (collectstatic) bash console da çalıştırıyoruz;

```bash
python manage.py collectstatic
```
- bu komut çalıştırıldıktan sonra; 197 adet static file kopyalandı ve belirttiğimiz folder altında toplandı.
" 197 static files copied to '/home/umit8098/Project_Django_Rest_Framework_Flight_App/main/static'. "

- Şimdi dashboarda gidip, web kısmında Static files: kısmında URL altında URL ini (/static/),  ve Directory altında path ini giriyoruz. (path ini zaten bize vermişti -> 197 static files cop..... kısmının sonunda. (/home/umit8098/Project_Django_Rest_Framework_Flight_App/main/static))
- girdikten sonra ✔ işareti ile kaydetmeliyiz.
  
```py
/static/
/home/umit8098/Project_Django_Rest_Framework_Flight_App/main/static
```

- Bu işlemi yaptıktan sonra değişikliklerin algılanması için tekrardan Reload butonuna tıklıyoruz. Artık sayfalarımızın statics leri de geliyor.

 - Şuanda backend projesi deploye edildi. Eğer bu backend için bir frontend yazılmış ise deploye edilmiş projenin endpointlerine istek atması gerekir. Mesela frontend kısmı React ile yazılmışsa istek atılacak endpointler düzenlenip netlify'a deploye edilip, oradan çalıştırılması daha uygun olur. 