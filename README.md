# Stress-Test-Portofolio
Yeaaaah, this is one step forward to become QE.

# Stress Test Portfolio - JMeter

## 📌 Overview
- Proyek ini mendemonstrasikan implementasi pengujian stres menggunakan Apache JMeter untuk menganalisis perilaku sistem di bawah kondisi beban ekstrem.

## 🛠 Tools Used
- Apache JMeter
- Java JDK
- CSV Data Config
- GitHub

## 🎯 Objectives
- Mengidentifikasi batasan sistem di bawah lalu lintas padat
- Mengukur waktu respons & throughput
- Mengamati titik kegagalan server
- Mengevaluasi stabilitas sistem
  
## Test Scenarios
  Ada 2 skenario pengujian:
- Total Permintaan: 1.000
- Target: API Swagger PetStore
- Tujuan: Mendorong sistem melampaui beban normal

===========================================
- Total Permintaan: 5.000
- Target: API Swagger PetStore
- Tujuan: Mendorong sistem melampaui beban normal

===========================================
Dari 2 skenario pengujian yang saya lakukan sebelumnya, saya masih belum puas karena sistem masih aman dan mencoba melakukan 1 skenario lagi hingga sistem mengalami crash.

- Total Permintaan: 23.000
- Target: API Swagger PetStore
- Tujuan: Mendorong sistem melampaui beban normal



## Result Summary
- ✔️ Sistem secara fungsional mampu menangani beban hingga tingkat sedang
- 📈 Penurunan kinerja menjadi signifikan dengan permintaan yang lebih tinggi
- ❌ Dalam skenario 23.000 permintaan, tingkat kesalahan mencapai **12%**
- ⏱️ Durasi respons maksimum mencapai **23 menit**
- 🛑 Skenario ini dianggap sebagai *kegagalan sebagian* — sistem tidak sepenuhnya stabil di bawah beban ekstrem

Pengamatan ini membantu memahami batasan kapasitas dan mempersiapkan optimasi kinerja.

## Conclusion
Pengujian beban dengan JMeter berhasil:

- Mengidentifikasi ambang batas di mana kinerja mulai menurun
- Mengumpulkan metrik berharga untuk perencanaan kinerja
- Memberikan wawasan tentang hambatan dan titik lemah sistem

Proyek ini adalah **demonstrasi praktis alur kerja pengujian beban** yang mungkin dilakukan oleh seorang QA atau insinyur kinerja untuk mengevaluasi keandalan dan skalabilitas sistem.
