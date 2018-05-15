# import library
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time
import json

# variabel global
# url dari halaman utama yang memuat data negara-negara passport yang dikeluarkan oleh Amerika
url_mainpage = "https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages"

# fungsi untuk membaca data dari 1 negara
def scrape_item(url):
    result =[]
    # membaca url jika error maka data akan dikosongkan
    try:
        page = urlopen(url).read()
    except:
        print("MaskExp ERROR!!!")
        return {}
    # parse page
    soup = BeautifulSoup(page,'html.parser')
    
    # mencari data yang diperlukan
    container_box = soup.findAll("div",{"class":"tsg-rwd-qf-box"})

    # variabel penampung judul dan isi datanya
    t_title = []
    t_data = []
    i = 0
    # proses pengambilan data satu per satu
    while i < len(container_box)/2:
        container_title = container_box[i].findAll("div",{"class":"tsg-rwd-qf-box-title"})
        container_data = container_box[i].findAll("div",{"class":"tsg-rwd-qf-box-data"})
        c_title = container_title[0].text.strip()
        c_data = container_data[0].text.strip()
        t_title.append(c_title)
        t_data.append(c_data)
        i+=1
    try:
        c_alamat = soup.findAll("p",{"class":"address"})[0].text.strip().split('\n')
    except:
        try:
            c_alamat = soup.findAll("div",{"class":"tsg-rwd-accordion-copy"})[0].text.strip().split('\n')
        except:
            c_alamat = []
            print("Alamat Kosong")
    item = {
        t_title[0] : t_data[0],
        t_title[1] : t_data[1],
        t_title[2] : t_data[2],
        t_title[3] : t_data[3],
        t_title[4] : t_data[4],
        t_title[5] : t_data[5],
        "ADDRESS" : c_alamat
    }
    
    return item

# Program utama
if __name__ == "__main__":
    # membaca halaman web dari url utama
    page = urlopen(url_mainpage+".html").read()
    # parse hasil baca url
    mainsoup = BeautifulSoup(page,'html.parser')
    # mencari bagian yang memuat keterangan negara-negara
    section_namaNegara = mainsoup.findAll("div",{"class":"segmentMenu parbase section"})
    # mencari negara-negara yang ada
    container_listNegara = section_namaNegara[1].findAll("p",{})
    i1 = 0
    count = 0
    print("Starting process...")
    while i1 < len(container_listNegara):
        # print(section_namaNegara[1].findAll("p",{})[i1].text.strip())
        nama_negara = section_namaNegara[1].findAll("p",{})[i1].text.strip()
        url = url_mainpage + "/" + nama_negara.replace(" ","") + '.html'
        url_json = "C:/Users/alvin limassa/Documents/GitHub/Seleksi-2018/Tugas1/data/" + nama_negara + ".json"
        hasil = scrape_item(url)
        with open(url_json,"w") as f:
            json.dump(hasil,f,indent=4)
        time.sleep(3)
        count+=1
        print("Progress done (" + str(count) + "/" + str(len(container_listNegara)) + ")")
        i1+=1