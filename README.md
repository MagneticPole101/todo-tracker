http://khair-juzaili-todotracker.pbp.cs.ui.ac.id/

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step

Buat proyek Django bernama <nama proyek> dengan perintah berikut.

```
django-admin startproject <nama proyek> .
```

Jalankan perintah berikut untuk membuat aplikasi baru.

```
python manage.py startapp <nama app>
```

---
Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

urls.py meneruskan request dari user ke view yang sesuai, views.py memasukkan data yang sudah dibaca dari model ke template (berkas html), models.py berurusan terkait read/write data, dan berkas html menyediakan template html web tersebut.

---
Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Agar bisa mengisolasi package dan dependencies aplikasi agar tidak bertabrakan dengan versi lain. Kita tetap bisa membuat aplikasi web berbasis Django tanpa menggunakan virtual environment akan tetapi ada kemungkinan muncul masalah karena bertabrakannya package dan dependencies aplikasi dari versi yang berbeda.

---
Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya?

MVT (Model-View-Template) 
Model: Menyimpan data dan logika aplikasi.
View: Menampilkan data dari model dan menghubungkannya dengan template.
Template: Menentukan tampilan antarmuka pengguna.

MVC (Model-View-Controller) dan MVVM (Model-View-ViewModel) adalah dua arsitektur desain perangkat lunak populer yang digunakan dalam pengembangan aplikasi. Kedua arsitektur memiliki perbedaan antara controller dan view model sebagai berikut:

Model-View-Controller (MVC): Dalam arsitektur MVC, controller bertanggung jawab untuk menerima input dari pengguna dan mengubah model sesuai dengan input tersebut. Controller juga berfungsi untuk mengirimkan respons ke view. View model tidak ada dalam arsitektur ini. Model mewakili data dan logika bisnis aplikasi.

Model-View-ViewModel (MVVM): Dalam arsitektur MVVM, view model berfungsi sebagai perantara antara model dan view. View model menyediakan data dan operasi yang dibutuhkan oleh view. Dalam arsitektur MVVM, controller tidak digunakan. View model mengendalikan aliran data antara model dan view, serta mengelola keadaan view. View, di sisi lain, hanya bertanggung jawab untuk menampilkan data.

Dalam kesimpulannya, perbedaan antara controller dan view model pada arsitektur MVC dan MVVM terletak pada fungsinya. Controller pada arsitektur MVC berperan untuk mengendalikan aliran data antara model dan view, sementara view model pada arsitektur MVVM berperan sebagai perantara antara model dan view.

