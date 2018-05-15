<h1 align="center">
  <br>
  Tugas 1 Seleksi Warga Basdat 2018
  <br>
  <br>
</h1>

<h2 align="center">
  <br>
  Passport Data Scraping
  <br>
  <br>
</h2>

### Description
Program yang dibuat akan melakukan pengambilan data pada web https://travel.state.gov untuk mengetahui syarat-syarat tertentu untuk berkunjung ke negara tertentu, pada tugas ini diambil contoh negara Amerika karena memiliki data yang sangat lengkap untuk diambil pada websitenya.
### Specifications

1. Lakukan data scraping dari sebuah laman web untuk memeroleh data atau informasi tertentu __TANPA MENGGUNAKAN API__

2. Daftarkan judul topik yang akan dijadikan bahan data scraping pada spreadsheet berikut: [Topik Data Scraping](http://bit.ly/TopikDataScraping). Usahakan agar tidak ada peserta dengan topik yang sama. Akses edit ke spreadsheet akan ditutup tanggal 10 Mei 2018 pukul 20.00 WIB

3. Dalam mengerjakan tugas 1, calon warga basdat terlebih dahulu melakukan fork project github pada link berikut: https://github.com/wargabasdat/Seleksi-2018/tree/master/Tugas1. Sebelum batas waktu pengumpulan berakhir, calon warga basdat harus sudah melakukan pull request dengan nama ```TUGAS_SELEKSI_1_[NIM]```

4. Pada repository tersebut, calon warga basdat harus mengumpulkan file script dan json hasil data scraping. Repository terdiri dari folder src dan data dimana folder src berisi file script/kode yang __WELL DOCUMENTED dan CLEAN CODE__ sedangkan folder data berisi file json hasil scraper.

5. Peserta juga diminta untuk membuat Makefile sesuai template yang disediakan, sehingga program dengan gampang di-_build_, di-_run_, dan di-_clean_

```Makefile
all: clean build run

clean: # remove data and binary folder

build: # compile to binary (if you use interpreter, then do not implement it)

run: # run your binary
```
### How to use
```
1. Pastikan Python terinstall pada komputer anda
2. Jalankan make / make run untuk mengambil data awal
3. Data yang diambil akan tersimpan pada folder data
```
### JSON Structure
```
{
        "Nama Negara": "Afghanistan",
        "PASSPORT VALIDITY:": "Must be valid for six months at time of entry",
        "BLANK PASSPORT PAGES:": "One page required for entry stamp",
        "TOURIST VISA REQUIRED:": "Yes",
        "VACCINATIONS:": "Polio vaccination up to 1 year before travel is recommended. See our Polio Fact Sheet",
        "CURRENCY RESTRICTIONS FOR ENTRY:": "$20,000",
        "CURRENCY RESTRICTIONS FOR EXIT:": "$20,000",
        "ADDRESS": [
            "Great Massoud (Airport) Road",
            "Kabul, Afghanistan",
            "Telephone: 0700-108-001 or 0700-108-002",
            "Emergency After-Hours Telephone: 0700-108-001",
            "Fax: (00 93) (0) 700-108-564 or (0)202-300-546",
            "kabulacs@state.gov"
        ]
}

### Screenshot
```
![](screenshots/proses pengambilan data.png)
![](screenshots/proses pengambilan data 1.png)
![](screenshots/daftarnegara.png)
![](screenshots/datanegara.png)
```
### Reference 
```
- urlopen
- BeautifulSoup
- time
- json
```

### Author
```
Alvin Limassa 13516039
```

<h1 align="center">
  <br>
  Selamat BerEksplorasi!
  <br>
  <br>
</h1>

<p align="center">
  <br>
  Basdat Industries - Lab Basdat 2018
  <br>
  <br>
</p>
