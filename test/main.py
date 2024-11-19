# get data from file one line at a time
log_list = []
java_low_coverage_list = []
java_low_coverage_map = {}
with open('log.txt', encoding='utf-8') as f:
    for line in f:
        line = line.replace('\n', '').replace('report-management-service/', '')
        if line.startswith('commit'):
            log_map = {}
            log_list.append(log_map)
        elif line.startswith('Author'):
            log_map['author'] = line
        elif line.startswith('Date'):
            log_map['date'] = line[6:-2]
        else:
            if line.endswith('.java'):
                # get log_map['javaList'] value, the value is a list, if it exists add the line to it, if null create it
                if 'javaList' in log_map:
                    log_map['javaList'].append(line)
                else:
                    log_map['javaList'] = [line]



with open('coverage.txt', encoding='utf-8') as f:
    line_number = 0
    pre_line = ''
    for line in f:
        line = line.replace('\n', '')
        if line_number == 0:
            pre_line = line
            java_low_coverage_list.append(line)
            line_number += 1
        else:
            ls = line.split('\t')
            java_low_coverage_map[pre_line] = ls[0]
            line_number = 0


# check log_list.javaList in the java_low_coverage_list
invalid_list = []
for log_map in log_list:
    invalid = {}
    if 'javaList' in log_map:
        for line in log_map['javaList']:
            if line in java_low_coverage_list:
                invalid['invalidAuthor'] = log_map['author']
                invalid['invalidDate'] = log_map['date']
                if 'javaList' in invalid:
                    invalid['invalidFileAndPercentage'].append(line + '    ' + java_low_coverage_map[line])
                else:
                    invalid['invalidFileAndPercentage'] = [line + '    ' + java_low_coverage_map[line]]
    if invalid != {}:
        invalid_list.append(invalid)

# invalid_list order by author
invalid_list.sort(key=lambda x: x['invalidAuthor'])

pre_author = ''
for item in invalid_list:
    if item['invalidAuthor'] != pre_author:
        print('\n')
        print('===============================================')
        print(item['invalidAuthor'])
        print('-----------------------------------')
        pre_author = item['invalidAuthor']

    print('-----------------------------------')
    print(item['invalidDate'])
    print(item['invalidFileAndPercentage'])
    print('-----------------------------------')

# print(invalid_list)
# print(java_low_coverage_map)

# print(log_list)