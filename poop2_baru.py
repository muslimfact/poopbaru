import requests
import re
import concurrent.futures
from domain_ganti import base_poop_api,poop_slash


# Mengosongkan file output_link.txt
open('output_link.txt', 'w').close()

def get_video_link(url):
    try:
        video_id = url.split('/')[-1]
        api_urls = [
            f'{base_poop_api}{poop_slash}?id={video_id}'
        ]
        for api_url in api_urls:
            print(f"Fetching: {api_url}")
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                'priority': 'u=0, i',
                'referer': 'https://poopstream.net/',
                'sec-ch-ua': '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132")',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Linux"',
                'sec-fetch-dest': 'iframe',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36',
            }

            response = requests.get(api_url, headers=headers)
            if response.status_code == 200 and 'player("' in response.text:
                match = re.search(r'player\("a",\s*"(.*?)",\s*"(.*?)",\s*"(https?://[^"]+\.mp4)"\)', response.text)
                if match:
                    video_link = match.group(3)
                    return video_link

    except Exception as e:
        print(f"Error in get_video_link: {e}")
    return None



# Membaca file link.txt
try:
    with open('link.txt', 'r') as file:
        links = file.readlines()
except Exception as e:
    print(f"Error reading link.txt: {e}")
    links = []

# Menyimpan hasil ke output_link.txt
try:
    total_links = len(links)
    with open('output_link.txt', 'w') as output_file:
        found_links = []
        for index, link in enumerate(links):
            link = link.strip()
            if link:
                print(f"Proses {index + 1} dari {total_links}")
                video_link = get_video_link(link)
                if video_link:
                    output_file.write(video_link + '\n')
                    print(f"{video_link}\n")
                    found_links.append(video_link)

    print(f'Jumlah link yang ditemukan: {len(found_links)}')
except Exception as e:
    print(f"Error writing to output_link.txt: {e}")
