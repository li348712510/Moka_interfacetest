from common import db


# 执行前清空表格,清空相应用户id数据
# 清空DELETE FROM main_order;
# DELETE FROM sub_order;
# DELETE FROM service_record;
# DELETE FROM flow;
# DELETE FROM flow_detail;
# DELETE FROM queue;
def delete_table(userid):
    delete_main_order = "DELETE main_order,sub_order FROM main_order LEFT JOIN sub_order ON main_order.order_id=sub_order.order_id WHERE main_order.uid='{}'".format(userid)
    # delete_sub_order = "DELETE FROM sub_order "
    delete_service_record = "DELETE FROM service_record WHERE service_record.user_id='{}' ".format(userid)
    delete_flow = "DELETE flow,flow_detail FROM flow LEFT JOIN flow_detail ON flow.id=flow_detail.flow_id WHERE flow.pay_user_id='{}'".format(userid)
    # delete_flow_detail = "DELETE FROM flow_detail"
    delete_queue = "DELETE FROM queue"
    db.Mysql.other('moka', delete_main_order)
    # db.Mysql.other('moka', delete_sub_order)
    db.Mysql.other('moka', delete_service_record)
    db.Mysql.other('moka', delete_flow)
    # db.Mysql.other('moka', delete_flow_detail)
    db.Mysql.other('moka', delete_queue)






