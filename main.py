from time import sleep
import random as rd
from selenium import webdriver
# 如果是chrome或其他浏览器，修改edge为chrome
from selenium.webdriver.edge.options import Options
import toml

with open("conf.toml", "r", encoding="utf8") as f:
    config = toml.load(f)

# config
search_option = config["search_option"]
keywords = search_option["keywords"]
base_url = search_option["base_url"]
loop_time_dict = config["loop_time"]
is_pc_on = search_option["pc_on"]
is_mb_on = search_option["mb_on"]
profile_path = config["profile"]["path"]

keyword_length = len(keywords)

def random_query_with_sleep():
    random_sleep_time = rd.randint(2, 5)
    random_keyword = keywords[rd.randint(0, keyword_length - 1)]
    random_postfix = rd.randint(0, 1e5)
    url = base_url + random_keyword + ' ' + str(random_postfix)
    driver.get(url)
    sleep(random_sleep_time)

# pc
if is_pc_on:
    options = Options()
    options.add_argument(f"--user-data-dir={profile_path}")
    driver = webdriver.Edge(options=options)

    for i in range(loop_time_dict["pc"]):
        random_query_with_sleep()
    driver.quit()

# mb
if is_mb_on:    
    options = Options()
    options.add_argument(f"--user-data-dir={profile_path}")
    options.add_argument("--auto-open-devtools-for-tabs")
    mobileEmulation = {  
        "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },  
        "userAgent" : "Mozilla/5.0 (BB10; Touch) AppleWebKit/537.10+ (KHTML, like Gecko) Version/10.0.9.2372 Mobile Safari/537.10+ Edg/118.0.0.0" 
    }  
    options.add_experimental_option("mobileEmulation", mobileEmulation)
    driver = webdriver.Edge(options=options)

    for i in range(loop_time_dict["mb"]):
        random_query_with_sleep()

    driver.quit()