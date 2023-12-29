def check_seat(num_of_seat):
    result = []
    if num_of_seat == '1':
        return ['poor conductor']
    else:
        if len(num_of_seat) == 1:
            num_of_seat = '0'+num_of_seat
        if num_of_seat[-1] == '1':
            seat = int(num_of_seat[:-1]) * 2
            result.append(f'{seat} W L')
        if num_of_seat[-1] == '2':
            seat = int(num_of_seat[:-1]) * 2 + 1
            result.append(f'{seat} W L')

        if num_of_seat[-1] == '0':
            seat = int(num_of_seat[:-1]) * 2
            result.append(f'{seat} A L')
        if num_of_seat[-1] == '3':
            seat = int(num_of_seat[:-1]) * 2 + 1
            result.append(f'{seat} A L')

        if num_of_seat[-1] == '4':
            seat = int(num_of_seat[:-1]) * 2 + 1
            result.append(f'{seat} A R')
        if num_of_seat[-1] == '9':
            seat = int(num_of_seat[:-1]) * 2 + 2
            result.append(f'{seat} A R')

        if num_of_seat[-1] == '5':
            seat = int(num_of_seat[:-1]) * 2 + 1
            result.append(f'{seat} M R')
        if num_of_seat[-1] == '8':
            seat = int(num_of_seat[:-1]) * 2 + 2
            result.append(f'{seat} M R')

        if num_of_seat[-1] == '6':
            seat = int(num_of_seat[:-1]) * 2 + 1
            result.append(f'{seat} W R')
        if num_of_seat[-1] == '7':
            seat = int(num_of_seat[:-1]) * 2 + 2
            result.append(f'{seat} W R')
        return result


test_case = int(input())
numbers_of_seats = [input() for _ in range(test_case)]
for num in numbers_of_seats:
    r = check_seat(num)
    print(*r)
