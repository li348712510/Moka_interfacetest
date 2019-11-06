from data import com_data

url = com_data.url1 + 'systemconfigcenter/api/gold-list-setting'
mobile = com_data.User.mobile1

sql = "select money, cast(gold_amount - money*100 as char), cast(money*100 as char) from money_gold \
where plant='Android' ORDER BY  cast(money as DECIMAL)"

keys = ('money', 'rewardAmount', 'goldAmount')
