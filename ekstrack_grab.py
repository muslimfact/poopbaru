import time
import os
import re

# Load semua link dari link.txt
with open('link.txt', 'r') as f:
    links = [line.strip() for line in f if line.strip()]

total_links = len(links)
total_found = 0
total_not_found = 0

# Set opsi headless
co = ChromiumOptions()
co.set_argument('--headless=new')
page = ChromiumPage(co)

# Buka halaman Grab n Watch
page.get('https://grabnwatch.com')

# Tunggu elemen 'Checking your browser...' hilang
page.wait.ele_deleted('#checkingMessage', timeout=30)

# File hasil
output_file = 'output_link.txt'

# Pastikan file output_link.txt ada
if not os.path.exists(output_file):
    with open(output_file, 'w'): pass

# Loop tiap link
for i, url in enumerate(links, start=1):
    print(f'\n🔄 Memproses {i} dari {total_links}: {url}')

    # Cari input dan isi
    input_box = page.ele('#video_url')
    if input_box:
        input_box.input(url)
    else:
        print('❌ Input box tidak ditemukan!')
        total_not_found += 1
        continue

    # Klik tombol
    grab_btn = page.ele('#submitBtn')
    if grab_btn:
        grab_btn.click()
    else:
        print('❌ Tombol Grab tidak ditemukan!')
        total_not_found += 1
        continue

    # Tunggu hasil muncul
    time.sleep(5)

    # Ambil isi elemen #result
    result_div = page.ele('#result')
    if result_div:
        html_result = result_div.inner_html
        # Cari semua href yang dimulai dengan /w/
        hrefs = re.findall(r'href="(/w/[^"]+)"', html_result)
        if hrefs:
            total_found += 1
            with open(output_file, 'a', encoding='utf-8') as f:
                for h in hrefs:
                    full_link = f'https://grabnwatch.com{h}'
                    print(f'✅ Link ditemukan: {full_link}')
                    f.write(full_link + '\n')
        else:
            print('⚠️ Tidak ditemukan link /w/ dalam #result')
            total_not_found += 1
    else:
        print('⚠️ Elemen #result tidak ditemukan')
        total_not_found += 1

    time.sleep(2)

# Tutup browser
page.quit()

# Ringkasan
print('\n===== RINGKASAN =====')
print(f'📄 Total link di link.txt     : {total_links}')
print(f'✅ Total link ditemukan       : {total_found}')
print(f'❌ Total tidak ditemukan/link rusak : {total_not_found}')
print(f'\n📁 Semua link disimpan ke: {output_file}')
