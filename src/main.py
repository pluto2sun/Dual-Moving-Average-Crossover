import re
import requests
# import sys
# import io
# import steam 
# from retrying import retry
# from bs4 import BeautifulSoup
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from loguru import logger
import all_cookies

# @retry(stop_max_attempt_number=2, wait_fixed=10000)
# def get_buff_index(page_num:int, game:str):
#     r = requests.get(buff_index_json_fmt.format(page_num=page_num, game=game), headers=headers, timeout=20)
#     assert r.status_code == 200, "Falied to fetch buff index with code: " + str(r.status_code)

#     assert r.json()["code"] == "OK", str(r.json())

#     return r.json()["data"]["items"]

# ======== proxies ========
proxies = {
    "http": "http://127.0.0.1:7890",
    "socks5": "https://127.0.0.1:7890",
}
# ======== log ========
logger.add("log/debug.log", level="DEBUG", rotation="10 MB", format="{time} {level} {message}")
logger.add("log/warning.log", level="WARNING", rotation="10 MB", format="{time} {level} {message}")

def check_url(url:str, headers:str, name:str):
    url_response = None 
    try:
        url_response = requests.get(url = url, headers = headers, proxies = proxies, timeout = 10)
        url_response.raise_for_status() # 检查HTTP响应码是否为200
        logger.debug(f"{name}_response: {url_response.text}")
    except  Exception as e:
        logger.exception(f"Error occurred when requesting {url}: {e}", url=url, e=str(e))
    return url_response




# ======== main ========
if __name__ == "__main__":
    # 构造请求头，添加cookie信息
    buff_headers = {
        "Cookie": all_cookies.cookies["buff_cookies"],
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    c5_headers = {
        "Cookie": all_cookies.cookies["c5_cookies"],
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    uuyp_headers = {
        "Cookie": all_cookies.cookies["uuyp_cookies"],
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    igxe_headers = {
        "Cookie": all_cookies.cookies["igxe_cookies"],
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    steam_headers = {
        "Cookie": all_cookies.cookies["steam_cookies"],
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    iflow_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
    }
    # 构造登录请求
    iflow_url = "https://www.iflow.work/steam?platform=buff-igxe-c5-uuyp&game=csgo-dota2&order=buy&pagenum=1&min_price=1.0&max_price=5000.0&min_volume=10"
    iflow_url_response = check_url (iflow_url, iflow_headers, "iflow")
    
    # buff_url = "https://buff.163.com/goods/42322?from=market#tab=selling"
    # buff_url_response =check_url(buff_url, buff_headers, "buff")

    # c5_url = "https://www.c5game.com/csgo/1098192325802266624/AK-47%20%7C%20%E4%B8%80%E5%8F%91%E5%85%A5%E9%AD%82/sell"
    # buff_url_response =check_url(c5_url, c5_headers, "c5")

    # #把cookie字符串处理成字典，以便接下来使用
    # cookies = {}
    # for line in cookie_str.split(";"):
    #     key, value = line.split("=", 1)
    #     cookies[key] = value


    

    # buff_soup = BeautifulSoup(buff_response.text, "html.parser")
    # c5_soup = BeautifulSoup(c5_response.text, "html.parser")
    # # 在解析网页内容后，需要使用特定的选择器来获取需要的信息。例如，可以使用以下代码来获取所有商品的名称和价格：
    # items = soup.select(".item")
    # for item in items:
    #     name = item.select_one(".item-name").text
    #     price = item.select_one(".item-price").text
    #     print(name, price)

    # # 接着，可以使用selenium库来打开buff和c5网站，并自动搜索并购买商�?,打开浏览器并登录buff和c5网站
    # browser = webdriver.Chrome()
    # browser.get("https://www.buff.com/")
    # # 进行登录操作





    # # 在buff中搜索需要购买的商品
    # search_box = browser.find_element_by_name("search")
    # search_box.send_keys(name)
    # search_box.send_keys(Keys.RETURN)

    # # 在搜索结果中购买商品
    # item = browser.find_element_by_class_name("item")
    # buy_button = item.find_element_by_class_name("buy-button")
    # buy_button.click()

    # # 在c5中搜索需要购买的商品
    # browser.get("https://www.c5game.com/")
    # # 进行登录操作
    # # ...

    # search_box = browser.find_element_by_id("search-input")
    # search_box.send_keys(name)
    # search_box.send_keys(Keys.RETURN)

    # # 在搜索结果中购买商品
    # item = browser.find_element_by_class_name("item")
    # buy_button = item.find_element_by_class_name("buy-button")
    # buy_button.click()

    # # 最后，可以使用steam库来登录Steam账号，并在Steam市场中出售购买的商品。可以使用以下代码：
    # # 登录Steam账户
    # username = "your_username"
    # password = "your_password"
    # steam.login(username, password)

    # # 定义要购买的商品名称和价�?
    # item_name = "Item Name"
    # item_price = 10.00

    # # 获取Steam市场中的商品列表
    # listings = steam.market.get_listings("730", item_name)

    # # 找到要购买的商品
    # for listing in listings:
    #     if listing["price"] == item_price:
    #         listing_id = listing["listingid"]
    #         break

    # # 购买商品
    # steam.market.buy_item(listing_id, item_price)







