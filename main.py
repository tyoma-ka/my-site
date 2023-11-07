import requests
import time
import datetime


url_main = 'https://www.ui42.sk'
url_products = 'https://www.ui42.sk/projekty'
monitoring_duration = 7 * 24 * 60
interval = 10 * 60 #поменяй потом
number_of_requests = 0
all_time_main = 0
all_time_products = 0
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"logs_{timestamp}.txt"
with open(filename, 'w') as file:
    print(
        f"{'nazov stranky':<30} {'datum':<10} {'cas':<8} {'error code':<5} {'velkost obsahu':<7} {'cas nacitania':<15} {'dlhe nacitavanie'}",
        file=file)

def check_website(url):
    current_time = time.localtime()
    current_date = time.strftime("%Y-%m-%d", current_time)
    current_time_str = time.strftime("%H:%M:%S", current_time)
    load_time = 0
    content_size = 0
    long_loading = False
    error_code = None
    try:
        start_time = time.time()
        response = requests.get(url)
        end_time = time.time()
        load_time = end_time - start_time
        if load_time > 10:
            long_loading = True
        if response.status_code == 200:
            content_size = len(response.content)
        else:
            print(f'Сайт вернул статусный код {response.status_code}')
    except requests.RequestException as e:
        error_code = e
        print(f"Ошибка при попытке получить доступ к сайту: {e}")
    #print(url, current_date, current_time_str, error_code, content_size, load_time, long_loading)
    result = (url, current_date, current_time_str, error_code, content_size, load_time, long_loading)
    return result


minutes_elapsed = 0
while minutes_elapsed < monitoring_duration:
    number_of_requests += 1

    result_main = check_website(url_main)
    all_time_main += result_main[5]
    result_products = check_website(url_products)
    all_time_products += result_products[5]
    with open(filename, 'a') as file:
        print(f"{str(result_main[0]):<32} {str(result_main[1]):<12} {str(result_main[2]):<10} {str(result_main[3]):<5} {str(result_main[4]):<7} {str(result_main[5]):<20} {str(result_main[6])}", file=file)
        print(f"{str(result_products[0]):<32} {str(result_products[1]):<12} {str(result_products[2]):<10} {str(result_products[3]):<5} {str(result_products[4]):<7} {str(result_products[5]):<20} {str(result_products[6])}", file=file)
    time.sleep(interval)
    minutes_elapsed += interval / 60

average_main = all_time_main / number_of_requests
average_products = all_time_products / number_of_requests
with open(filename, 'a') as file:
    print(f'Average for the main page:{average_main}', file=file)
    print(f'Average for the product page:{average_products}', file=file)
