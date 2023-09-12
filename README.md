# Tugas 2 PBP Ganjil 2023/2024
[Link to OrbitTune](https://orbitune.adaptable.app/main/)<br>

**Nama    : Bulan Athaillah Permata Wijaya**<br>
**NPM     : 2206032135**<br>
**Kelas   : PBP C**<br>

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
![Bagan request client Bulan](https://www.dropbox.com/scl/fi/56r2tlk37h5ytwefgejeg/Screenshot-2023-09-12-134404.png?rlkey=t5w5fiuti4elabn6p09shg86x&dl=0)<br>
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

#### Referensi
[Situs Web PBP Ganjil 2023/2024](https://pbp-fasilkom-ui.github.io/ganjil-2024/)<br>
[Django Web Framework](https://dev.to/ivanadokic/django-web-framework-python-ebn)<br>
[MVC, MVP, MVVM: Which One to Choose?](https://www.makeuseof.com/mvc-mvp-mvvm-which-choose/)<br>
[Django Testing Tutorial](https://learndjango.com/tutorials/django-testing-tutorial)