from data import com_data

url = com_data.url1 + 'systemconfigcenter/api/add-report-actor'
mobile = com_data.User.mobile1

data = {"reportedId": '10392', "informerId": '10410', "reason": "接口举报",
        "reasonImage": open('C:/Users/SuQing/Desktop/5.20.png', 'rb')}

sql = "select count(1) from report_info where informer_id = {} and reported_id = {} and reason ='接口举报' \
and process_status = 'PROCESSING' ".format(com_data.User.user1, com_data.User.user2)
