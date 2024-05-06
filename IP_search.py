import time
import requests
from bs4 import BeautifulSoup
import base64
import os
import pandas as pd
def extract_urls_with_target_blank(html_content):
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all anchor tags with both 'href' attribute and 'target="_blank"' attribute
    anchor_tags = soup.find_all('a', href=True, target='_blank')

    # Extract the 'href' attribute from each anchor tag found
    urls = [tag['href'] for tag in anchor_tags]

    return urls
def generate_url_with_parameters(base_url, qbase64_value, page_value):
    # Construct the URL with the provided parameters
    url_with_parameters = f"{base_url}?qbase64={qbase64_value}&page={page_value}&page_size=15"
    return url_with_parameters
def Domain(qbase64_value,burp0_cookies,burp0_headers):
    url_list=[]
    base_url = "https://fofa.info:443/result"
    for i in range(1,6):
        print(i)
        session = requests.session()
        burp0_url = generate_url_with_parameters(base_url, qbase64_value, i)
        # burp0_cookies = {"isRedirectLang": "1", "is_flag_login": "0", "is_mobile": "pc", "_ga": "GA1.1.2043739424.1714900122", "Hm_lvt_4275507ba9b9ea6b942c7a3f7c66da90": "1714900122", "__fcd": "xt6nTOG5KIn40u4q3VSwaAc4", "baseShowChange": "false", "viewOneHundredData": "false", "befor_router": "%2F", "fofa_token": "eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6NDI4MjYwLCJtaWQiOjEwMDI0NjczOSwidXNlcm5hbWUiOiJIaWVuZHoiLCJleHAiOjE3MTUxNjA4Nzh9.T5DysJI-KGZvsU_wpiMVwRJ_aNqV3o8fIBYaPaTRQndPUSaEuib7lKjIIeRzYb7ikqcjPaG14wHggwaStq4PVA", "user": "%7B%22id%22%3A428260%2C%22mid%22%3A100246739%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22Hiendz%22%2C%22nickname%22%3A%22Hiendz%22%2C%22email%22%3A%22dinhconghien2000%40gmail.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%22717360031ceb4fb012cd2ed0c22b38ef%22%2C%22category%22%3A%22user%22%2C%22rank_avatar%22%3A%22%22%2C%22rank_level%22%3A0%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22company_name%22%3A%22Hiendz%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22fofa_point%22%3A0%2C%22credits%22%3A1%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%2C%22data_limit%22%3A%7B%22web_query%22%3A300%2C%22web_data%22%3A3000%2C%22api_query%22%3A0%2C%22api_data%22%3A0%2C%22data%22%3A-1%2C%22query%22%3A-1%7D%2C%22expiration_notice%22%3Afalse%2C%22remain_giveaway%22%3A0%2C%22fpoint_upgrade%22%3Afalse%7D", "Hm_lpvt_4275507ba9b9ea6b942c7a3f7c66da90": "1714956181", "_ga_9GWBD260K9": "GS1.1.1714956156.2.1.1714956953.0.0.0"}
        # burp0_headers = {"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.199 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://fofa.info/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i", "Connection": "close"}
        response=session.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
        # time.sleep(5)
        urls_with_target_blank1=extract_urls_with_target_blank(response.text)
        print("URLs with target=_blank:")
        for url in urls_with_target_blank1:
         url_list.append(url)
    for url in url_list: print(url)
    return url_list
def process_ip_file(file_path,current_directory,burp0_cookies,burp0_headers):
    with open(file_path, 'r') as file:
        # Read each line (IP address) from the file
        ip_addresses = file.readlines()

    # Remove any leading or trailing whitespace from each IP address
    ip_addresses = [ip.strip() for ip in ip_addresses]

    # Encode each IP address to Base64 and pass it to the Domain function
    for ip in ip_addresses:
        encoded_ip =base64.b64encode(ip.encode('utf-8')).decode('utf-8')
        url_list= Domain(encoded_ip,burp0_cookies,burp0_headers)
    # Construct the file path
        file_path = os.path.join(current_directory, f'{ip}.xlsx')
    # Write the url_list to an Excel file
        df = pd.DataFrame({'URLs': url_list})
        df.to_excel(file_path, index=False)
    
if __name__ == "__main__":
    # qbase64_value = "45.117.82.17"
    # encoded_bytes = base64.b64encode(qbase64_value.encode('utf-8')).decode('utf-8')
    # # qbase64_value = "NDUuMTE3LjgyLjE3"
    # Domain(encoded_bytes)
    # print(encoded_bytes)
    burp0_cookies = {"isRedirectLang": "1", "is_flag_login": "0", "is_mobile": "pc", "_ga": "GA1.1.2043739424.1714900122", "Hm_lvt_4275507ba9b9ea6b942c7a3f7c66da90": "1714900122", "__fcd": "xt6nTOG5KIn40u4q3VSwaAc4", "baseShowChange": "false", "viewOneHundredData": "false", "befor_router": "%2F", "fofa_token": "eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6NDI4MjYwLCJtaWQiOjEwMDI0NjczOSwidXNlcm5hbWUiOiJIaWVuZHoiLCJleHAiOjE3MTUyMzY5Mjd9.PSQAMk6OeRMigs085qONeeSP7ofHTtxRb1ND3PXOaj7aogI3cQIHAPeqhv5mWa9qX52279VmZ4pBwIO0S122Ng", "user": "%7B%22id%22%3A428260%2C%22mid%22%3A100246739%2C%22is_admin%22%3Afalse%2C%22username%22%3A%22Hiendz%22%2C%22nickname%22%3A%22Hiendz%22%2C%22email%22%3A%22dinhconghien2000%40gmail.com%22%2C%22avatar_medium%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22avatar_thumb%22%3A%22https%3A%2F%2Fnosec.org%2Fmissing.jpg%22%2C%22key%22%3A%22717360031ceb4fb012cd2ed0c22b38ef%22%2C%22category%22%3A%22user%22%2C%22rank_avatar%22%3A%22%22%2C%22rank_level%22%3A0%2C%22rank_name%22%3A%22%E6%B3%A8%E5%86%8C%E7%94%A8%E6%88%B7%22%2C%22company_name%22%3A%22Hiendz%22%2C%22coins%22%3A0%2C%22can_pay_coins%22%3A0%2C%22fofa_point%22%3A0%2C%22credits%22%3A1%2C%22expiration%22%3A%22-%22%2C%22login_at%22%3A0%2C%22data_limit%22%3A%7B%22web_query%22%3A300%2C%22web_data%22%3A3000%2C%22api_query%22%3A0%2C%22api_data%22%3A0%2C%22data%22%3A-1%2C%22query%22%3A-1%7D%2C%22expiration_notice%22%3Afalse%2C%22remain_giveaway%22%3A0%2C%22fpoint_upgrade%22%3Afalse%7D", "Hm_lpvt_4275507ba9b9ea6b942c7a3f7c66da90": "1714977775", "_ga_9GWBD260K9": "GS1.1.1714977482.5.1.1714977779.0.0.0"}
    burp0_headers = {"Sec-Ch-Ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\"", "Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "\"Linux\"", "Upgrade-Insecure-Requests": "1", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.6099.199 Safari/537.36", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-User": "?1", "Sec-Fetch-Dest": "document", "Referer": "https://fofa.info/", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "Priority": "u=0, i", "Connection": "close"}

    process_ip_file(r"C:\Users\Acer\Desktop\list.txt",r"C:\Users\Acer\Desktop",burp0_cookies,burp0_headers)
    