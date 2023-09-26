# Tugas PBP Ganjil 2023/2024

**Nama    : Bulan Athaillah Permata Wijaya**<br>
**NPM     : 2206032135**<br>
**Kelas   : PBP C**<br>

## Tugas 4
### Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?
Django `UserCreationForm` merupakan _built-in_ form milik Django untuk sistem autentikasi registrasi _user_. Kelebihan dari `UserCreationForm` adalah:
- Cepat dan mudah digunakan karena dapat diintegrasikan ke dalam proyek Django hanya dengan beberapa baris kode saja.
- Memiliki sistem keamanan yang kuat karena `UserCreationForm` sudah secara otomatis melakukan _password hashing_ yang menyebabkan peretas sulit dalam mengakses _password_ biasa. `UserCreationForm` sudah terintegrasi dengan sistem autentikasi milik Django sehingga implementasi fitur seperti _login_, _reset password_, dan sebagainya menjadi lebih mudah.
- Kompatibel dengan berbagai _extensions_ dan aplikasi pihak ketiga karena `UserCreationForm` merupakan bagian dari _library_ standar Django.

Sedangkan kelemahan dari `UserCreationForm` adalah:

- Kurang fleksibel karena untuk registrasi yang kompleks, `UserCreationForm` terlalu sederhana. Sehingga jika kita ingin menambahkan fitur tambahan perlu untuk membuat form baru atau _extend_ form yang sudah ada tersebut.
- Desainnya bisa saja kurang sesuai dengan konsep yang diinginkan pada situs web kita sehingga perlu untuk dipersonalisasikan lagi tampilan formnya.
- `UserCreationForm` sangat bergantung kepada sistem autentikasi Django sehingga akan kurang cocok bagi proyek yang ingin menambahkan metode autentikasi eksternal.

### Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi merupakan proses verifikasi identitas pengguna, sistem, atau entitas yang mencoba mengakses sebuah _platform_. Autentikasi biasanya melibatkan kata sandi atau biometrik seperti sidik jari dan _face recognition_ untuk mengkonfirmasi identitas.

Otorisasi merupakan proses verifikasi apakah pengguna, sistem, atau entitas dapat memiliki akses ke sebuah _platform_ tersebut. Otorisasi memastikan bahwa pengguna hanya dapat mengakses ke sumber daya yang relevan sesuai dengan peran mereka saja. 

Setelah data pengguna melalui tahap autentikasi, Otorisasi akan mendefinisikan aksi dan fitur apa yang dapat pengguna pakai dan data apa yang dapat mereka akses. Kedua hal ini sangat penting dan berpengaruh dalam meningkatkan keamanan pada _platform_ serta untuk mengurangi risiko kebocoran data.

### Apa itu _cookies_ dalam konteks aplikasi web, dan bagaimana Django menggunakan _cookies_ untuk mengelola data sesi pengguna?
_Cookies_ merupakan sejumlah informasi yang dikirim oleh server web ke _browser_ dan kemudian akan dikirim kembali oleh browser untuk permintaan halaman mendatang. _Cookie_ digunakan untuk otentikasi, manajemen sesi, personalisasi, dan pelacakan.

Django menggunakan _cookies_ untuk menyimpan data sesi pengguna yang dinamakan dengan _session id_. _Session id_ akan menyimpan _key_ dari sesi ke dalam _browser_. Data sesi yang sebenarnya akan disimpan di dalam _database_. Pada permintaan berikutnya, _browser_ akan mengirimkan _cookies sessionid_ ke server. Django memanfaatkan _cookies_ ini untuk mengambil data sesi pengguna dan membuatnya dapat diakses di dalam kode program. Fitur _session_ ini akan otomatis diaktifkan ketika kita memulai sebuah proyek Django.

### Apakah penggunaan _cookies_ aman secara _default_ dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
_Cookies_ sangat aman jika diimplementasikan dengan benar. Akan tetapi terdapat beberapa risiko potensial yang harus diwaspadai seperti:

- _Cookie Poisoning_. Dimana penyerang mencoba memodifikasi isi _cookies_ dan merusak _cookies_ pengguna.
- _Cross-Site Scripting_ (XSS). Jika seseorang berhasil melakukan serangan XSS mereka bisa mendapatkan akses _session cookies_ dan mengakses situs web sebagai pengguna tersebut.
- _Cookie Sniffing_. Jika situs web tidak menggunakan HTTPS maka _cookies_ bisa dengan mudah untuk diambil oleh peretas yang memantau lalu lintas jaringan. Hal ini dapat mengarah kepada pencurian sesi.
- Kebocoran Data. _Cookies_ akan senantiasa mengirimkan data ke server setiap permintaan HTTP dibuat. Jika terdapat data sensitif yang disimpan dalam _cookies_, ada risiko terjadinya kebocoran data ketika _cookies_ diambil oleh peretas.

### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_
1. Pertama-tama saya mengaktifkan _virtual environment_ terlebih dahulu. Setelah itu saya meng-_import_ `UserCreationForm` dan `messages` pada `views.py` agar dapat membuat form registrasi. Saya menambahkan fungsi `register` pada `views.py` untuk membuat form secara otomatis menggunakan fitur _built-in_  dari Django.
```
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```
Setelah itu, saya menambahkan berkas HTML baru `signup.html` pada `main` sebagai _template_ untuk halaman _signup_.

2. Melakukan _import_ `register` pada `urls.py` dan menambahkan _routing_ baru pada `urlpatterns` dengan menambahkan kode berikut.
```
path('signup/', register, name='signup'),
```

3. Setelah menambahkan fitur _signup_, saya kemudian menambahkan fitur _login_. Pertama saya meng-_import_ `authenticate` dan `login` pada `views.py`. Selanjutnya saya menambahkan fungsi `login_user`untuk autentikasi pengguna yang ingin _login_ sebagai berikut.
```
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main:show_main')
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```
Kemudian saya menambahkan berkas HTML baru `login.html` pada `main` sebagai _template_ untuk halaman _login_.

4. Melakukan _import_ `login_user` pada `urls.py` dan menambahkan _routing_ baru pada `urlpatterns` dengan menambahkan kode berikut.
```
path('login/', login_user, name='login'),
```
5. Setelah itu, saya menambahkan fitur _logout_. Pertama saya menambahkan _import_ `logout` pada `views.py`. Kemudian, saya membuat fungsi `logout_user` agar aplikasi dapat melakukan mekanisme _logout_ seperti berikut.
```
def logout_user(request):
    logout(request)
    return redirect('main:login')
```
Sehabis itu, saya menambahkan _button_ baru pada `main.html` dengan _hyperlink tag_ yang akan mengarahkan _user_ untuk keluar.

6. Melakukan _import_ `logout_user` pada `urls.py` dan menambahkan _routing_ baru pada `urlpatterns` dengan menambahkan kode berikut.
```
path('logout/', logout_user, name='logout'),
```

7. 

## Tugas 3
### Apa perbedaan antara form `POST` dan form `GET` dalam Django?
- Form `GET` digunakan untuk meminta data dari server. Hal ini menyebabkan data pada `GET` dapat dilihat oleh siapapun pada URL. Form `GET` juga memiliki limitasi dalam ukuran. Form `GET` hanya bisa mengakses data dalam tipe _string_ saja.
- Form `POST` mengirimkan data ke server melalui _body_ dari HTTP _request_. Hal ini menyebabkan data pada `POST` tidak dapat dilihat di URL sehingga menjamin keamanan pada data. Form `POST` juga tidak memiliki limitasi dalam ukuran data yang dimasukkan dan mendukung berbagai tipe data seperti _string_, _numeric_, dan _binary_.

### Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML (_Exstensible Markup Language_) merupakan sebuah _markup language_ yang digunakan untuk mewakili data dalam format yang terstruktur. XML menggunakan _tag_ untuk mendefinisikan elemen data. XML dapat digunakan untuk mewakili berbagai jenis data. XML biasanya digunakan untuk pertukaran data, file konfigurasi, dan menyimpan data terstruktur yang dapat dibaca oleh manusia.
- JSON (_JavaScript Object Notation_) merupakan format data yang digunakan untuk merepresentasikan data dalam format yang mudah untuk dibaca. JSON menggunakan kurung kurawal dan tanda kutip untuk mendefinisikan struktur data. JSON terdiri atas _key-value pairs_, dimana _key_-nya dapat berupa _string_, _numeric_, _object_, _array_, _boolean_, atau _null_. JSON biasanya digunakan untuk _web APIs_, file konfigurasi, dan penyimpanan data dalam basis data.
- HTML (_Hypertext Markup Language_) merupakan sebuah _markup language_ yang digunakan untuk menampilkan data pada web. HTML menggunakan _tag_ untuk mendefinisikan struktur dan tata letak dokumen web. HTML tidak digunakan untuk pertukaran data atau penyimpanan data seperti XML dan JSON, melainkan untuk merepresentasikan data dalam halaman web.

### Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern
Hal ini dikarenakan JSON memiliki beberapa kelebihan dibandingkan dengan format data yang lain, diantaranya:<br>
- JSON merupakan format yang ringan dan mudah untuk di-_parse_. Oleh karena itu, JSON merupakan format yang ideal untuk pertukaran data melalui web, dimana _bandwith_ dan kinerja merupakan pertimbangan penting.
- JSON mudah dibaca, bahkan untuk orang yang tidak terlalu biasa dengan bahasa pemrograman. Hal ini membuat JSON ideal untuk _debugging_.
- JSON tidak terikat dengan bahasa pemrograman tertentu sehingga dapat digunakan dengan berbagai bahasa pemrograman dan platform.
- JSON sangat fleksibel digunakan karena dapat merepresentasikan berbagai tipe data.
- JSON didukung luas oleh seluruh _web browser_ dan bahasa pemrograman. Hal ini memudahkan dalam pengembangan aplikasi web yang menggunakan JSON untuk pertukaran data.

### Jelaskan bagaimana cara kamu mengimplementasikan _checklist_ di atas secara _step-by-step_
1. Pertama, saya menjalankan _virtual environment_ terlebih dahulu. Lalu saya mengubah _routing_ `main/` ke `/` dengan mengubah _path_ `main/` pada `urls.py` untuk menyesuaikan dengan konvensi yang ada.
2. Selanjutnya saya implementasi _skeleton_ sebagai kerangka _views_ untuk situs web. Hal ini dilakukan dengan membuat `base.html` di _folder_ `templates` pada _root_. `base.html` merupakan kerangka umum untuk halaman web pada proyek ini. Kemudian saya mengubah `settings.py` pada subdir `orbit_tune` menjadi seperti berikut agar `base.html` terdeteksi sebagai _template_.
```
...
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR / 'templates'],
        ...
    }
]
...
```

Setelah itu sesuaikan berkas `main.html` pada direktori `main` dengan _template_ utama yang telah dibuat.

3. Membuat berkas baru `forms.py` pada `main` untuk membuat struktur _form_ sederhana yang dapat menginput data barang baru dengan kode berikut. 
```
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "brand", "type", "amount", "description"]
```

4. Meng-_import_ hal-hal yang diperlukan pada `views.py` di folder `main`, yakni `HttpResponseRedirect`, `ProductForm`, `reverse`, dan `Item`. Kemudian, saya membuat fungsi baru `create_item` untuk menghasilkan sebuah formulir yang dapat menambahkan barang baru secara otomatis ketika men-_submit_ data di _form_ dengan kode seperti ini.
```
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    
    context = {'form': form}
    return render(request, "create_item.html", context)
```

5. Mengubah fungsi `show_main` pada `views.py` menjadi seperti berikut.
```
def show_main(request):
    #Mengambil seluruh object Item pada database
    items = Item.objects.all() 

    #Menghitung berapa object Item yang telah disimpan
    items_count = items.count()

    context = {
        'items': items,
        'items_count': items_count
    }

    return render(request, "main.html", context)
```

6. Membuat berkas `create_item.html` pada `templates` di `main` dengan kode seperti di bawah untuk membuat tampilan laman _form_ agar dapat menambah _object_ baru item.
```
{% extends 'base.html' %} 

{% block content %}
<style>
    body {
        font-family: Helvetica;
    }
    input[type=text], input[type=number] {
        width: 100%;
        padding: 12px 20px;
        box-sizing: border-box;
    }
    input[type=button], input[type=submit] {
        width: 50%;
        padding: 12px 14px;
    }
    label {
        margin: 10px;
        float: left;
    }
</style>

<h1>Add New Instrument</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Instrument"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

7. Memodifikasi `main.html` dengan menambahkan potongan kode di bawah untuk menampilkan item yang telah di input oleh _user_ dalam tabel dan menambah tombol yang akan mengarah menuju ke laman `create_item`. Saya disini menambahkan fitur pesan yang akan memberitahu _user_ berapa banyak _object_ Item yang telah dimasukkan ke dalam aplikasi sebelum tabel.
```
...
{% block content %}
    <style>
        body {
            text-align: center;
            font-family: Helvetica;
        }
        table, th, td {
            width: 560px;
            border: 1px solid black;
            border-collapse: collapse;
            text-align: center;
            margin-left: auto;
            margin-right: auto;
        }
        button {
        width: 150px;
        padding: 5px 10px;
        }
    </style>

    <h1>OrbitTune</h1>
    <h3>An Easier Way to Keep Track of your Instruments!</h3>
    <p>You have inserted <b>{{ items_count }}</b> instrument in this app</p>

    <table>
        <tr>
            <th>Name</th>
            <th>Brand</th>
            <th>Type</th>
            <th>Amount</th>
            <th>Description</th>
        </tr>
    
        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}
    
        {% for item in items %}
            <tr>
                <td>{{item.name}}</td>
                <td>{{item.brand}}</td>
                <td>{{item.type}}</td>
                <td>{{item.amount}}</td>
                <td>{{item.description}}</td>
            </tr>
        {% endfor %}
    </table>
    
    <br />
    
    <a href="{% url 'main:create_item' %}">
        <button>
            Add New Instrument
        </button>
    </a>
...
```

8. Setelah membuat _form_ dan menampilkan data dalam HTML, kemudian says membuat fitur untuk mengembalikan data dalam bentuk XML, JSON, XML by id, dan JSON by id. Pertama, tambahkan _import_ pada `views.py` terlebih dahulu yakni `HttpResponse` dan `serializers`. Kemudian saya membuat empat fungsi (`show_xml`, `show_json`, `show_xml_by_id`, dan `show_json_by_id`) sebagai berikut.
```
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

Dalam setiap fungsi tersebut terdapat variabel data yang akan menyimpan hasil _query_. Untuk fungsi `show_xml_by_id` dan `show_json_by_id` menggunakan `.filter(pk=id)` untuk menyimpan hasil _query_ data dengan id yang ditentukan. Seluruh fungsi tersebut akan mengembalikan hasil _query_ yang sudah diserialisasi sesuai dengan format data yang dibutuhkan, yakni XML atau JSON.

9. Selanjutnya saya mengimpor fungsi-fungsi yang telah dibuat pada `urls.py` di folder `main` sebagai berikut.
```
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id
```

Setelah itu saya melakukan _routing url_ dengan menambahkan _path_ pada `urlpatterns` untuk mengakses fungsi-fungsi yang telah dibuat.
```
...
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
```

10. Terakhir, saya menjalankan proyek Django pada terminal dengan perintah `python manage.py runserver` dan membuka `localhost` untuk melihat hasil dari berbagai format yang dapat digunakan untuk melihat objek model. Saya juga menggunakan Postman untuk melihat data dengan hasil yang dapat dilihat pada _screenshot_ berikut.

### _Screenshot_ hasil URL pada Postman
**1. Melihat data format HTML**<br>
<img width="800" alt="Screenshot 2023-09-18 194734" src="https://github.com/bulanath/orbit-tune/assets/104998027/69839e0e-42a6-41a0-a0da-16121daea786">
<br><br>**2. Melihat data format XML**<br>
<img width="800" alt="Screenshot 2023-09-18 194714" src="https://github.com/bulanath/orbit-tune/assets/104998027/f6ed0f7b-cf28-4870-aa4f-10bbfc18bdfd">
<br><br>**3. Melihat data format JSON**<br>
<img width="800" alt="Screenshot 2023-09-18 194656" src="https://github.com/bulanath/orbit-tune/assets/104998027/efd1010b-6330-487c-83d3-8f4ed4a2efbb">
<br><br>**4. Melihat data format XML by id**<br>
<img width="800" alt="Screenshot 2023-09-18 194621" src="https://github.com/bulanath/orbit-tune/assets/104998027/054a922d-03f3-46a1-bf24-c3563a420d1d">
<br><br>**5. Melihat data format JSON by id**<br>
<img width="800" alt="Screenshot 2023-09-18 194559" src="https://github.com/bulanath/orbit-tune/assets/104998027/fd28b6e2-fe89-4f7a-9dba-3b6a49e31a1f">

## Tugas 2
### Cara mengimplementasikan <i>checklist</i> tugas secara <i>step-by-step</i>
1. Agar dapat membuat proyek Django baru, pertama-tama saya membuat folder `orbit-tune` pada direktori lokal. Kemudian saya membuat dan mengaktifkan <i>virtual environment</i> melalui terminal. 
2. Membuat file teks `requirements.txt` berisi berbagai <i>dependencies</i> yang diperlukan yaitu:<br>
```
django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
```
3. Kemudian melakukan instalasi <i>dependencies</i> dengan perintah `pip install -r requirements.txt` pada terminal.
4. Membuat proyek Django baru bernama `orbit_tune` dengan menjalankan perintah `django-admin startproject orbit_tune .`.
5. Setelah itu, saya menambahkan perubahan pada `ALLOWED_HOSTS` di `settings.py` menjadi `ALLOWED_HOSTS = ["*"]` untuk mengizinkan semua host mendapat akses agar aplikasi dapat diakses secara luas.
6. Menjalankan server Django dengan menggunakan perintah `python manage.py runserver` dan kemudian melihat animasi roket saat web dibuka melalui <i>localhost</i> menandakan bahwa aplikasi Django telah berhasil dibuat.
7. Menghentikan <i>server</i> dan <i>virtual environment</i> agar dapat mengunggah proyek menuju repositori GitHub.
8. Membuat repositori GitHub baru bernama `orbit-tune` dan menghubungkannya dengan direktori lokal dengan memasukkan perintah `git remote add origin https://github.com/bulanath/orbit-tune.git` melalui terminal.
9. Menambahkan berkas `.gitignore` untuk menentukan mana saja berkas dan direktori yang harus diabaikan oleh Git.
10. Melakukan `add`,`commit`, dan `push` dari direktori lokal ke repositori untuk pertama kalinya.
11. Mengaktifkan kembali <i>virtual environment</i> menggunakan terminal pada direktori lokal `orbit-tune`.
12. Setelah itu, saya membuat aplikasi baru bernama `main` pada proyek `orbit-tune` dengan menjalankan perintah `python manage.py startapp main`.
13. Mendaftarkan aplikasi `main` ke dalam proyek dengan menambahkan `'main'` ke dalam variabel `INSTALLED_APPS` pada `settings.py`.
14. Menambahkan direktori baru bernama `template` dalam direktori `main`. Di dalamnya membuat berkas baru `main.html` dengan isi seperti berikut:<br>
```
<h1>OrbitTune</h1>
<h3>An Easier Way to Keep Track of your Instruments!</h3>

<h5>Instrument: </h5>
<p>Guitar</p>
<h5>Brand: </h5>
<p>Fender</p>
<h5>Type: </h5>
<p>Telecaster</p>
<h5>Amount: </h5>
<p>2</p>
<h5>Description: </h5>
<p>In good conditions</p>
```
15. Mengubah `models.py` pada direktori `main` dengan kode berikut:<br>
```
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
```
Saya mendefinisikan `Item` sebagai nama model. Atribut yang saya gunakan pada model adalah `nama`,`merek`,`tipe`,`jumlah`, dan `deskripsi`. Setiap atribut telah menggunakan dengan tipe data yang sesuai.

16. Karena telah menambahkan model baru, selanjutnya saya melakukan migrasi model pada Django. Pertama saya menciptakan berkas migrasi dengan perintah `python manage.py makemigrations`. Setelah itu, saya mengaplikasikan model yang baru saja ditambahkan ke basis data dengan perintah `python manage.py migrate`.
17. Menghubungkan <i>view</i> dengan <i>template</i> dengan menambahkan kode berikut pada `views.py` dalam direktori aplikasi `main`.
```
from django.shortcuts import render

def show_main(request):
    context = {
        'instrument': 'Guitar',
        'brand': 'Fender',
        'type': 'Telecaster',
        'amount': '2',
        'description': 'In good conditions'
    }

    return render(request, "main.html", context)
```
Data yang telah dimasukkan ke dalam <i>dictionary</i> `context` pada fungsi `show_main` akan ditampilkan ke dalam HTML dengan bantuan fungsi `render` yang telah di <i>import</i>.

18. Memodifikasi `main.html` dari statis menjadi kode Django agar dapat menampilkan data dari model.
```
...
<h5>Instrument: </h5>
<p>{{ instrument }}</p>
<h5>Brand: </h5>
<p>{{ brand }}</p>
<h5>Type: </h5>
<p>{{ type }}</p>
<h5>Amount: </h5>
<p>{{ amount }}</p>
<h5>Description: </h5>
<p>{{ description }}</p>
```

19. Membuat <i>routing</i> URL pada aplikasi `main` dengan membuat `urls.py` dan diisi dengan kode berikut:<br>
```
from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
]
```
Setelah itu, saya membuat <i>routing</i> URL pada proyek `orbit-tune` dengan mengubah dan menambahkan `urls.py` menjadi:<br>
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls')),
]
```
<i>Routing</i> dilakukan agar aplikasi `main` yang telah dibuat dapat diakses melalui web dengan tampilan HTML.

20. Kemudian, saya membuat unit _test_ dengan mengisi `tests.py` pada `main` dengan kode di bawah ini:<br>
```
from django.test import TestCase, Client

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_content(self):
        response = Client().get('/main/')
        self.assertContains(response, "OrbitTune")
        self.assertNotContains(response, "Penyimpanan alat musik")
```

Tes pertama, `test_main_url_is_exist` berfungsi untuk mengecek apakah _path_ URL `/main/` dapat diakses. Tes kedua, `test_main_using_main_template` befungsi untuk mengecek apakah halaman `/main/` di-_render_ menggunakan _template_ `main.html`. Dan tes ketiga, `test_main_content` saya buat sendiri berfungsi untuk mengecek apakah konten-konten tersebut terdapat pada halaman `/main` atau tidak.

21. Setelah membuat unit _test_, saya menjalankan tes dengan menggunakan perintah `python manage.py test`. Tes yang dilakukan berhasil karena mengeluarkan informasi berikut.<br>
```
Found 3 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
...
----------------------------------------------------------------------     
Ran 3 tests in 0.020s

OK
Destroying test database for alias 'default'...
```
22. Melakukan `add`,`commit`, dan `push` ke dalam repositori GitHub setelah berhasil mengimplementasikan MVT pada Django.
23. Melakukan <i>deployment</i> repositori `orbit-tune` menggunakan Adaptable. Template <i>deployment</i> yang digunakan adalah `Python App Template` dan tipe basis data yang digunakan adalah `PostgreSQL`.

### Bagan yang berisi <i>request client</i> ke web aplikasi berbasis Django beserta responnya
<img width="503" alt="Bagan request client Bulan" src="https://github.com/bulanath/orbit-tune/assets/104998027/f797b92d-4c37-469c-9fc2-f0600b012823"><br>
Pada awalnya, klien membuat permintaan HTTP ke URL tertentu yang didefinisikan di dalam `urls.py`. `urls.py` berfungsi untuk mendefinisikan URL _patterns_ dan memetakannya ke fungsi _view_ yang spesifik. Dalam `urls.py` akan ditentukan fungsi _view_ mana yang harus dipanggil untuk setiap URL _pattern_. Kemudian, fungsi pada `views.py` memproses permintaan HTTP tersebut dan berinteraksi dengan `models.py` untuk mengakses data pada _model_. Setelah itu, fungsi _view_ akan menggunakan `main.html` sebagai _template_ HTML untuk me-_render_ tampilan HTML. _Template_ HTML tersebut akan menggunakan data dari `views.py` yang disisipkan menggunakan sintaks Django yang telah didefinisikan dalam variabel `context`. _Template_ HTML yang telah di-_render_ akan dikirimkan kembali ke klien dalam bentuk respon HTTP. Peramban web klien akan menerima respon tersebut dan menampilkannya pada halaman web klien.

### Jelaskan mengapa kita menggunakan <i>virtual environment</i>? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan <i>virtual environment</i>?
<i>Virtual environment</i> digunakan untuk mengisolasi <i>dependencies</i> dan <i>package</i> yang dibutuhkan dari aplikasi sehingga tidak terjadi tabrakan antar versi lain yang ada pada komputer. Misalnya jika kita sedang mengerjakan dua aplikasi web berbasis Django, dimana yang satu menggunakan `Django 4.1` dan yang satu lagi menggunakan `Django 4.2`. Agar <i>dependencies</i> kedua aplikasi dapat terjaga, diperlukan penggunaan <i>virtual environment</i>.<br>

Kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan <i>virtual environment</i>. Akan tetapi, hal tersebut tidak direkomendasikan karena ada beberapa risiko yang mungkin terjadi. Diantaranya adalah:<br>
- Tidak sengaja mengunduh <i>dependency</i> yang memiliki konflik dengan proyek Django lain pada komputer.
- Melakukan <i>upgrade</i> atau <i>downgrade dependency</i> yang dapat merusak proyek.
- Menjadi lebih sulit untuk melakukan <i>debugging</i> pada proyek.<br>

Hal di atas dapat terjadi karena tidak adanya isolasi <i>dependencies</i> antar proyek karena tidak mengimplementasikan <i>virtual environment</i> dalam membuat aplikasi Django.

### Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya

- MVC merupakan singkatan dari <i>Model-View-Controller</i>. MVC merupakan salah satu konsep arsitektur untuk pengembangan web yang memberlakukan <i>separation of concerns</i> antara _model_, _view_, dan _controller_. Secara ringkas, konsep MVC berjalan dalam kerangka berikut:
    - **<i>Model</i>**: menyimpan data dan logika pada aplikasi.
    - **<i>View</i>**: merepresentasikan <i>user interface</i> dan bertanggung jawab dalam menampilkan data ke pengguna.
    - **<i>Controller</i>**: menangani input pengguna dan membantu proses <i>routing</i> untuk mengintegrasikan <i>model</i> ke <i>view</i> yang relevan.
- MVT merupakan singkatan dari <i>Model-View-Template</i>. MVT merupakan salah satu konsep arsitektur untuk pengembangan web yang sangat terkait dengan <i>framework</i> Django. Secara ringkas, konsep MVT berjalan dalam kerangka berikut:
    - **<i>Model</i>**: sama seperti MVC, digunakan untuk menyimpan data dan logika pada aplikasi.
    - **<i>View</i>**: mengatur tampilan dan mengambil data dari <i>model</i> untuk ditampilkan kepada pengguna.
    - **<i>Template</i>**: merancang <i>user interface</i> yang akan diisi oleh data dari <i>model</i> melalui <i>view</i>.
- MVVM merupakan singkatan dari <i>Model-View-ViewModel</i>. MVVM merupakan salah satu konsep arsitektur untuk pengembangan web yang memisahkan antara logika (<i>model</i>) dan tampilan (<i>view</i>). Secara ringkas, konsep MVVM berjalan dalam kerangka berikut:
    - **<i>Model</i>**: menyimpan data dan logika pada aplikasi.
    - **<i>View</i>**: merepresentasikan <i>user interface</i> dan menampilkan <i>output</i> data ke pengguna.
    - **<i>ViewModel</i>**: berada di antara <i>view</i> dan <i>model</i>, memberikan abstraksi <i>model</i> ke <i>view</i> yang dapat digunakan <i>view</i> untuk memengaruhi <i>model</i>.

Perbedaan dari ketiga konsep tersebut terletak pada <i>controller</i>. Pada **MVC**, <i>controller</i> berperan dalam menerima input pengguna dan memperbarui <i>model</i> dan mengintegrasikannya dengan <i>view</i>.<br>

Sedangkan pada **MVT**, peran <i>controller</i> telah ditangani oleh sistem <i>routing</i> internal Django sehingga tidak perlu membuat <i>controller</i> secara eksplisit. <i>View</i> pada MVT secara umum memiliki peran yang sama dengan <i>controller</i> pada MVC dalam menangani input pengguna dari <i>model</i>.<br>

Kemudian pada **MVVM**, responsibilitas ini dialihkan menjadi <i>ViewModel</i> yang bertanggung jawab sebagai mediator antara <i>view</i> dan <i>model</i>.<br>

Selain itu, **MVC** dan **MVT** seringkali melibatkan <i>server-side</i> pada aplikasi web, sedangkan **MVVM** lebih sering dikaitkan dengan aplikasi web yang bersifat <i>client-side</i>.