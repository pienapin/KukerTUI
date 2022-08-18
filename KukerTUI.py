from sys import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
import getpass
import time
import os

if platform == 'win32':
    try:
        s=Service(os.path.dirname(os.path.realpath(__file__))+'\driver\geckodriver.exe')
        options = Options()
        options.headless = True
        driver = webdriver.Firefox(service=s,options=options)
    except:
        print('maaf, browser tidak didukung!')
        time.sleep(2)

driver.get("https://kukerta.unri.ac.id/login")
driver.find_element(By.CSS_SELECTOR, "img[src='/assets/ui.png']").click()

driver.find_element('name', 'identifier').send_keys(input('email: '))
driver.find_element(By.ID, 'identifierNext').click()
time.sleep(3) 
try:
    driver.find_element(By.ID, "passwordNext")
    logEmail = False
except:
    logEmail = True    

while logEmail:
    print('email tidak ditemukan\n')
    driver.find_element('name', 'identifier').clear()
    driver.find_element('name', 'identifier').send_keys(input('email: '))
    driver.find_element(By.ID, 'identifierNext').click()
    time.sleep(3)
    try:
        driver.find_element(By.ID, "passwordNext")
        logEmail = False
    except:
        logEmail = True

driver.find_element('name', 'password').send_keys(getpass.getpass('password (ketikan memang tidak muncul): '))
driver.find_element(By.ID, 'passwordNext').click()
time.sleep(3)
try:
    driver.find_element(By.ID, "dropdownMenu1")
    logPw = False
except:
    logPw = True  
while logPw:
    print('password salah\n')
    driver.find_element('name', 'password').clear()
    driver.find_element('name', 'password').send_keys(getpass.getpass('password (ketikan memang tidak muncul): '))
    driver.find_element(By.ID, 'passwordNext').click()
    time.sleep(3)
    try:
        driver.find_element(By.ID, "dropdownMenu1")
        logPw = False
    except:
        logPw = True  

driver.find_element(By.ID, 'dropdownMenu1').click()

wait = WebDriverWait(driver , 300)
wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()[contains(., '3. Logbook')]]")))
driver.find_element(By.XPATH,"//*[text()[contains(., '3. Logbook')]]").click()

wait = WebDriverWait(driver , 300)
wait.until(EC.presence_of_element_located((By.NAME, "kegiatan")))

driver.find_element(By.XPATH,"//*[text()[contains(., 'Isi Logbook')]]").click()
lagi = 'y'
while lagi == 'y':
    salah = True
    while salah:
        print('\nIsi Logbook (Perhatikan penulisan!)')
        tan = str(int(input('1. tanggal berapa (tanpa bulan dan tahun): ')))
        bul = input('bulan apa: ').title()
        tah = input('tahun berapa: ')
        while int(tah) < 2019:
            print('tahun tidak valid')
            tah = input('tahun berapa: ')
        keg = input('2. kegiatan: ')
        lok = input('3. lokasi kegiatan: ')
        pih = input('4. pihak terlibat: ')
        ura = input('5. uraian kegiatan: ')
        has = input('6. hasil kegiatan: ')
        ken = input('7. kendala kegiatan: ')
        est = input('8. estimasi waktu kegiatan (isi dengan hanya angka): ')
        konfirmasi = 'n'
        while konfirmasi == 'n' :
            print('\n\nKonfirmasi isi Logbook')
            print('1. tanggal: '+tan+' '+bul+' '+tah)
            print('2. kegiatan: '+keg)
            print('3. lokasi kegiatan: '+lok)
            print('4. pihak terlibat: '+pih)
            print('5. uraian kegiatan: '+ura)
            print('6. hasil kegiatan: '+has)
            print('7. kendala kegiatan: '+ken)
            print('8. estimasi waktu kegiatan: '+est)
            konfirmasi = input('\napakah data yang diinput sudah benar?(y/n) : ').lower()
            match konfirmasi:
                case 'y':
                    salah = False
                    ganti_data = 'n'
                case 'n':
                    ganti_data = 'y'
            while ganti_data == 'y':
                ubah = int(input('\ndata apa yang ingin diubah? (jawab dengan angka urutan data, 1 untuk ubah tanggal, 2 untuk ubah kegiatan, dst. Masukkan 0 untuk mengubah semua data): '))
                print()
                match ubah:
                    case 1:
                        tan = str(int(input('1. tanggal berapa (tanpa bulan dan tahun): ')))
                        bul = input('bulan apa: ').title()
                        tah = input('tahun berapa: ')
                    case 2:
                        keg = input('2. kegiatan: ')
                    case 3:
                        lok = input('3. lokasi kegiatan: ')
                    case 4:
                        pih = input('4. pihak terlibat: ')
                    case 5:
                        ura = input('5. uraian kegiatan: ')
                    case 6:
                        has = input('6. hasil kegiatan: ')
                    case 7:
                        ken = input('7. kendala kegiatan: ')
                    case 8:
                        est = input('8. estimasi waktu kegiatan (isi dengan hanya angka): ')
                    case 0:
                        konfirmasi = 'y'
                        ganti_data = 'n'
                ganti_data = input('apakah masih ada data yang ingin diubah?(y/n) : ').lower()

    Select(driver.find_element('name', 'tanggal_d')).select_by_visible_text(tan)
    Select(driver.find_element('name', 'tanggal_m')).select_by_visible_text(bul)
    Select(driver.find_element('name', 'tanggal_y')).select_by_visible_text(tah)
    driver.find_element('name', 'kegiatan').send_keys(keg)
    driver.find_element('name', 'lokasi_kegiatan').send_keys(lok)
    driver.find_element('name', 'pihak_terlibat').send_keys(pih)
    driver.find_element('name', 'uraian_kegiatan').send_keys(ura)
    driver.find_element('name', 'hasil_kegiatan').send_keys(has)
    driver.find_element('name', 'kendala_kegiatan').send_keys(ken)
    driver.find_element('name', 'waktu_kegiatan').send_keys(est)
    gas = True
    while gas:
        submit = input('submit logbook? (submit/cancel): ').lower()
        if submit == 'submit':
            driver.find_element(By.XPATH, "//button[@type='submit']").click()
            print('data sudah disubmit!')
            time.sleep(2)
            driver.find_element(By.XPATH,"//*[text()[contains(., 'Isi Logbook')]]").click()
            gas = False
        elif submit == 'cancel':
            print('pengisian logbook dibatalkan, terima kasih')
            driver.find_element('name', 'kegiatan').clear()
            driver.find_element('name', 'lokasi_kegiatan').clear()
            driver.find_element('name', 'pihak_terlibat').clear()
            driver.find_element('name', 'uraian_kegiatan').clear()
            driver.find_element('name', 'hasil_kegiatan').clear()
            driver.find_element('name', 'kendala_kegiatan').clear()
            driver.find_element('name', 'waktu_kegiatan').clear()
            gas = False
    lagi = input('isi lagi?(y/n) : ')