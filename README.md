# Tugas 3 PBP Ganjil 2023/2024

**Nama    : Bulan Athaillah Permata Wijaya**<br>
**NPM     : 2206032135**<br>
**Kelas   : PBP C**<br>

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

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_
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

#### Referensi
[Situs Web PBP Ganjil 2023/2024](https://pbp-fasilkom-ui.github.io/ganjil-2024/)<br>
[Working with forms - Django](https://docs.djangoproject.com/en/4.2/topics/forms/)
