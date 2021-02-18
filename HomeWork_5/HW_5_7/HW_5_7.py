import json
with open('firm_statistics.txt', 'r', encoding='utf-8') as firm:
    # for line in firm:
        profit = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in firm}
        # print(profit)
        # if profit_count > 0:
        #    profit = {line.split()[0]: profit_count}
        # print(len(profit))
        for_upload = ([profit, {'average': sum((int(value) for value in profit.values() if int(value) > 0)) / len(profit)}])
        # print(for_upload)
with open('upload_statistics', 'w', encoding='utf-8') as upload:
    json.dump(for_upload, upload, ensure_ascii=False, indent=4)

