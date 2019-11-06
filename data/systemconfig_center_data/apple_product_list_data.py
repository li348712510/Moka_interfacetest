from data import com_data

url = com_data.url1 + 'systemconfigcenter/api/apple-product-list'
mobile = com_data.User.mobile1

sql = "select money, ios_product_id, cast(gold_amount as char) from money_gold \
where plant='IOS' and package_name='com.yequ' ORDER BY  cast(money as DECIMAL)"

keys = ('money', 'productId', 'goldAmount')