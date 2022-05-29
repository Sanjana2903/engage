from datetime import datetime


def attendance(id):
    with open('Attendance.csv', 'r+') as f:
        myDatalist = f.readlines()
        User_idList = []
        for line in myDatalist:
            entry = line.split(',')
            User_idList.append(entry[0])
        if id not in User_idList:
            now = datetime.now()
            dateString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{id},{dateString}')
            attendance(id)
