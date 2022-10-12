# Tugas 6 Proyek Django PBP

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

#### Jelaskan perbedaan antara _asynchronous programming_ dengan _synchronous programming_.

**Jawab:**

_Asynchronous programming_ berarti program dapat dijalankan secara paralel. Artinya, kita tidak perlu menunggu satu program sampai selesai dijalankan untuk menjalankan program lainnya. Di sisi lain, _synchronous programming_ berarti program harus dijalankan secara berurutan, suatu program akan dijalankan ketika program yang sebelumnya sudah selesai dijalankan.
 

#### Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.

**Jawab:**

Event-Driven Programming adalah paradigma pemrograman di mana program akan dijalankan berdasarkan event yang terjadi. Contoh event adalah tombol yang diklik atau kursor mouse yang bergerak. Ketika suatu event terjadi, maka program atau function akan dijalankan.

Pada tugas ini, contoh penerapan event-driven programming adalah ketika menggunakan AJAX POST dan AJAX DELETE. Saat user menekan tombol "Add Task" atau icon "trash", maka akan dijalankan function yang sesuai (post data atau delete data).

#### Jelaskan penerapan asynchronous programming pada AJAX.
 
**Jawab:**

Penggunaan AJAX memungkinkan suatu halaman web untuk di-update tanpa melakukan reload terlebih dahulu. Ketika request dikirimkan oleh client, AJAX akan menerimanya dan meneruskannya ke server. Di saat yang bersamaan, pengguna tetap bisa berinteraksi dengan halaman web yang ada. Ketika response sudah dikembalikan oleh server, AJAX akan segera menerimanya dan menjalankan callback function yang sesuai.

### Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.

**Jawab:**

Pertama, untuk AJAX GET, saya menggunakan endpoint `/todolist/json` yang berisi data todolist sebagai tujuan request method GET yang saya buat. Pada `todolist.html`, saya membuat fungsi yang akan melakukan request ke endpoint `/todolist/json` dan data yang diperoleh akan diiterasi menjadi elemen html yang akan ditambahkan di halaman web. Fungsi tersebut harus selalu di-load setiap kali pengguna mengakses halaman html tersebut.

Kedua, untuk AJAX POST, saya membuat views yang akan membuatkan objek Task dan mengembalikan JsonResponse sebagai nilai kembaliannya. Nantinya, json tersebut akan diterima oleh template HTML yang sesuai, yakni todolist.html. Setelah itu, saya juga menambahkan path yang mengarahkan kepada views tersebut di `urls.py`. Untuk setiap kembalian dari views akan diproses di dalam todolist.html menjadi card yang akan ditampilkan di halaman web. Selain itu, saya juga membuat modal untuk menambahkan task dengan menggunakan bootstrap.
