import requests
import csv
import random
import os.path
import datetime
import time
import sys
import numpy

name  = 'contest.csv'

def request_contest(concurso):
    #url = 'https://apiloterias.com.br/app/resultado?loteria=megasena&token={}'.format(token)
    url ='https://loteriascaixa-api.herokuapp.com/api/megasena/'

    concurso = concurso or 'latest' 
    url += "{}".format(concurso)

    r = requests.get(url)

    try:
        if r.status_code >= 200 and r.status_code < 400 and r.status_code != 204:
            return r.json()
        else:
            return r.status_code
    except:
        return 500


def return_double(out):
    first_number  = 0
    interval      = 0

    while True:
        first_number  = random.randint(30, 50)
        interval      = random.randint(2, 4)
        second_number =  first_number + interval

        if not (first_number in out or second_number in out):
            break

    return [ first_number, second_number ]


def build_csv_contest(json):

    if os.path.exists('./{}'.format(name)):
        change_csv_contest(json)
    else:
        build_new_csv_contest(json)


def build_new_csv_contest(json):
    csv_file    = open(name, 'w')
    new_csv     = csv.writer(csv_file)

    row = [ json['concurso'] ]
    row.extend( json['dezenas'] )
    new_csv.writerow( row )


def change_csv_contest(json):
    with open(name, 'a') as fd:
        writer = csv.writer(fd)
        row = [ json['concurso'] ]
        row.extend( json['dezenas'] )
        writer.writerow( row )


def verify_update():
    ultimate_contest = request_contest(None) 

    if os.path.exists('./{}'.format(name)):
        read = open(name, 'r')
        csv_reader = [ line.split() for line in read ] 

        number_ultimate_contest = int(ultimate_contest['concurso'])
        number_ultimate_row_csv = int(csv_reader[len(csv_reader) - 1][0].split(",")[0])

        if number_ultimate_contest > number_ultimate_row_csv:
            for n in range(number_ultimate_row_csv + 1, number_ultimate_contest + 1):
                r = request_contest(n)

                if isinstance(r, int): 
                    print('deu ruim > {}'.format(r))
                else:
                    if 'concurso' in r:
                        print('gravando jogo > {}'.format(r['concurso']))
                        change_csv_contest(r) 
                    else:
                        if 'erro' in r:
                            print('concurso inexistente')
                        else:
                            print('gravando jogo sem núermo')
                            change_csv_contest(r) 
                     
    else:
        number_ultimate_contest = ultimate_contest['concurso']
        number_ultimate_row_csv = 0

        for n in range(number_ultimate_row_csv + 1, number_ultimate_contest + 1):
            r = request_contest(n)

            if isinstance(r, int): 
                print('deu ruim > {}'.format(r))
            else:
                print('gravando jogo > {}'.format(r['concurso']))
                build_new_csv_contest(r) 
                 


def suggest_numbers():
    verify_update()

    read        = open(name, 'r')
    contests    = [ line.split() for line in read ]

    amount_second_sequence = 2 if am_num == '7' else 1
    first_sequence  = return_numbers(1, 30, 3) 
    second_sequence = return_numbers(30, 61,  amount_second_sequence)
    double          = return_double(second_sequence)

    while True:
        number_sequence = first_sequence
        number_sequence.extend(double)
        number_sequence.extend(second_sequence)

        if verify_not_exists_number_sequence(number_sequence, contests):
            break

    return numpy.sort(number_sequence)


def verify_not_exists_number_sequence(number_sequence, contests):
    for x in contests:
        account = 0

        contest = x[0].split(',')

        for number in contest:
            if int(number) in number_sequence:
                account = account + 1

                if account >= 6:
                    return False

    return True


def return_numbers(start, end, amount):
    numbers = []

    for i in range(0,amount):
        while True:
            new_number = random.randint(start, end)
            if not new_number in numbers:
                numbers.append(new_number)
                break

    return numbers 

am_num = 6
if len(sys.argv) > 1:
    am_num = sys.argv[1]

print(suggest_numbers())
