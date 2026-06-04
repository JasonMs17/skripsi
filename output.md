**RANCANG BANGUN APLIKASI** ***MOBILE*** **DENGAN VISUALISASI DAN ANALISIS SINYAL ELEKTROENSEFALOGRAM UNTUK MONITORING TERAPI** ***VIRTUAL REALITY DENTAL HYPNOSIS*** **MENGGUNAKAN METODE**

**LAPORAN SKRIPSI**

diajukan untuk menempuh ujian sarjana

pada Fakultas Matematika dan Ilmu Pengetahuan Alam
Universitas Padjadjaran

JASON NATANAEL KRISYANTO

NPM 140810220051

<!-- image -->

UNIVERSITAS PADJADJARAN
FAKULTAS MATEMATIKA DAN ILMU PENGETAHUAN ALAM
PROGRAM STUDI TEKNIK INFORMATIKA
SUMEDANG
2026

## 

## 

## DAFTAR ISI

## 

## 

## BAB I

## PENDAHULUAN

Pada bab ini akan dibahas gambaran umum mengenai penelitian yang dilakukan. Pembahasan meliputi latar belakang permasalahan, perumusan dan batasan masalah, tujuan penelitian, serta manfaat yang diharapkan dari penelitian ini. Selain itu, pada bab ini juga disajikan sistematika penulisan sebagai gambaran alur pembahasan pada bab-bab selanjutnya.

- 1.1 **Latar Belakang**

Kecemasan dental ( *dental anxiety* ) merupakan permasalahan yang umum terjadi dalam praktik kedokteran gigi dan dapat muncul sebelum maupun selama tindakan perawatan. Kondisi ini tidak hanya menimbulkan ketidaknyamanan psikologis bagi pasien, tetapi juga memicu respons fisiologis berupa aktivasi sistem saraf simpatis dan *hypothalamic–pituitary–adrenal axis* (HPA axis), yang menyebabkan peningkatan hormon stres seperti kortisol. Peningkatan kecemasan dental diketahui berkontribusi terhadap penghindaran perawatan gigi, memburuknya kondisi kesehatan mulut, serta penurunan kualitas hidup pasien (Yubiliana, Raksanagara, et al., 2021).

Penanganan kecemasan dental secara konvensional umumnya dilakukan melalui pendekatan farmakologis, seperti *inhalation conscious sedation* , namun efeknya bersifat sementara. Oleh karena itu, berkembang pendekatan non-farmakologis berbasis *behavioral medicine* , salah satunya *dental hypnosis* . Penelitian Yubiliana dkk. (2021) menunjukkan bahwa *dental hypnosis* efektif menurunkan kadar kortisol saliva dan berkorelasi dengan peningkatan kualitas hidup pasien.

Seiring perkembangan teknologi, *dental hypnosis* dikombinasikan dengan *Virtual Reality* (VR) untuk meningkatkan efektivitas terapi melalui lingkungan imersif. Integrasi ini dikenal sebagai *Virtual Reality Dental Hypnosis* (VRDH). Kondisi relaksasi dan hipnosis dalam terapi VRDH dapat diidentifikasi secara objektif melalui aktivitas gelombang otak pada rentang frekuensi theta dan alpha (4–12 Hz) menggunakan Elektroensefalogram (Yubiliana et al., 2025).

Penelitian sebelumnya di bidang fisika telah berhasil mengembangkan perangkat EEG portabel yang dapat merekam aktivitas gelombang otak, mengolah sinyal secara analog dan digital, menentukan frekuensi dominan, serta mengirimkan data ke perangkat *mobile* melalui koneksi Bluetooth (Ghani &amp; Abdurrochman, 2024). Sebagai pendukung perangkat keras tersebut, telah dikembangkan juga aplikasi *mobile* sederhana yang berfungsi untuk menampilkan nilai frekuensi dominan dan status kondisi hipnosis.

Meskipun aplikasi *mobile* tersebut telah mampu menjalankan fungsi dasar sebagai penerima dan penampil data EEG, fitur yang tersedia masih sangat terbatas. Aplikasi belum mendukung pengelolaan dan penyimpanan data EEG, serta belum dirancang secara optimal untuk mendukung kebutuhan klinis maupun analisis lanjutan. Akibatnya, pemanfaatan data EEG yang dihasilkan oleh perangkat belum dapat digunakan secara maksimal untuk evaluasi terapi, pemantauan perkembangan pasien, maupun dokumentasi medis.

Berdasarkan permasalahan tersebut, diperlukan pengembangan aplikasi *mobile* yang lebih komprehensif untuk mendukung sistem VRDH. Pengembangan ini tidak hanya berfokus pada penambahan fitur, tetapi juga pada perancangan aplikasi yang mampu menyajikan visualisasi EEG, mendukung penyimpanan dan pengelolaan data, serta meningkatkan keterpaduan antara perangkat EEG, dokter, perawat, dan pasien. Dengan adanya pengembangan aplikasi *mobile* ini, diharapkan sistem VRDH dapat digunakan secara lebih efektif, informatif, dan berkelanjutan dalam mendukung terapi kedokteran gigi berbasis teknologi.

- 1.1 **Identifikasi Masalah**

Berdasarkan latar belakang yang telah diuraikan, maka identifikasi masalah dalam penelitian dan pengembangan aplikasi mobile EEG ini adalah sebagai berikut:

1. Fitur-fitur apa saja yang diperlukan dalam pengembangan aplikasi mobile untuk mendukung sistem VRDH berbasis data EEG?
2. Bagaimana

- 1.2 **Batasan Masalah**

Untuk menjaga fokus dan ruang lingkup pengembangan sistem, maka batasan masalah dalam penelitian ini adalah sebagai berikut:

1. Aplikasi yang dikembangkan hanya ditujukan untuk sistem operasi Android dan tidak mencakup pengembangan pada sistem operasi iOS maupun platform lainnya.
2. Data EEG yang diterima aplikasi dibatasi pada hasil pengolahan yang dikirim oleh perangkat, seperti nilai frekuensi dominan, status kondisi hipnosis, dan data sinyal untuk keperluan visualisasi.
3. Aplikasi dikembangkan dan diuji menggunakan data uji dan skenario terbatas, sehingga hasil analisis yang ditampilkan belum ditujukan untuk penggunaan klinis skala besar.

- 1.3 **Maksud dan Tujuan Penelitian**

Maksud dari kegiatan penelitian ini adalah untuk merancang dan mengembangkan aplikasi *mobile* pendukung sistem VRDH berbasis data EEG yang terintegrasi, guna memfasilitasi pengelolaan, pemantauan, dan pertukaran informasi terapi antara pasien, perawat, dan dokter.

Tujuan yang ingin dicapai oleh penulis dari kegiatan penelitian ini adalah:

1. Mengidentifikasi dan menganalisis fitur-fitur yang diperlukan dalam pengembangan aplikasi *mobile* untuk mendukung sistem VRDH berbasis data EEG.
2. Merancang dan mengembangkan sistem aplikasi mobile yang memungkinkan integrasi antara pasien, perawat, dan dokter dalam proses terapi VRDH berbasis EEG.

- 1.4 **Manfaat Penelitian**

Adapun manfaat yang dapat diperoleh melalui pengembangan aplikasi *mobile* EEG ini adalah:

1. Bagi pengguna: membantu pengguna dalam memantau aktivitas gelombang otak melalui perangkat *mobile* , serta memberikan informasi sederhana mengenai kondisi aktivitas otak, seperti
2. Bagi peneliti atau tenaga akademik: menjadi media pendukung penelitian, khususnya dalam pengumpulan, penyimpanan, dan analisis data EEG secara terstruktur, sehingga memudahkan proses evaluasi dan pengolahan data lanjutan.
3. Bagi pengembang: memberikan pengalaman dan pemahaman dalam pengembangan aplikasi *mobil* , integrasi perangkat keras EEG dengan aplikasi, serta perancangan sistem yang berpotensi dikembangkan lebih lanjut ke arah aplikasi bernilai komersial.

- 1.5 **Metodologi Penelitian**

Penelitian ini menggunakan metode sebagai pendekatan dalam pengembangan aplikasi mobile pendukung sistem VRDH. Metode dipilih karena bersifat iteratif dan fleksibel, sehingga memungkinkan proses pengembangan aplikasi dilakukan secara bertahap dan dapat disesuaikan dengan kebutuhan pengguna serta hasil evaluasi pada setiap tahap pengembangan.

Proses penelitian diawali dengan analisis kebutuhan sistem dan identifikasi kebutuhan klinis terapi VRDH. Selanjutnya dilakukan perancangan awal aplikasi *mobile* yang mencakup alur sistem, antarmuka                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       pengguna, serta integrasi dengan perangkat EEG portabel. Tahap berikutnya adalah pengembangan aplikasi secara bertahap melalui beberapa iterasi dan evaluasi.

Hasil evaluasi pada setiap iterasi digunakan sebagai dasar perbaikan dan penyempurnaan aplikasi pada tahap pengembangan berikutnya hingga diperoleh aplikasi *mobile* yang mampu mendukung visualisasi, penyimpanan, dan pengelolaan data EEG secara optimal untuk kebutuhan terapi VRDH.

## BAB II

**TINJAUAN PUSTAKA**

Bab ini berisi uraian teori, konsep, dan penelitian terdahulu yang menjadi dasar serta acuan dalam pelaksanaan penelitian. Tinjauan pustaka disajikan untuk memberikan landasan ilmiah yang memperkuat argumen sekaligus membantu dalam merumuskan solusi yang dikembangkan.

- 2.12 **Elektroensefalogram**

Elektroensefalogram (EEG) adalah aktivitas listrik otak yang diperoleh melalui elektroda yang ditempatkan pada kulit kepala.  aktivitas neurondi korteks serebral, khususnya potensial postsinaptik dari sel piramidal(Niedermeyer &amp; Lopes da Silva, 2005). EEG menjadi salah satu teknik utama dalam neurofisiologi klinis karena mampu memberikan informasi temporal yang sangat baik mengenai dinamika aktivitas otak (Teplan, 2002).

Secara metode, EEG dibedakan menjadi teknik  dan . EEG non-invasif dilakukan dengan menempatkan elektroda pada permukaan kulit kepala menggunakan sistem penempatan standar internasional 10–20 dan tidak memerlukan prosedur pembedahan (Niedermeyer &amp; Lopes da Silva, 2005).

(Zouridakis, 200)

<!-- image -->

Dalam praktik klinis, EEG berfungsi sebagai alat diagnostik utama pada epilepsi dengan mendeteksi pola aktivitas epileptiform seperti *spike* dan *sharp waves* (Niedermeyer &amp; Lopes da Silva, 2005). Selain itu, EEG juga digunakan untuk evaluasi gangguan kesadaran, studi tidur, monitoring aktivitas otak di ruang intensif, serta penelitian kognitif dan neuropsikologis (Teplan, 2002). Dengan kemampuannya merekam aktivitas otak secara langsung dan *real-time* , EEG menjadi metode yang penting dalam bidang neurologi dan ilmu saraf modern.

Secara umum, gelombang otak manusia diklasifikasikan ke dalam lima jenis, yaitu gelombang alfa, beta, teta, gamma, dan deltaenjelasan lebih rinci mengenai karakteristik masing-masing gelombang dapat dilihat pada Tabel 2.1.

Tabel 2.1 Klasifikasi Gelombang Otak (Abhang et al., 2016; St. Louis et al., 2016)

| **Tipe Gelombang**   | **Rentang Frekuensi**   | **Kondisi Otak**                                                      |                |
|----------------------|-------------------------|-----------------------------------------------------------------------|----------------|
| Delta                | 0.5 – 4 Hz              | Dominan pada tidur nyenyak (  *deep sleep*  ) dan kondisi tidak sadar | <!-- image --> |
| Theta                | 4 – 7 Hz                | Berkaitan dengan kantuk, relaksasi mendalam, dan tahap awal tidur     | <!-- image --> |
| Alpha                | 8 – 13 Hz               | Muncul saat kondisi rileks, sadar, mata terpejam namun tidak tidur    | <!-- image --> |
| Beta                 | 13 – 30 Hz              | Berkaitan dengan aktivitas mental aktif, konsentrasi, dan kewaspadaan | <!-- image --> |
| Gamma                | >30 Hz                  | Berhubungan dengan proses kognitif tingkat tinggi dan perhatian       | <!-- image --> |

(De Matos et al., 2024)(Levenson, 2018)

(Yubiliana, Putra, et al., 2021)(Yubiliana et al., 2025)

- 2.12 (Yubiliana, Putra, et al., 2021)

React Native merupakan *framework open-source* untuk pengembangan aplikasi *mobile* lintas platform yang dikembangkan oleh Meta Platforms dan dirilis pada tahun 2015. Framework ini menggunakan JavaScript . Konsep *single codebase* memungkinkan sebagian besar kode digunakan kembali pada dua *platform* berbeda sehingga meningkatkan efisiensi waktu dan biaya pengembangan. Arsitektur React Native menggunakan mekanisme *bridge* untuk menghubungkan kode JavaScript dengan modul native, sehingga aplikasi tetap dapat mengakses fitur perangkat secara langsung(Eisenman, 2017)

Dalam konteks akademik, React Native banyak sebagai solusi pengembangan aplikasi yang efisien. Analisis komparatif menunjukkan bahwa React Native memiliki keunggulan dalam produktivitas dan percepatan waktu rilis dibandingkan pengembangan *native* , meskipun terdapat sedikit penurunan performa pada aplikasi dengan kebutuhan komputasi tinggi (Ramachandrappa, 2024). Selain itu, aspek *maintainability* dalam proyek berskala besar menjadi perhatian karena struktur kode berbasis komponen dan integrasi modul *native* dapat meningkatkan kompleksitas pemeliharaan (Aditya &amp; Susanty, 2022). Temuan tersebut menunjukkan bahwa React Native sesuai untuk pengembangan aplikasi yang memprioritaskan efisiensi pengembangan.

(Shrivastava et al., 2021)

(Anwer &amp; Aftab, 2017)

(Lucassen et al., 2016)(Sharp &amp; Hall, 2016)

(Yudhistira et al., 2021)(Beck, 2004)
(Rahmi et al., 2016; Sharp &amp; Hall, 2016)

(Anwer &amp; Aftab, 2017; Rahmi et al., 2016)

- 2.12 Unified Modeling Language

*Unified Modeling Language* (UML) adalah bahasa grafis yang digunakan untuk memvisualisasikan, menentukan, membangun, dan mendokumentasikan komponen-komponen dalam sistem perangkat lunak. UML mencakup sembilan jenis diagram, seperti *class* diagram, *object diagram* , *use case diagram* , *sequence diagram, collaboration diagram* , *statechart diagram* , *activity diagram* , *component diagram* , dan *deployment diagram* (Booch et al., 2005).

- 1.6.1 ***Use Case Diagram***

*Use case diagram* adalah salah satu jenis diagram yang digunakan untuk menggambarkan interaksi antara pengguna dengan sistem. Diagram ini menampilkan berbagai skenario  dengan sistem yang dikembangkan, serta tujuan yang ingin dicapai melalui interaksi tersebut *. Use case diagram* memberikan gambaran tingkat tinggi mengenai fungsi-fungsi utama sistem dan batasan-batasannya tanpa mendetailkan urutan langkah-langkah proses. Dengan menggunakan simbol seperti oval untuk *use case* , gambar orang untuk aktor, dan garis penghubung antar elemen, diagram ini membantu tim memahami konteks dan kebutuhan fungsional dari sistem secara jelas dan terstruktur (Booch et al., 2005).

*Use case diagram* memiliki beberapa simbol utama yang digunakan untuk merepresentasikan interaksi antara aktor dan sistem. Pada Tabel 2.1 ditampilkan simbol-simbol beserta keterangannya yang umum digunakan dalam penyusunan diagram ini.

Tabel 2.1 Simbol *Use Case Diagram* *(Hendini, 2016)*

|   **No** | **Simbol**                       | **Keterangan**                                                                                                                                                                                                                                                                               |
|----------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        1 | *Use Case*  <!-- image -->       | Deskripsi fungsi sistem yang menggambarkan interaksi antar komponen atau aktor, yang saling bertukar pesan dalam satu kesatuan proses.                                                                                                                                                       |
|        2 | *Actor*  <!-- image -->          | Individu atau sistem eksternal yang melakukan interaksi langsung dengan sistem yang sedang dikembangkan. Biasanya dituliskan dalam bentuk kata benda atau nama peran.                                                                                                                        |
|        3 | *Association*  <!-- image -->    | Hubungan komunikasi yang terjadi antara aktor dengan suatu  *use case*  , yang menggambarkan partisipasi aktor dalam skenario sistem.                                                                                                                                                        |
|        4 | *Extend*  <!-- image -->         | Sebuah hubungan yang menunjukkan bahwa ada  *use case*  tambahan yang memperluas fungsionalitas  *use case*  utama.  *Use case*  tambahan ini tetap dapat beroperasi secara mandiri tanpa tergantung pada  *use case*  utama. Panah pada relasi ini mengarah ke  *use case*  yang diperluas. |
|        5 | *Generalization*  <!-- image --> | Hubungan hirarki antara dua  *use case*  , di mana satu  *use case*  mewakili fungsi umum dan yang lainnya merupakan bentuk khususnya. Konsep ini mencerminkan hubungan umum-khusus.                                                                                                         |
|        6 | *Include*  <!-- image -->        | Hubungan antara  *use case*  utama dengan  *use case*  tambahan yang harus dijalankan sebagai bagian dari proses.  *Use case*  utama tidak dapat berfungsi tanpa menyertakan  *use case*  tambahan ini. Arah panah menunjuk pada  *use case*  yang wajib disertakan.                         |

- 1.6.1 ***Activity Diagram***

*Activity diagram* adalah salah satu jenis diagram dalam UML yang termasuk dalam kategori *behavior* diagram. Diagram ini digunakan untuk menggambarkan alur aktivitas atau proses dalam suatu sistem, baik yang dilakukan oleh pengguna maupun oleh sistem itu sendiri. *Activity diagram* sangat berguna untuk memvisualisasikan logika suatu proses, memahami alur kerja, serta menjelaskan langkah-langkah dalam suatu *use case* . Dengan menggunakan simbol-simbol khusus seperti *start node, action, decision node,* dan *end node* , diagram ini membantu tim bisnis dan pengembang untuk memiliki pemahaman yang sama mengenai perilaku sistem yang sedang dirancang (Booch et al., 2005).

*Activity diagram* menggunakan sejumlah simbol standar untuk merepresentasikan alur proses dan kondisi yang terjadi dalam sistem. Pada Tabel 2.2 ditunjukkan simbol-simbol utama beserta penjelasannya yang umum digunakan dalam penyusunan *activity diagram* .

Tabel 2.2 Simbol *Activity Diagram* (Pedamkar, 2019)

|   **No** | **Simbol**                      | **Keterangan**                                                                                                                                                                                                                                                                              |
|----------|---------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        1 | *Initial State*  <!-- image --> | Titik awal dari sebuah  *activity diagram*  atau  *state machine*  yang menunjukkan di mana aliran kontrol dimulai secara  *default*  .                                                                                                                                                     |
|        2 | *Action State*  <!-- image -->  | Merepresentasikan eksekusi sebuah komputasi tunggal dan atomik dalam diagram. Ini adalah tindakan yang tidak dapat diinterupsi oleh  *event*  lain. Ketika sebuah  *action state*  selesai, aliran kontrol akan langsung berpindah ke  *state*  berikutnya.                                 |
|        3 | *Control Flow*  <!-- image -->  | Menggambarkan jalur berarah yang menunjukkan bagaimana aliran kontrol berpindah dari satu  *action*  atau  *activity state*  ke  *state*  berikutnya dalam diagram.                                                                                                                         |
|        4 | *Decision Node*  <!-- image --> | Berfungsi sebagai titik percabangan dalam aliran kontrol, di mana jalur alternatif dipilih berdasarkan evaluasi ekspresi  *Boolean*  .                                                                                                                                                      |
|        5 | *Fork*  <!-- image -->          | Digunakan untuk memecah satu aliran kontrol menjadi dua atau lebih aliran paralel yang berjalan secara bersamaan. Setelah sebuah  *fork*  , aktivitas di setiap jalur baru akan berlanjut secara independen, memungkinkan konkurensi dalam sistem.                                          |
|        6 | *Join*  <!-- image -->          | Berfungsi untuk menyinkronkan dua atau lebih aliran kontrol paralel menjadi satu aliran tunggal. Pada titik  *join*  , semua aliran masuk harus mencapai node ini sebelum aliran kontrol dapat melanjutkan ke  *state*  berikutnya, memastikan bahwa semua aktivitas paralel telah selesai. |
|        7 | *Final State*  <!-- image -->   | Menunjukkan penghentian atau penyelesaian aliran kontrol dalam sebuah  *activity diagram*  atau  *state machine.*  Setelah mencapai  *state*  ini, eksekusi proses yang diwakilinya dianggap telah berakhir.                                                                                |

    - 2.12 ***Entity-Relationship Diagram***

*Entity-Relationship Diagram* (ERD) adalah sebuah teknik pemodelan visual yang diusulkan sebagai alat penting dalam desain basis data dan analisis sistem. ERD memungkinkan visualisasi struktur data melalui penggambaran entitas serta hubungan antar entitas dalam sebuah sistem.

Dalam hal ini, entitas didefinisikan sebagai sesuatu yang dapat dikenali secara unik, seperti individu, objek, atau peristiwa. Entitas dikelompokkan ke dalam himpunan entitas, yaitu kumpulan entitas yang memiliki atribut atau karakteristik yang sama. Informasi tentang entitas maupun hubungan antar entitas diperoleh melalui pengamatan atau pengukuran, dan diekspresikan dalam bentuk pasangan atribut-nilai.

Setiap atribut dapat didefinisikan sebagai fungsi yang memetakan dari himpunan entitas atau himpunan hubungan ke dalam himpunan nilai (atau produk Cartesian dari beberapa himpunan nilai). Sementara itu, hubungan ( *relationship* ) menggambarkan asosiasi di antara dua atau lebih entitas, dan himpunan hubungan merupakan representasi matematis dari asosiasi tersebut. Dengan demikian, model ini memungkinkan struktur data direpresentasikan secara sesuai kebutuhan sistem.

ERD juga memuat informasi mengenai kardinalitas, seperti pemetaan satu-ke-satu, satu-ke-banyak, atau banyak-ke-banyak, yang menunjukkan batasan jumlah entitas yang terlibat dalam suatu hubungan. Selain itu, peran masing-masing entitas dalam hubungan juga dapat dinyatakan secara eksplisit dalam diagram. Dengan memisahkan informasi tentang entitas dan hubungan, ERD membantu dalam memahami struktur semantik data serta mengidentifikasi ketergantungan fungsional yang mungkin terjadi (Chen, 1976).

Pada Tabel 2.3 ditampilkan simbol-simbol utama yang digunakan dalam ERD Simbol-simbol ini berfungsi untuk merepresentasikan berbagai komponen penting, mulai dari entitas, atribut, hingga hubungan antar entitas dalam sebuah sistem. Dengan adanya standar simbol ini, pemodelan ERD menjadi lebih mudah dipahami dan konsisten, baik oleh perancang sistem maupun pihak lain yang membacanya. Penjelasan dalam tabel memberikan gambaran ringkas mengenai arti setiap simbol dan peranannya dalam memvisualisasikan struktur data.

Tabel 2.3 Simbol *Entity Relationship Diagram* (Elmasri &amp; Navathe, 2016)

|   **No** | **Simbol**                              | **Keterangan**                                                                                                                                                     |
|----------|-----------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|        1 | *Entity*  <!-- image -->                | Sesuatu yang bisa dibedakan dan dikenali, seperti orang, perusahaan, atau acara tertentu. Dalam diagram, digambarkan sebagai kotak persegi panjang.                |
|        2 | *Weak Entity*  <!-- image -->           | Entitas yang tidak bisa dikenali secara unik tanpa bantuan entitas lain. Digambarkan dengan kotak persegi ganda.                                                   |
|        3 | <!-- image -->  Attribute               | Informasi atau ciri khas dari entitas atau hubungan. Biasanya ditampilkan sebagai oval yang terhubung ke entitas.                                                  |
|        4 | *Key attribute*  <!-- image -->         | Atribut yang digunakan untuk membedakan entitas secara unik. Biasanya disebut sebagai  *primary key*  (kunci utama).                                               |
|        5 | *Multivalued attribute*  <!-- image --> | Atribut multinilai adalah atribut yang dapat menyimpan lebih dari satu nilai untuk satu entitas. Contohnya seorang pegawai bisa memiliki lebih dari satu keahlian. |
|        6 | <!-- image -->  Derived attribute       | Atribut yang nilainya bisa dihitung dari atribut lain, seperti umur dari tanggal lahir.                                                                            |
|        7 | *Relationship*  <!-- image -->          | Menggambarkan kaitan antar entitas, seperti “mengajar” antara dosen dan mata kuliah. Digambarkan dengan belah ketupat.                                             |

- 2.12 **Skema Relasional**

Skema relasional merupakan representasi struktur basis data yang menggambarkan tabel, atribut, serta hubungan antar tabel yang digunakan dalam sistem basis data relasional. Skema relasional umumnya menampilkan atribut, *Primary Key* (PK), dan *Foreign Key* (FK) yang berfungsi untuk menghubungkan data antar tabel. Bentuk visual ini sering digunakan pada tahap perancangan basis data karena lebih dekat dengan implementasi yang akan diterapkan pada *Database Management System* (Coronel &amp; Morris, 2019).

Konsep skema relasional berasal *dari Relational Model* yang diperkenalkan oleh Codd pada tahun 1970. Menurut Codd (1970), data direpresentasikan dalam bentuk relasi yang diwujudkan sebagai tabel yang terdiri atas baris dan kolom Model relasional dikembangkan untuk menciptakan independensi data sehingga pengguna tidak perlu memahami bagaimana data disimpan secara fisik di dalam sistem komputer. Dalam proses perancangan basis data, model relasional kemudian divisualisasikan ke dalam bentuk skema relasional untuk memudahkan pengembang memahami struktur data yang akan dibangun.

Selain digunakan sebagai dokumentasi perancangan, skema relasional juga berperan dalam menjaga integritas data. Hubungan antar tabel yang dibentuk melalui *Foreign Key* membantu mengurangi redundansi data dan mencegah terjadinya anomali pada proses penyisipan, pembaruan, maupun penghapusan data (Lemahieu et al., 2018). Oleh karena itu, penyusunan skema relasional yang baik menjadi salah satu faktor penting dalam pengembangan sistem informasi.

## BAB III ANALISIS DAN PERANCANGAN 
Bab ini membahas tahapan analisis dan perancangan aplikasi mobile yang dikembangkan untuk mendukung analisis aktivitas gelombang otak dalam terapi Virtual Reality Dental Hypnosis (VRDH). Analisis dilakukan untuk mengidentifikasi kebutuhan pengguna, kebutuhan data, serta kebutuhan sistem secara keseluruhan, sedangkan perancangan difokuskan pada penyusunan solusi aplikasi yang sesuai dengan kebutuhan tersebut. Tahapan ini bertujuan agar aplikasi yang dikembangkan dapat berjalan secara terarah, efektif, dan sesuai dengan tujuan pengembangan sistem.
3.1	Tahap Perencanaan
Tahap perencanaan dilakukan melalui proses eksplorasi kebutuhan sistem dengan melakukan diskusi dengan pihak terkait untuk memahami kebutuhan pengguna serta proses bisnis yang berjalan. Kegiatan diskusi pertama dilaksanakan pada tanggal 18 Januari 2026 bersama Dr. Andri Abdurochman, S.Si., M.T. dan Dr. Gilang Yubiliana, drg., M.Kes selaku stakeholder.
Berdasarkan hasil diskusi tersebut, diperoleh identifikasi awal kebutuhan sistem yang kemudian disusun dalam bentuk user story dan user requirement. Pada tahap awal, kebutuhan sistem dibagi ke dalam tiga aktor utama, yaitu perawat, dokter, dan pasien. Masing-masing aktor memiliki kebutuhan dan peran yang berbeda dalam penggunaan sistem terapi VRDH. Hasil identifikasi kebutuhan awal tersebut ditunjukkan pada Tabel 3.1 dan Tabel 3.2.  

Aktor	User Story
Perawat	Sebagai seorang perawat, saya ingin menambahkan dan mengelola data pasien, sehingga data pasien dapat tersimpan dengan rapi dan mudah diakses saat proses terapi berlangsung.
	Sebagai seorang perawat, saya ingin melihat daftar pasien yang terdaftar dalam sistem, sehingga saya dapat memantau pasien yang akan menjalani terapi.
	Sebagai seorang perawat, saya ingin melihat riwayat sesi terapi pasien, sehingga saya dapat mengetahui perkembangan terapi pasien.
Dokter	Sebagai seorang dokter, saya ingin login dan mengakses sistem sesuai peran saya.
	Sebagai seorang dokter, saya ingin melihat daftar pasien yang saya tangani, sehingga saya dapat memantau pasien yang menjalani terapi.
	Sebagai seorang dokter, saya ingin memulai sesi terapi baru, sehingga proses terapi dapat dilakukan dan dicatat oleh sistem.
	Sebagai seorang dokter, saya ingin melakukan monitoring sinyal EEG pasien secara real-time, sehingga saya dapat memantau kondisi pasien selama terapi berlangsung.
	Sebagai seorang dokter, saya ingin melihat status hipnosis pasien berdasarkan data EEG, sehingga saya dapat mengetahui tingkat relaksasi atau hipnosis pasien.
	Sebagai seorang dokter, saya ingin mengetahui scene VR yang sedang aktif, sehingga saya dapat memastikan terapi VR berjalan sesuai skenario.
	Sebagai seorang dokter, saya ingin mengakhiri sesi terapi dan menyimpan data sesi ke basis data cloud, sehingga data terapi dapat tersimpan secara aman dan terpusat.
	Sebagai seorang dokter, saya ingin mengisi catatan terapi untuk setiap sesi, sehingga hasil observasi dan evaluasi terapi dapat terdokumentasi.
	Sebagai seorang dokter, saya ingin melihat riwayat sesi terapi pasien, sehingga saya dapat mengevaluasi perkembangan terapi pasien dari waktu ke waktu.
Pasien	Sebagai seorang pasien, saya ingin melakukan registrasi dan login akun, sehingga saya dapat mengakses layanan terapi secara pribadi dan aman.
	Sebagai seorang pasien, saya ingin melihat riwayat terapi yang pernah saya jalani, sehingga saya dapat mengetahui perkembangan terapi saya.
	Sebagai seorang pasien, saya ingin melihat ringkasan hasil setiap sesi terapi, sehingga saya dapat memahami hasil terapi yang telah dilakukan.
	Sebagai seorang pasien, saya ingin membaca informasi edukatif mengenai hipnosis dan terapi VRDH, sehingga saya dapat memahami proses terapi yang akan dijalani.
	Sebagai seorang pasien, saya ingin memberikan feedback setelah sesi terapi, sehingga saya dapat menyampaikan pengalaman dan evaluasi terhadap terapi yang diberikan.
	Selanjutnya, dilakukan pertemuan kedua pada tanggal 18 April 2026 untuk mendiskusikan kembali hasil user story yang telah disusun sebelumnya. Pada pertemuan ini dilakukan evaluasi terhadap rancangan aktor dan alur sistem agar lebih sesuai dengan implementasi di lapangan. Berdasarkan hasil diskusi bersama stakeholder, diputuskan bahwa beberapa peran seperti perawat, dan dokter memiliki fungsi yang saling berkaitan dalam pengoperasian sistem, sehingga struktur aktor disederhanakan menjadi satu aktor utama, yaitu tenaga medis. 
Selain itu, aktor pasien untuk sementara tidak dilibatkan dalam revisi user story karena penelitian masih berada pada tahap awal pengembangan sistem. Pada tahap ini, fokus utama sistem adalah pengolahan, monitoring, dan evaluasi data terapi dari sisi tenaga medis. Oleh karena itu, fitur yang berkaitan dengan akses langsung oleh pasien, seperti melihat hasil terapi atau memberikan feedback, belum menjadi prioritas pengembangan dan akan dipertimbangkan pada tahap pengembangan berikutnya. Hasil revisi user story berdasarkan diskusi kedua ditunjukkan pada Tabel 3.3.
Tabel 3.1 User Stories
Aktor	User Story
Tenaga Medis	Sebagai tenaga medis, saya ingin melakukan otentikasi untuk masuk ke dalam sistem menggunakan kredential yang valid, sehingga keamanan data dan rekam medis pasien dapat terjamin.
	Sebagai tenaga medis, saya ingin melihat dan memperbarui data diri saya.
	Sebagai tenaga medis, saya ingin melihat dan mencari daftar pasien yang saya tangani.
	Sebagai tenaga medis, saya ingin menambah, mengubah, ataupun menghapus data pasien.
	Sebagai tenaga medis, saya ingin mengisi instrumen evaluasi pra-induksi dan pasca-induksi untuk setiap pasien, sehingga saya dapat menganalisis perubahan tingkat kecemasan pasien sebagai tolak ukur hasil terapi.
	Sebagai tenaga medis, saya ingin melakukan pengecekan konektivitas perangkat Virtual Reality (VR) dan Elektroensefalogram (EEG) dengan aplikasi mobile sebelum sesi dimulai, sehingga proses terapi dapat berjalan dengan baik.
	Sebagai tenaga medis, saya ingin mengontrol keberlangsungan terapi, yakni mengakhiri dan memberhentikan terapi.
	Sebagai tenaga medis, saya ingin sistem merekam dan menyimpan seluruh data sesi yang telah selesai.
	Sebagai tenaga medis, saya ingin mengakses daftar riwayat sesi terapi pasien, sehingga saya dapat melakukan evaluasi perkembangan kecemasan pasien.
	Sebagai tenaga medis, saya ingin menghapus entri riwayat sesi yang tidak valid, sehingga kualitas data observasi medis tetap terjaga.

Tabel 3.2 User Requirement
Kode	User Requirement
UR-D01	Sistem harus menyediakan fitur autentikasi login bagi dokter menggunakan kredensial yang valid.
UR-D02	Sistem harus membatasi akses sistem hanya kepada tenaga medis yang berhasil terautentikasi.
UR-D03	Sistem harus menyediakan fitur untuk melihat data profil profesional dokter.
UR-D04	Sistem harus menyediakan fitur untuk memperbarui data profil profesional dokter.
UR-D05	Sistem harus menampilkan daftar pasien yang ditangani oleh dokter.
UR-D06	Sistem harus menyediakan fitur pencarian data pasien berdasarkan nama, ID, atau informasi tertentu.
UR-D07	Sistem harus menyediakan fitur penambahan data pasien baru.
UR-D08	Sistem harus menyediakan fitur perubahan data pasien.
UR-D09	Sistem harus menyediakan fitur penghapusan data pasien.
UR-D10	Sistem harus menyediakan formulir evaluasi pra-induksi untuk setiap pasien.
UR-D11	Sistem harus menyediakan formulir evaluasi pasca-induksi untuk setiap pasien.
UR-D12	Sistem harus menyimpan hasil evaluasi pra-induksi dan pasca-induksi pasien.
UR-D13	Sistem harus menyediakan fitur validasi konektivitas perangkat Virtual Reality (VR) dengan aplikasi mobile sebelum terapi dimulai.
UR-D14	Sistem harus menyediakan fitur validasi konektivitas perangkat Electroencephalogram (EEG) dengan aplikasi mobile sebelum terapi dimulai.
UR-D15	Sistem harus menyediakan fitur untuk memulai, menghentikan sementara, dan mengakhiri sesi terapi.
UR-D16	Sistem harus merekam seluruh data sesi terapi yang telah selesai.
UR-D17	Sistem harus menyimpan riwayat sesi terapi pasien ke dalam basis data.
UR-D18	Sistem harus menampilkan daftar riwayat sesi terapi pasien kepada dokter.
UR-D19	Sistem harus menyediakan fitur evaluasi perkembangan tingkat kecemasan pasien berdasarkan riwayat terapi.
UR-D20	Sistem harus menyediakan fitur penghapusan riwayat sesi terapi yang tidak valid.

3.1.1	Kebutuhan Perangkat Lunak
Kebutuhan perangkat lunak yang digunakan dalam proses pengembangan adalah sebagai berikut:
1.	Sistem Operasi: Windows 10/11 64-bit
2.	Visual Studio Code: Sebagai code editor dalam pengembangan aplikasi.
3.	Node.js: Sebagai runtime environment untuk menjalankan React Native.
4.	React Native: Framework utama dalam pengembangan aplikasi mobile berbasis TypeScript.
5.	Android Studio & Android SDK: Digunakan untuk proses build, debugging, dan emulator Android.
6.	Supabase: Digunakan sebagai layanan backend meliputi autentikasi pengguna, database PostgreSQL, dan penyimpanan file berbasis cloud.
7.	PostgreSQL: Sistem manajemen basis data relasional untuk penyimpanan data terstruktur.
8.	Library Bluetooth React Native: Digunakan untuk komunikasi data antara aplikasi dan perangkat EEG melalui koneksi Bluetooth.
9.	Library Visualisasi Grafik: Digunakan untuk menampilkan grafik sinyal EEG.
3.1.2	Kebutuhan Perangkat Keras
Perangkat keras yang digunakan dalam pengembangan dan pengujian aplikasi mobile ini terdiri dari perangkat pengembangan serta perangkat pendukung terapi VRDH. Perangkat keras yang digunakan untuk proses pengembangan aplikasi adalah sebagai berikut:
1.	Processor		: 11th Gen Intel(R) Core (TM) i5-1135G7 2.42 GHz
2.	Installed RAM		: 16.0 GB 
3.	System type		: 64-bit operating system, x64-based processor
4.	Resolusi Layar		: 1920 x 1080
5.	Penyimpanan (Storage) : SSD 512 GB
Aplikasi yang dikembangkan perlu dijalankan pada perangkat smartphone berbasis Android yang mendukung konektivitas Bluetooth. Perangkat ini berfungsi sebagai media utama untuk menampilkan antarmuka monitoring, menerima data sinyal EEG, serta mengelola penyimpanan dan sinkronisasi data. Dukungan Bluetooth menjadi komponen penting karena komunikasi antara aplikasi dan perangkat EEG dilakukan secara wireless.
Selanjutnya, perangkat penyadap sinyal EEG digunakan untuk menangkap aktivitas sinyal otak pasien selama terapi berlangsung. Perangkat ini mengirimkan data sinyal EEG beserta status hipnosis secara berkala melalui koneksi Bluetooth dengan interval tertentu. Data yang diterima kemudian diproses dan ditampilkan pada aplikasi untuk keperluan monitoring serta disimpan sebagai bagian dari rekaman sesi terapi.
Selain itu, terapi didukung oleh perangkat Virtual Reality berupa Meta Quest yang digunakan untuk menampilkan stimulus visual dalam metode VRDH. Perangkat VR ini menjalankan skenario atau scene terapi yang dirancang sesuai kebutuhan stimulus. Aplikasi mobile tidak melakukan streaming tampilan VR secara langsung, melainkan menerima dan mencatat informasi scene yang sedang aktif sebagai metadata yang dapat disinkronkan dengan data EEG berdasarkan waktu sesi.
3.2	Tahap Desain
Tahap desain dalam metode Extreme Programming (XP) berfokus pada perancangan antarmuka sistem secara sederhana, jelas, dan mudah dipahami oleh pengguna. Desain yang dihasilkan bersifat iteratif dan disesuaikan dengan kebutuhan pengguna berdasarkan user story yang telah dikumpulkan. Pada bagian ini dijelaskan rancangan antarmuka sistem yang digunakan dalam aplikasi. 
3.2.1	Use Case Diagram
Pada tahap pemodelan kebutuhan sistem ini dilakukan agar lebih mudah dalam melanjutkan pada tahap yang selanjutnya yaitu melakukan perancangan sistem. Peneliti melakukan pemodelan menggunakan Unified Modeling Language (UML). Diagram yang akan digunakan antara lain use case diagram dan activity diagram. Pemodelan kebutuhan sistem ini akan dibuat berdasarkan tabel fungsionalitas sistem Tabel 4.3 yang telah diverifikasi oleh stackholder (Lampiran B).
 
Gambar x.x Use Case Diagram
3.1.2	Activity Diagram
A.	Proses Login
 
Gambar x.x Activity Diagram Halaman Home

B.	Proses Edit Profile
Halaman Edit Profile memungkinkan pengguna untuk memperbarui informasi akun mereka. Pengguna dapat mengubah data seperti nama, email, atau informasi lainnya sesuai kebutuhan.
Sistem akan melakukan validasi sebelum data disimpan untuk memastikan keakuratan informasi. Setelah perubahan berhasil, data akan diperbarui secara otomatis di sistem.
 
Gambar x.x
C.	Proses Lihat dan Cari Data Pasien
Halaman daftar pasien digunakan untuk menampilkan seluruh data pasien yang telah terdaftar dalam sistem. Data pasien ditampilkan dalam bentuk list sehingga memudahkan pengguna untuk melihat informasi secara cepat dan terstruktur. Selain itu, pengguna juga dapat melakukan pencarian data pasien dan mengakses detail informasi pasien yang dipilih. Gambar x.x menunjukkan activity diagram untuk proses melihat dan mencari data pasien. Melalui proses tersebut, pengguna dapat mengelola data pasien secara lebih efisien.
Selanjutnya, rancangan antarmuka halaman daftar pasien juga ditunjukkan pada Gambar x.x. Tampilan ini menggambarkan desain halaman daftar pasien yang akan digunakan pengguna, meliputi daftar data pasien, fitur pencarian, tombol navigasi ke detail pasien, serta elemen antarmuka lainnya yang mendukung kemudahan pengelolaan data pasien.
 
Gambar x.x
D.	Proses Melihat Riwayat Sesi
Halaman riwayat sesi digunakan untuk menampilkan seluruh catatan sesi terapi yang telah dilakukan terhadap pasien. Informasi yang ditampilkan mencakup tanggal sesi, durasi, serta hasil atau catatan dari sesi terapi yang telah dilakukan.  Selain itu, halaman ini juga menyediakan fitur filter berdasarkan status sehingga pengguna dapat menampilkan seluruh data sesi, sesi yang berhasil, maupun sesi yang tidak berhasil. Gambar x.x menunjukkan activity diagram untuk proses melihat dan memfilter data historis terapi. 
Selanjutnya, rancangan antarmuka halaman riwayat sesi juga ditunjukkan pada Gambar x.x. Tampilan ini menggambarkan desain halaman riwayat sesi yang akan digunakan pengguna, meliputi daftar riwayat sesi terapi, informasi detail sesi, tombol filter, serta elemen antarmuka lainnya yang mendukung kemudahan pengguna dalam memantau perkembangan pasien.
 
Gambar x.x
E.	Proses Tambah Pasien
Halaman Home merupakan tampilan awal yang muncul ketika pengguna berhasil masuk ke dalam sistem. Halaman ini berfungsi sebagai pusat navigasi utama yang mengarahkan pengguna ke fitur-fitur penting dalam aplikasi. Pada halaman ini ditampilkan beberapa menu utama seperti daftar pasien, riwayat sesi, serta akses ke profil pengguna.
Desain halaman Home dibuat sederhana dengan tujuan agar pengguna dapat dengan cepat memahami fungsi utama aplikasi tanpa kebingungan. Elemen visual dibuat minimalis dengan penempatan menu yang jelas sehingga meningkatkan pengalaman pengguna dalam mengakses fitur yang tersedia.
 
Gambar x.x
F.	Proses Edit Pasien
Halaman Edit Pasien digunakan untuk memperbarui data pasien yang sudah ada. Pengguna dapat mengubah informasi jika terdapat kesalahan atau perubahan data pasien.
Sistem memastikan bahwa perubahan yang dilakukan tetap konsisten dengan data yang sudah tersimpan sebelumnya. Dengan fitur ini, data pasien dapat selalu terjaga akurasinya.
 
Gambar x.x
3.1.3	Desain Database
Kebutuhan data pada pengembangan aplikasi mobile ini dirancang untuk mendukung operasional terapi VRDH yang dilakukan oleh tenaga medis dalam melakukan monitoring dan pengelolaan sesi terapi pasien. Data yang digunakan difokuskan pada kebutuhan utama sistem, yaitu autentikasi dokter, pengelolaan data pasien, serta pencatatan aktivitas terapi dan monitoring EEG selama sesi berlangsung. 
A.	Data Tenaga Medis
Data tenaga medis digunakan untuk menyimpan informasi akun tenaga medis yang menggunakan sistem. Data ini digunakan untuk proses login dan identifikasi dokter pada setiap sesi terapi.
Tabel 3.1 Data Tenaga Medis
Nama Data	Sumber	Tipe Data	Keterangan
id	Sistem	UUID	Identitas unik tenaga medis.
email	Input tenaga medis/admin	VARCHAR(255)	Digunakan untuk login dan identitas akun.
nama	Input tenaga medis/admin	VARCHAR(255)	Nama lengkap tenaga medis.
nomor_telepon	Input tenaga medis	VARCHAR(20)	Nomor telepon tenaga medis
created_at	Sistem	TIMESTAMP	Waktu pembuatan akun.
updated_at	Sistem	TIMESTAMP	Waktu pembaruan data tenaga medis.
B.	Data Pasien
Data pasien digunakan untuk menyimpan informasi pasien yang menjalani terapi VRDH. Struktur data pasien ditunjukkan pada Tabel 3.2.
Tabel 3.6 Data Pasien
Nama Data	Sumber	Tipe Data	Keterangan
patient_id	Sistem	UUID	Identitas unik pasien.
full_name	Input dokter	String	Nama lengkap pasien.
date_of_birth	Input dokter	Date	Tanggal lahir pasien.
gender	Input dokter	Enum/String	Jenis kelamin pasien.
created_at	Sistem	Timestamp	Waktu pembuatan data pasien.
updated_at	Sistem	Timestamp	Waktu pembaruan data pasien.
C.	Data Sesi Terapi
Struktur data sesi terapi yang ditunjukkan pada Tabel 3.9 digunakan untuk mencatat setiap pelaksanaan terapi VRDH. Data ini menghubungkan pasien, dokter, dan klinik dalam satu entitas yang merepresentasikan aktivitas terapi secara lengkap. Informasi waktu mulai, waktu selesai, serta status sesi memungkinkan sistem melakukan pelacakan riwayat terapi secara terstruktur.
Tabel 3.9 Data Sesi Terapi
Nama Data	Sumber	Tipe Data	Keterangan
id	Sistem	UUID	Identitas unik sesi terapi.
id_tenaga_medis	Relasi tabel tenaga_medis	UUID	Referensi tenaga medis yang menangani sesi terapi.
id_pasien	Relasi tabel pasien	UUID	Referensi pasien yang menjalani sesi terapi.
status_sesi	Input sistem/dokter	VARCHAR(20)	Status sesi terapi.
waktu_mulai	Sistem	TIMESTAMP	Waktu mulai sesi terapi.
waktu_selesai	Sistem	TIMESTAMP	Waktu selesai sesi terapi.
durasi_detik	Sistem	INTEGER	Durasi sesi terapi dalam detik.
created_at	Sistem	TIMESTAMP	Waktu pembuatan data sesi terapi.
updated_at	Sistem	TIMESTAMP	Waktu pembaruan data sesi terapi.
D.	Data Sesi Terapi
Struktur data event scene VR sebagaimana terlihat pada Tabel 3.10 digunakan untuk mencatat perubahan stimulus visual selama sesi berlangsung. Pencatatan dilakukan berbasis waktu sehingga dapat disinkronkan dengan data sinyal EEG yang diterima sistem. Pendekatan ini memungkinkan analisis hubungan antara perubahan stimulus dan respons aktivitas otak pasien.
Tabel 3.10 Data Scene VR
Nama Data	Sumber	Tipe Data	Keterangan
vr_event_id	Sistem	UUID	Identitas unik event VR
session_id	Sistem	UUID	Relasi ke sesi terapi
scene_id	Sistem/VR	UUID	Scene yang aktif
stimulus_level	Sistem/VR	Enum/String	LOW/MEDIUM/HIGH (snapshot)
event_type	Sistem	Enum/String	SCENE_START, SCENE_END, SCENE_CHANGE
event_time	Sistem/VR	Timestamp	Waktu perubahan scene terjadi

3.1.4	Perancangan Antarmuka Sistem
A.	Halaman Login
Rancangan antarmuka halaman login juga ditunjukkan pada Gambar x.x. Tampilan ini menggambarkan desain halaman login yang akan digunakan pengguna, meliputi form input email dan password, tombol login, serta elemen antarmuka lainnya yang mendukung kemudahan penggunaan aplikasi.
 
Gambar x.x Activity Diagram Halaman Home
B.	Halaman Home
 Gambar x.x menunjukkan desain halaman home yang dirancang dengan tampilan sederhana dan penempatan menu yang jelas agar pengguna dapat dengan mudah memahami dan mengakses fitur-fitur yang tersedia dalam aplikasi.
 
Gambar x.x
C.	Halaman Profile Pengguna
Halaman Profile menampilkan informasi akun pengguna yang sedang login. Informasi ini mencakup nama, email, serta detail lainnya yang terkait dengan akun.
Halaman ini juga menjadi pusat akses untuk melakukan perubahan data profil atau pengaturan akun. Desain dibuat sederhana agar pengguna mudah mengakses informasi pribadi mereka.
 
Gambar x.x
D.	Halaman Edit Profile
Halaman Edit Profile memungkinkan pengguna untuk memperbarui informasi akun mereka. Pengguna dapat mengubah data seperti nama, email, atau informasi lainnya sesuai kebutuhan.
Sistem akan melakukan validasi sebelum data disimpan untuk memastikan keakuratan informasi. Setelah perubahan berhasil, data akan diperbarui secara otomatis di sistem.
 
Gambar x.x
E.	Halaman Daftar Pasien
Rancangan antarmuka halaman daftar pasien ditunjukkan pada Gambar x.x. Tampilan ini menggambarkan desain halaman daftar pasien yang akan digunakan pengguna, meliputi daftar data pasien, fitur pencarian, tombol navigasi ke detail pasien, serta elemen antarmuka lainnya yang mendukung kemudahan pengelolaan data pasien.
 
Gambar x.x
F.	Halaman Tambah Pasien
Gambar x.x menunjukkan rancangan antarmuka halaman tambah pasien yang digunakan untuk menambahkan data pasien baru ke dalam sistem. Pada halaman ini, pengguna dapat mengisi beberapa informasi pasien seperti nama lengkap, tanggal lahir, jenis kelamin, serta data pendukung lainnya. Selain itu, tersedia tombol simpan untuk menyimpan data pasien yang telah diinput sehingga data dapat digunakan pada proses terapi selanjutnya.
 
Gambar x.x
G.	Halaman Edit Pasien
Halaman Edit Pasien digunakan untuk memperbarui data pasien yang sudah ada. Pengguna dapat mengubah informasi jika terdapat kesalahan atau perubahan data pasien.
Sistem memastikan bahwa perubahan yang dilakukan tetap konsisten dengan data yang sudah tersimpan sebelumnya. Dengan fitur ini, data pasien dapat selalu terjaga akurasinya.
 
Gambar x.x
H.	Halaman Detail Pasien
Rancangan antarmuka halaman detail pasien ditunjukkan pada Gambar x.x. Tampilan ini menggambarkan desain halaman detail pasien yang akan digunakan pengguna, meliputi informasi identitas pasien, daftar riwayat sesi terapi, tombol mulai sesi terapi baru, serta elemen antarmuka lainnya yang mendukung kemudahan pengguna dalam melihat data pasien secara menyeluruh.
 
Gambar x.x
I.	Halaman Cek Konektivitas
Rancangan antarmuka halaman koneksi perangkat juga ditunjukkan pada Gambar x.x. Tampilan ini menggambarkan desain halaman koneksi perangkat yang akan digunakan pengguna, meliputi daftar perangkat yang tersedia, status koneksi perangkat, tombol refresh, serta elemen antarmuka lainnya yang mendukung kemudahan pengguna dalam menghubungkan perangkat terapi ke sistem.
 
Gambar x.x
J.	Halaman Riwayat Sesi
Rancangan antarmuka halaman riwayat sesi juga ditunjukkan pada Gambar x.x. Tampilan ini menggambarkan desain halaman riwayat sesi yang akan digunakan pengguna, meliputi daftar riwayat sesi terapi, informasi detail sesi, tombol filter, serta elemen antarmuka lainnya yang mendukung kemudahan pengguna dalam memantau perkembangan pasien.
 
Gambar x.x
3.3	Coding
Tahap coding dilakukan dengan mengimplementasikan desain sistem ke dalam bentuk kode program agar aplikasi dapat dijalankan sesuai kebutuhan yang telah dirancang sebelumnya. Pada tahap ini, pengembangan sistem menerapkan beberapa prinsip pengembangan perangkat lunak agar kode yang dihasilkan lebih terstruktur, mudah dipahami, dan mudah dikembangkan kembali di masa mendatang.
Beberapa prinsip yang diterapkan pada tahap coding antara lain sebagai berikut:
1.	Simplicity
Pengembangan sistem dilakukan dengan menjaga kesederhanaan struktur kode agar mudah dipahami dan dipelihara. Setiap fitur dikembangkan dengan alur yang jelas tanpa menambahkan kompleksitas yang tidak diperlukan. 
2.	Modularity
Kode program dibagi ke dalam beberapa modul atau komponen sesuai fungsi masing-masing sehingga memudahkan proses pengembangan, pengujian, serta pemeliharaan sistem. 
3.	Reusability
Komponen dan fungsi yang dapat digunakan kembali dirancang untuk mengurangi duplikasi kode sehingga proses pengembangan menjadi lebih efisien. 
4.	Refactoring
Proses perbaikan dan penataan ulang kode dilakukan secara berkala tanpa mengubah fungsi utama sistem. Refactoring bertujuan meningkatkan keterbacaan kode dan kualitas struktur program. 
5.	Consistency
Penulisan kode dilakukan secara konsisten, baik dari segi penamaan variabel, struktur folder, maupun format penulisan kode sehingga memudahkan proses pengembangan secara berkelanjutan.
3.4	Testing
Fase akhir merupakan tahap penutupan kegiatan penelitian dan pengembangan sistem. Pada tahap ini dilakukan evaluasi menyeluruh terhadap hasil implementasi aplikasi, termasuk pengujian fungsionalitas utama seperti autentikasi pengguna, manajemen klinik, pelaksanaan sesi terapi, monitoring EEG, pencatatan event scene VR, serta penyimpanan data sesi ke cloud. 
Mengingat aplikasi ini dikembangkan menggunakan kerangka kerja React Native yang ditujukan untuk memfasilitasi komunikasi perangkat keras medis secara real-time di platform mobile, pengujian tidak hanya dititikberatkan pada keberhasilan sistem secara teknis, tetapi juga pada kualitas interaksi pengguna (User Experience). Oleh karena itu, tahap pengujian pada penelitian ini dibagi menjadi tiga pendekatan utama:
1.	Pengujian Fungsionalitas Sistem (Black-Box Testing)
Pengujian ini berfokus pada verifikasi logika dan fitur teknis aplikasi. Skenario pengujian dirancang untuk memastikan bahwa proses transmisi data via koneksi Bluetooth dari perangkat penyadap EEG, pencatatan metadata dari headset Virtual Reality (Meta Quest), serta sinkronisasi riwayat terapi ke layanan backend (Supabase) dapat beroperasi dengan lancar dan bebas dari bug. Pengujian ini dilakukan secara iteratif pada setiap akhir siklus pengembangan untuk menjaga stabilitas sistem.
2.	Pengujian Heuristik (Heuristic Evaluation)
Sebelum aplikasi diujikan kepada pengguna akhir, antarmuka aplikasi dievaluasi terlebih dahulu oleh pakar (expert evaluator) menggunakan sembilan prinsip Heuristic Mobile. Evaluasi ini bertujuan untuk mengidentifikasi celah usability sedini mungkin—seperti kejelasan indikator status koneksi perangkat atau konsistensi navigasi—tanpa harus melibatkan pengguna akhir secara langsung. Setiap temuan masalah antarmuka diklasifikasikan menggunakan skala Severity Rating (1 hingga 5) untuk menentukan prioritas perbaikan yang harus dilakukan oleh pengembang.

3.	Pengujian Usabilitas (Usability Testing)
Setelah fungsionalitas dan antarmuka dinilai cukup stabil dari hasil evaluasi heuristik, pengujian dilanjutkan dengan melibatkan representasi pengguna akhir, yaitu tenaga medis (dokter gigi atau perawat). Pengujian ini menggunakan skenario tugas (task scenarios) yang mensimulasikan kondisi klinis sesungguhnya untuk mengukur tiga metrik utama:
Learnability (Tingkat Keberhasilan): Diukur melalui perhitungan Success Rate saat tenaga medis mengeksekusi skenario, seperti mendaftarkan pasien baru atau memantau grafik gelombang otak selama terapi berjalan.
Efficiency (Efisiensi Waktu): Diukur berdasarkan time-based efficiency, yaitu jumlah waktu (dalam detik) yang dibutuhkan pengguna untuk merespons dan menyelesaikan setiap skenario tugas di tengah kesibukan praktik medis.
Satisfaction (Kepuasan Pengguna): Diukur menggunakan instrumen kuesioner System Usability Scale (SUS) yang terdiri dari 10 butir pernyataan. Metode ini digunakan untuk memperoleh penilaian objektif yang dapat dikuantifikasi menjadi skor akhir terkait tingkat penerimaan dan kepuasan tenaga medis terhadap aplikasi.

## BAB IV

|    |    |    |    |    |    |
|----|----|----|----|----|----|
|    |    |    |    |    |    |
|    |    |    |    |    |    |
|    |    |    |    |    |    |
|    |    |    |    |    |    |
|    |    |    |    |    |    |
|    |    |    |    |    |    |
|    |    |    |    |    |    |
|    |    |    |    |    |    |
|    |    |    |    |    |    |
|    |    |    |    |    |    |

## 

## DAFTAR PUSTAKA

Abhang, P. A., Gawali, B. W., &amp; Mehrotra, S. C. (2016). *Introduction to EEG- and Speech-Based Emotion Recognition* . Academic Press. https://doi.org/10.1016/C2015-0-01959-1

Aditya, M. D., &amp; Susanty, M. (2022). *Studi Komparasi Maintainability Antara Aplikasi yang Dikembangkan dengan Framework Flutter dan React Native* .

Anwer, F., &amp; Aftab, S. (2017). Latest Customizations of XP: A Systematic Literature Review. *International Journal of Modern Education and Computer Science* , *9* (12), 26–37. https://doi.org/10.5815/ijmecs.2017.12.04

Beck, K. (2004). *Extreme Programming Explained* .

Booch, G., Rumbaugh, J., &amp; Jacobson, I. (2005). *The unified modeling language user guide* (2nd ed). Addison-Wesley.

Chen, P. P.-S. (1976). The entity-relationship model—Toward a unified view of data. *ACM Transactions on Database Systems* , *1* (1), 9–36. https://doi.org/10.1145/320434.320440

De Matos, N. M. P., Staempfli, P., Zoelch, N., Seifritz, E., &amp; Bruegger, M. (2024). Neurochemical dynamics during two hypnotic states evidenced by magnetic resonance spectroscopy. *Scientific Reports* , *14* (1), 29952. https://doi.org/10.1038/s41598-024-80795-3

Eisenman, B. (2017). *Learning React Native: Building Native Mobile Apps with JavaScript* . O’Reilly.

Elmasri, R., &amp; Navathe, S. B. (2016). *Fundamentals of Database System* (7th Edition). Pearson. https://www.pearson.com/store/p/fundamentals-of-database-systems/P100000665256

Ghani, F. A., &amp; Abdurrochman, A. (2024). *PENGEMBANGAN PERANGKAT PEMANTAU GELOMBANG OTAK YANG TERHUBUNG BLUETOOTH* .

Hendini, A. (2016). *PEMODELAN UML SISTEM INFORMASI MONITORING PENJUALAN DAN STOK BARANG (STUDI KASUS: DISTRO ZHEZHA PONTIANAK* . *IV* .

Levenson, J. L. (Ed.). (2018). *The American Psychiatric Association Publishing Textbook of Psychosomatic Medicine and Consultation-Liaison Psychiatry* (Third Edition). American Psychiatric Association Publishing. https://doi.org/10.1176/appi.books.9781615371990

Lucassen, G., Dalpiaz, F., Van Der Werf, J. M. E. M., &amp; Brinkkemper, S. (2016). Improving agile requirements: The Quality User Story framework and tool. *Requirements Engineering* , *21* (3), 383–403. https://doi.org/10.1007/s00766-016-0250-x

Maples-Keller, J. L., Bunnell, B. E., Kim, S.-J., &amp; Rothbaum, B. O. (2017). The Use of Virtual Reality Technology in the Treatment of Anxiety and Other Psychiatric Disorders. *Harvard Review of Psychiatry* , *25* (3), 103–113. https://doi.org/10.1097/HRP.0000000000000138

Niedermeyer, E., &amp; Lopes da Silva, F. (2005). *Electroencephalography: Basic Principles, Clinical Applications, and Related Fields* (5th ed.). Lippincott Williams &amp; Wilkins.

Pedamkar, P. (2019, June 19). UML Activity Diagram. *EDUCBA* . https://www.educba.com/uml-activity-diagram/

Rahmi, R., Sari, R. P., &amp; Suhatman, R. (2016). Pendekatan Metodologi Extreme Programming pada Aplikasi E-Commerce (Studi kasus Sistem Informasi Penjualan Alat-alat Telekomunikasi). *Jurnal Komputer Terapan* , *2* (2), 83–92.

Ramachandrappa, N. C. (2024). *A Comparative Analysis of Native vs React Native Mobile App Development* .

Sharp, H., &amp; Hall, T. (Eds.). (2016). *Agile Processes, in Software Engineering, and Extreme Programming: 17th International Conference, XP 2016, Edinburgh, UK, May 24-27, 2016, Proceedings* (Vol. 251). Springer International Publishing. https://doi.org/10.1007/978-3-319-33515-5

Shrivastava, A., Jaggi, I., Katoch, N., Gupta, D., &amp; Gupta, S. (2021). A Systematic Review on Extreme Programming. *Journal of Physics: Conference Series* , *1969* (1), 012046. https://doi.org/10.1088/1742-6596/1969/1/012046

Slater, M., &amp; Sanchez-Vives, M. V. (2016). Enhancing Our Lives with Immersive Virtual Reality. *Frontiers in Robotics and AI* , *3* . https://doi.org/10.3389/frobt.2016.00074

St. Louis, E. K., Frey, L. C., Britton, J. W., &amp; American Epilepsy Society (Eds.). (2016). *Electroencephalography (EEG): An introductory text and atlas of normal and abnormal findings in adults, children, and infants* . American Epilepsy Society.

Teplan, M. (2002). Fundamentals of EEG Measurement. *Measurement Science Review* , *2* .

Whitworth, D. E., &amp; Wright, K. (2015). Online assessment of learning and engagement in university laboratory practicals. *British Journal of Educational Technology* , *46* (6), 1201–1213. https://doi.org/10.1111/bjet.12193

Yubiliana, G., Abdurrochman, A., Suryani, M., Rika, Z. P., &amp; Nursin, R. (2025). *Effectiveness of Virtual Reality Dental Hypnosis in Lowering Dental Anxiety: Brain Wave Analysis Using EEG* . https://doi.org/10.21203/rs.3.rs-7540723/v1

Yubiliana, G., Putra, R., &amp; Abdurrochman, A. (2021). Q-EEG map of parietal and frontal lobes out of brain waves recording during dental hypnosis practice. *PADJADJARAN JOURNAL OF DENTISTRY* .

Yubiliana, G., Raksanagara, A. S., &amp; Susilawati, S. (2021). Dental Hypnosis Effectiveness to Cortisol Levels As Dental Anxiety Biomarker and Its Correlation with QoL. *Journal of International Dental and Medical Research* , *14* .

Yudhistira, K., Muharni, S., &amp; Saprudin, U. (2021). PENDEKATAN EXTREME PROGRAMMING MODEL PADA PERANCANGAN APLIKASI MENGGUNAKAN UML. *International Research on Big-Data and Computer Technology: I-Robot* , *2* (1), 134. https://doi.org/10.53514/ir.v2i1.86

Zouridakis, G. (2003). *Biomedical Technology and Devices Handbook* (0 ed.). CRC Press. https://doi.org/10.1201/9780203491492