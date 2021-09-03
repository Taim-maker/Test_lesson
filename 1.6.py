while True:
    days = 1
    start_km = float(input('Start res-'))
    last_km = float(input('Finish res-'))
    if start_km <= 0 or last_km < 0:
        print('input should be more 0')
    else:
        while start_km < last_km:
            start_km *= 1.1
            days += 1
    print(f'Result will come for {days} days ')