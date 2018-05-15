# import library
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json

# variabel global
# url dari halaman utama yang memuat data negara-negara passport yang dikeluarkan oleh Amerika
url_mainpage = "https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages"
# url file json yang dibuat
url_json = "C:/Users/alvin limassa/Documents/GitHub/Seleksi-2018/Tugas1/dataListNegara.json"

#program utama
if __name__ == "__main__":
    # membaca halaman web dari url utama
    page = urlopen(url_mainpage+".html").read()
    # parse hasil baca url
    mainsoup = BeautifulSoup(page,'html.parser')
    # mencari bagian yang memuat keterangan negara-negara
    section_namaNegara = mainsoup.findAll("div",{"class":"segmentMenu parbase section"})
    # mencari negara-negara yang ada
    container_listNegara = section_namaNegara[1].findAll("p",{})

    # tahap proses
    result = []
    i1 = 0
    count = 0
    print("Starting process...")
    while i1 < len(container_listNegara):
        # penulisan nama negara kedalam format json
        nama_negara = section_namaNegara[1].findAll("p",{})[i1].text.strip()
        hasil = {
            "no" : i1+1,
            "nama" : nama_negara
        }
        result.append(hasil)
        i1+=1

    # penulisan kedalam json
    with open(url_json,"w") as f:
        json.dump(result,f,indent=4)
        