# Tugas 4 Proyek Django PBP

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

Nama: Fadhlan Hasyim

NPM: 2106652215

Kelas: PBP F

Kode Asdos: BYN

## Pendahuluan

Repositori ini digunakan sebagai wadah untuk mengumpulkan tugas Proyek Django PBP.

## Link Deployment

Aplikasi Heroku yang sudah di-_deploy_ dapat diakses melalui link berikut:
[https://pbp-django-assignments.herokuapp.com/](https://pbp-django-assignments.herokuapp.com/)

## Jawaban Pertanyaan

#### Apa kegunaan `{% csrf_token %}` pada elemen `<form>`? Apa yang terjadi apabila tidak ada potongan kode tersebut pada elemen `<form>`?

**Jawab:**

`{% csrf_token %}` adalah sebuah pertahanan yang disediakan oleh Django dalam menghadapi serangan _Cross Site Request Forgeries_. Singkatnya, jenis serangan CSRF terjadi ketika _attacker_ memaksa _user_ untuk melakukan tindakan yang tidak ingin mereka lakukan. `{% csrf_token %}` menghasilkan token di sisi server saat merender halaman dan memastikan untuk memeriksa ulang token ini untuk setiap permintaan yang masuk. Jika permintaan yang masuk tidak berisi token, permintaan tersebut tidak akan dieksekusi. Oleh karena itu, jika kita tidak menambahkan `{% csrf_token %}` pada elemen `<form>`, kita akan mendapatkan error yang mengatakan `CSRF verification failed. Request aborted` sehingga halaman HTML tidak dapat ditampilkan :( 

#### Apakah kita dapat membuat elemen `<form>` secara manual (tanpa menggunakan generator seperti {{ form.as_table }})? Jelaskan secara gambaran besar bagaimana cara membuat `<form>` secara manual.

**Jawab:**

Tentunya kita bisa membuat elemen `<form>` secara manual. Caranya cukup mudah, kita dapat membuat table dengan elemen `<table>`. Setelah itu, kita harus mengisi setiap baris dari table tersebut dengan field yang diinginkan. Untuk melakukannya, kita dapat memanfaatkan elemen `<tr>` dan `<td>`. Untuk mendapatkan input dari pengguna, kita dapat menggunakan elemen `<input>`. Hal yang sama juga dapat dilakukan untuk membuat tombol submit, kita hanya perlu menyesuaikan atribut `type=` yang ada pada elemen `<input>` tersebut menjadi `submit`.

#### Jelaskan proses alur data dari submisi yang dilakukan oleh pengguna melalui HTML form, penyimpanan data pada database, hingga munculnya data yang telah disimpan pada template HTML.
 
**Jawab:**

Pengguna akan mengisi formulir yang ditampilan pada halaman HTML. Ketika pengguna menekan tombol submit, HTPP Request (beserta data yang dimasukkan oleh pengguna) akan dikirimkan ke server. Dari HTPP Request yang didapatkan, server akan mengecek apakah requestnya valid atau tidak. Jika sudah valid, akan ditentukan views yang sesuai. Di tahap ini juga data yang diperoleh akan diolah sesuai kebutuhan, misalnya membuat objek baru dan menyimpannya ke database. Selanjutnya, views akan mengembalikan HTTP Response dan template HTML yang sesuai ke pengguna. Data yang telah diolah sebelumnya juga dapat ditampilkan di HTML tersebut sesuai kebutuhan.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

**Jawab:**

Pertama, saya membuat django app bernama todolist menggunakan perintah
`python manage.py startapp todolist` di dalam folder yang sudah diaktifkan virtualenv-nya dan sudah ter-install packages yang dibutuhkan.

Kedua, saya mendaftarkan aplikasi todolist ke dalam variable `INSTALLED_APPS` yang terdapat di `settings.py` pada folder `project_django`. Tidak lupa, saya juga mendaftarkan path todolist di `urls.py` yang berada di folder `project_django`.

Ketiga, saya membuat model Task yang memiliki lima buah atribut sebagai berikut:
```
...
class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=50)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
...
```
Di mana, user berelasi dengan model User yang sudah didefinisikan oleh Django. Pemilihan data type dari setiap atribut saya sesuaikan dengan kebutuhannya. Jangan lupa untuk menjalankan perintah makemigrations dan migrate untuk menerapkan skemanya pada database ^_^

Keempat, saya mengimplementasikan form registrasi, login, dan logout. Saya membuat masing-masing _function_-nya di `views.py`. Untuk registrasi, saya memanfaatkan `UserCreationForm` yang sudah disediakan oleh Django. Untuk login, saya memanfaatkan method `authenticate` dan `login`. Untuk logout, saya memanfaatkan method `logout`. Saya juga menerapkan cookie agar pengguna tidak perlu login berulang kali. Setelah itu, saya membuat halaman HTML untuk fitur registrasi dan login, di mana di dalamnya saya menggunakan generator {{ form.as_table }} dan menambahkan tombol submit. Tidak lupa, saya juga meristriksi akses ke halaman utama jika pengguna belum melakukan login.

Kelima, saya membuat halaman utama yang di dalamnya terdapat table todolist, tombol logout, dan tombol add task. Urutannya adalah membuat fungsi di `views.py` dan membuat template-nya (`todolist.html`).

Keenam, saya membuat halaman form untuk menambahkan task. Kali ini, saya membuat custom form bernama `TaskForm` yang merupakan subclass dari forms.Form. Form ini saya gunakan di fungsi `create_task` pada `views.py`. Di fungsi tersebut, data yang diperoleh dari user akan digunakan sebagai atribut untuk membuat objek baru yang nantinya akan disimpan di database. Terakhir, saya juga membuat halaman HTML-nya menggunakan `{{ form.as_table}}`.

Ketujuh, saya membuat routing dari setiap fungsi yang telah saya buat sebelumnya di `urls.py` yang sudah di buat di dalam folder todolist. Hasilnya seperti ini:
```
...
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('create-task/', create_task, name='create-task'),
    path('<id>/delete/', delete_task, name='delete-task'),
    path('<id>/update/', update_task, name='update-task'),
]
...
```

Kedelapan, cara untuk men-_deploy_-nya adalah dengan membuat aplikasi Django di heroku.com. Setelah itu, tambahkan HEROKU_API_KEY dan HEROKU_APP_NAME sebagai secrets di repository GitHub proyek Django. Selanjutnya, saya membuka tab GitHub Actions dan menjalankan kembali workflow yang gagal.

Kesembilan, saya membuat dua akun pengguna dan tiga dummy data. Akun dan passwordnya adalah sebagai berikut:
```
username_1: fadhlann
password_1: kP.FTVsA5ybhTb_

username_2: hasyimm
password_2: Vc#9mC5HyJzH!tR
```
Kesepuluh, untuk pengerjaan bonus, saya menerapkan CRUD pada django untuk mengambil data yang sudah ada dan meng-update nilainya, serta untuk menghapus datanya.

# Tugas 5 Proyek Django PBP

## Jawaban Pertanyaan

#### Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?

**Jawab:**

Internal CSS adalah kode CSS yang ditulis di dalam tag `<style>` dan kode HTML dituliskan di bagian atas (header) file HTML. Kelebihan internal CSS adalah perubahan pada internal CSS hanya berlaku pada satu halaman saja, jumlah file yang digunakan lebih sedikit karena HTML dan CSS berada dalam satu file yang sama. Kekurangan internal CSS adalah tidak efisien jika terdapat elemen yang menggunakan style yang sama, performa lebih lambat karena proses reload CSS yang berbeda-beda di setiap halaman.

Eksternal CSS adalah kode CSS yang ditulis terpisah dengan kode HTML. Eksternal CSS ditulis di sebuah file khusus yang berekstensi `.css`. File eksternal CSS biasanya diletakkan setelah bagian `<head>` pada halaman. Kelebihan eksternal CSS adalah membuat file HTML lebih rapi dan terstruktur, loading website lebih cepat, CSS yang sama dapat digunakan pada banyak elemen yang berbeda. Kekurangan eksternal CSS adalah halaman akan menjadi berantakan ketika file CSS gagal dipanggil oleh file HTML.

Inline CSS adalah kode CSS yang ditulis langsung pada atribut elemen HTML, tepatnya di atribut style. Kelebihan inline CSS adalah proses permintaan HTTP yang lebih kecil dan proses load website akan lebih cepat, membantu ketika hanya ingin menguji dan melihat perubahan pada satu elemen. Kekurangan inline CSS adalah tidak efisien karena Inline style CSS hanya bisa diterapkan pada satu elemen HTML.

#### Jelaskan tag HTML5 yang kamu ketahui.

**Jawab:**

`<a>`: untuk mendefinisikan sebuah hyperlink.
`<body>`: untuk mendefinisikan bagian "body" dari HTML.
`<br>`: untuk memberikan _single line break_.
`<button>`: untuk membuat sebuah tombol.
`<div>`: untuk memberikan bagian dari dokumen.
`<form>`: untuk mendefinisikan HTML form.
`<head>`: untuk mendefinisikan bagian "head" dari HTML.
`<h1>`-`<h6>`: untuk mendefinisikan heading pada HTML.
`<html>`: untuk mendefinisikan root dari HTML
`<img>`: untuk menampilkan gambar.
`<input>`: untuk mendefinisikan input control. 
`<label>`: untuk memberikan label. 
`<li>`: untuk mendefinisikan list. 
`<p>`: untuk mendefinisikan paragraf. 
`<script>`: untuk mendefinisikan script bagi client-side processing.
`<span>`: untuk mendefiniskan bagian inline styleless.  
`<style>`: untuk memasukkan informasi style pada HTML.
`<table>`: untuk mendefinisikan sebuah tabel. 
`<td>`: untuk mendefinisikan sebuah sel pada tabel. 
`<th>`: untuk mendefinisikan sebuah header pada tabel. 
`<title>`: untuk mendefinisikan judul dokumen.

#### Jelaskan tipe-tipe CSS selector yang kamu ketahui.

**Jawab:**

Element selector: menggunakan tag HTML sebagai selector untuk memberikan style pada elemen tersebut.
ID selector: menambahkan ID pada elemen HTML dan menggunakan ID tersebut pada file CSS sebagai selector.
Class Selector: menambahkan atribut class pada elemen HTML dan menggunakan nama class tersebut sebagai selector pada file CSS.

#### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

**Jawab:**

Pertama, saya mencari inspirasi desain website yang elegan, mencari color palette yang sesuai, dan mempelajari bagaimana dasar-dasar Tailwind CSS.

Kedua, saya menambahkan baris ini `<script src="https://cdn.tailwindcss.com"></script>` pada bagian `<head>` di base.html. 

Ketiga, saya mengimplementasikan style pada setiap elemen HTML. Saya menambahkan style-style tersebut pada atribut class elemen HTML. Bagian ini memakan waktu paling lama, tetapi sangat mengasyikkan!

Keempat, saya menerapkan prinsip responsive design pada halaman web.

Kelima, saya melakukan cross-check dan melakukan push serta commit ke Github. Selesai! :D