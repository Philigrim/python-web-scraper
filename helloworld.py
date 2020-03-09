#!/usr/bin/env python
import sys

from collections import Counter
from collections import defaultdict

if __name__ == '__main__':

    def print_arguments_error(parameter_no):
        print('Incorrectly specified command line arguments.')
        if parameter_no == 'all':
            print('Arguments must contain 3 (or 4) parameters.')
        elif parameter_no == 1:
            print('First parameter should include input file name')
        elif parameter_no == 2:
            print('Second parameter should specify group type. (\"ip\" or \"http\")')
        elif parameter_no == 3:
            print('Third parameter should indicate function number. (\"1\", \"2\" or \"3\")')
        exit()

    def read_file(filename):
        try:
            with open(filename, 'r') as file:
                data = file.readlines()
        except IOError:
            print('File not found.')
            print_arguments_error(1)
            exit()
        if not data:
            print("File is empty.")
            exit()
        return data

    def get_column_from_log(list, word_number):
        column_as_list = []
        for line in list:
            column_as_list.append(line.split(" ")[word_number])
        print(column_as_list)
        return column_as_list

    def request_count(list):
        return(Counter(list))

    def request_count_percentage(list):
        ip_or_http_frequency = request_count(list)
        no_of_all_logged_requests = sum(ip_or_http_frequency.values())
        
        for ip_or_http in ip_or_http_frequency:
            ip_or_http_frequency[ip_or_http] = round(ip_or_http_frequency[ip_or_http]/no_of_all_logged_requests*100, 2)
            
        return ip_or_http_frequency

    def calculate_bytes(ip_or_http_list, bytes):
        ip_or_http_and_bytes = defaultdict(list)
        x=0
        for ip_or_http in ip_or_http_list:
            if bytes[x] != "-":
                ip_or_http_and_bytes[ip_or_http_list[x]].append(int(bytes[x]))
            x+=1

        for ip_or_http in ip_or_http_and_bytes:
            ip_or_http_and_bytes[ip_or_http] = sum(ip_or_http_and_bytes[ip_or_http])

        return ip_or_http_and_bytes
    
    def printing_result(results, limit):
        print(sorted(results.items(), key=lambda x: x[1], reverse=True)[:limit])

    def main():

        if len(sys.argv) != 4 and len(sys.argv) != 5:
            print_arguments_error('all')
        
        if len(sys.argv) == 5:
            limit = int(sys.argv[4])
        else:
            limit = None

        loglist = read_file(sys.argv[1])

        if sys.argv[2] == "ip":
            ip_or_http_list = get_column_from_log(loglist, 0)
        elif sys.argv[2] == "http":
            ip_or_http_list = get_column_from_log(loglist, 8)
        else:
            print_arguments_error(2)

        if sys.argv[3] == "1":
            ip_or_http_counted = request_count(ip_or_http_list)
            printing_result(ip_or_http_counted, limit)
        elif sys.argv[3] == "2":
            ip_or_http_count_percentage = request_count_percentage(ip_or_http_list)
            printing_result(ip_or_http_count_percentage, limit)
        elif sys.argv[3] == "3":
            bytes = get_column_from_log(loglist, 9)
            ip_or_http_and_bytes = calculate_bytes(ip_or_http_list, bytes)
            printing_result(ip_or_http_and_bytes, limit)
        else:
            print_arguments_error(3)
    
    main()