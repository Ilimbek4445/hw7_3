import schedule, time, requests

def perform_request(url):
    try:
        response = requests.get(url).json()
        price = round(float(response['price']), 2)
        
        with open('log.txt', 'a') as log_file:
            log_file.write(f"price now: {price} $\n")

    except requests.exceptions.RequestException as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Error: {e}\n')
        
    except Exception as e:
        with open('log.txt', 'a') as log_file:
            log_file.write(f'Неожиданная ошибка: {e}\n')

def main():
    url = 'https://api.binanc.com/api/v3/avgPrice?symbol=BTCUSDT'
    
    schedule.every(3).seconds.do(perform_request, url) 
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()