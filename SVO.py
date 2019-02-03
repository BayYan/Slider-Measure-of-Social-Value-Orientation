import csv,  math
with open('your_Qualtrics_file.csv') as input:
    reader = csv.DictReader(input)
    fieldnames = reader.fieldnames
    with open('SVO.csv', 'w') as output:
        outputFieldnames = ['WorkerID', 'SVO']
        writer = csv.DictWriter(output, outputFieldnames)
        writer.writeheader()

        for row in reader:
            #print row
            res = dict()
            sumSelf, sumOther, count = 0, 0, 0
            for fieldname in fieldnames:
                value = row[fieldname]
                if fieldname.startswith('Q3_or_your_Qualtrics_questions') or fieldname.startswith('Q73_or_your_Qualtrics_questions'):
                    if value:  
                        #value = value.replace('\r\n', '') # "\r\n is enter in Windoes"
                        #value = value.replace('<br/>', '')
                        value = value.replace('\n', '')
                        value = value.replace('\r', '')
                        value = value.replace(' ', '')
                        #print value
                        #print value
                        nums = value.split('||') 
                        #print nums
                        sumSelf += int(nums[0])
                        #print sumSelf
                        sumOther += int(nums[1])
                        #print sumOther
                        count += 1
                        #print count
            
            avgSelf = float(sumSelf) / float(count) # float is number with decimals
            avgOther = float(sumOther) / float(count)
            SVO = math.atan2(avgOther - 50, avgSelf - 50)*180/math.pi
            res['WorkerID'] = row['ResponseId']
            res['SVO'] = SVO
            #print res
            writer.writerow(res)

