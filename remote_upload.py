

import base64
import httpx

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import urllib.parse

# Lanjutkan eksekusi kode
def encrypt_url(url, key):
    # Pastikan kunci adalah 16-byte
    key = key.encode('utf-8')
    cipher = AES.new(key, AES.MODE_ECB)

    # Pad URL menggunakan PKCS7
    padded_url = pad(url.encode('utf-8'), AES.block_size)

    # Enkripsi data
    encrypted = cipher.encrypt(padded_url)

    # Encode hasil enkripsi ke Base64 URL-safe
    encrypted_base64 = base64.urlsafe_b64encode(encrypted).decode('utf-8')
    return encrypted_base64

# API Keys

vinovo_api_key = "8b857a827319ed70f22e4d0668853f"
bigwarp_api_key = "1185roh927m637ogi3lv"

doodstream_api_key = "219725bbkborbourrp2cd4"
easyvidplay_api_key = "1a9f2e28183ebfe2f5551066"
streamup_api_key = "71defff7b74869da23c8e1c905bb8594"

voesx_api_key = "Wr7fjmWTBp6EY0XGYJZwleaMJiJ2cuf21c3UvSpDd7GtPLAVnQTGiY9RNtwCyCbK"

key = "mysecretkey12345"  # Kunci AES untuk enkripsi




vinovo_api_endpoint  = "https://api.vinovo.si/api/upload/url"
bigwarp_api_endpoint  = "https://bigwarp.io/api/upload/url"
doodstream_api_endpoint  = "https://doodapi.com/api/upload/url"
easyvidplay_api_endpoint = "https://easyvidplay.com/api/v1/video/advance-upload"
streamup_api_endpoint = "https://api.streamup.cc/v1/remote"

voesx_api_endpoint = "https://voe.sx/api/upload/url"


# Variabel untuk menghitung jumlah sukses
success_count = 0



# Read URLs from output.txt
try:
    with open('output_link.txt', 'r') as file:
        urls = file.readlines()
        # urls = [url.strip() for url in urls if url.strip()]  # Remove empty lines and whitespace
        urls = [f"https://darenx-upbkafe.hf.space/download?url={url.strip()}" for url in urls if url.strip()]
    
    total_urls = len(urls)  # Total link yang akan diproses

    # Encrypt each URL and send GET requests to both APIs
    for index, url in enumerate(urls, start=1):
       
        
        print(f"**=> Processing {index} of {total_urls}...")  # Menampilkan progress

        try:
            # doodstream request
            response_doodstream= httpx.get(doodstream_api_endpoint, params={"key": doodstream_api_key, "url": url})
            if response_doodstream.status_code == 200:
                success_count += 1
            else:
                print(f"Failed doodstream: {url} - doodstream Response: {response_doodstream.status_code} - {response_doodstream.text}")
        except Exception as e:
            print(f"Error during dood tream request for {url}: {e}")

        
        
        
        
        
        
        

        try:
            # vinovo request
            response_vinovo = httpx.get(vinovo_api_endpoint, params={"key": vinovo_api_key, "url": url})
            if response_vinovo.status_code == 200:
                success_count += 1
            else:
                print(f"Failed vinovo : {url} - Vinovo Response: {response_vinovo.status_code} - {response_vinovo.text}")
        except Exception as e:
            print(f"Error during Vinovo request for {url}: {e}")

        

        try:
            url_to_upload = f"{bigwarp_api_endpoint}?key={bigwarp_api_key}&url={url}"

            # bigwarp request
            response_bigwarp = httpx.get(url_to_upload)
            if response_bigwarp.status_code == 200:
                success_count += 1
            else:
                print(f"Failed bigwarp: {url} - bigwarp Response: {response_bigwarp.status_code} - {response_bigwarp.text}")
        except Exception as e:
            print(f"Error during bigwarp request for {url}: {e}")

       
       
       
        try:
            # encode URL untuk jaga-jaga (opsional, tergantung API)
            encoded_url = urllib.parse.quote(url, safe=':/?&=%')  # biar format URL tetap valid
            payload = {
                "url": encoded_url
               
            }
    
            headers = {
                "accept": "application/json",
                "api-token": easyvidplay_api_key,
                "Content-Type": "application/json"
            }
    
            response_easyvidplay = httpx.post(easyvidplay_api_endpoint, json=payload, headers=headers)
            if response_easyvidplay.status_code == 200:
                success_count += 1
            else:
                print(f"Status: {response_easyvidplay.status_code} - {response_easyvidplay.text} - {url} ")
    
        except Exception as e:
            print(f"Error during easyvidplay request for {url}: {e}")
        

        print(f"==>  {index} of {total_urls} SUCCESS UPLOAD KE DropLOAD & Lulustream  <=====")

    # Tampilkan total jumlah sukses
    print("\n=========================================")
    print(f"Total Successful Uploads: {success_count}")
    print("=========================================")

except FileNotFoundError:
    print("The file 'output_link.txt' was not found. Please ensure it exists in the same directory.")
