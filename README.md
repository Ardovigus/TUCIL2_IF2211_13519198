# TUCIL 2 IF2211: Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer)
Program ini dibuat untuk memenuhi tugas kecil kdedua dari mata kuliah IF2211 Strategi Algoritma Semester 2 tahun 2020/2021. Program berfungsi melakukan sorting dari sekumpulan elemen yang dapat direpresentasikan dalam Directed Acyclic Graph (DAG) dengan menggunakan algoritma <b>Topological Sort</b> sebagai salah satu bentuk penerapan <b>Decrease and Conquer</b>. 
<br><br>Secara sederhana, pertama, program akan membuka file berisi kumpulan node dan prerequisite-nya. Kemudian, program menelusuri seluruh elemen dan <b>mencari node yang tidak memiliki prerequisite</b>. Node tersebut <b>dihapus</b> dari elemen dan <b>dipindahkan</b> ke dalam list solusi. Dilanjutkan dengan tahap <b>penghapusan</b> pada <b>prerequisite</b> elemen lain yang mengandung node yang sudah dihapus sebelumnya. Sekuens langkah pencarian node dan penghapusan prerequisite ini dilakukan berulang kali hingga list tersebut kosong, sedangkan list solusi berisi seluruh node yang sudah tersusun.

## Program berjalan normal dengan spesifikasi:
* Windows 10 64-bit
* Python 3.9.1 64-bit

## Cara menggunakan:
Dikarenakan program tidak berhasil dikonversi ke dalam satu executable file, maka program perlu dijalankan dalam command prompt untuk memastikan berhasil bekerja.<br>
1. Akses folder src, pastikan terdapat topological_sort.py
2. Akses folder test, pastikan terdapat file uji, dengan format sampeX.txt (X adalah angka 0 - 7)
3. Buka command prompt, lalu ganti direktori ke dalam folder src tadi (dengan 'cd {direktori}')
4. Tuliskan perintah: py 13519198.py
5. Program akan berjalan dengan sendirinya, sampai seluruh file dalam folder test dibaca

## Tentang Pembuat
Program ini dibuat oleh Aurelius Marcel Candra (NIM 13519198) sebagai mahasiswa semester 4 IF ITB pada Januari 2021. Terima kasih atas perhatiannya.