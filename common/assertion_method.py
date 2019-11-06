# _*_ encoding: utf-8 _*_


def result_to_dict(keys, result):
    """将数据库查出的数据转换成字典列表"""
    r = []
    n = len(result)
    for i in range(n):
        r.append(dict(zip(keys, result[i])))

    return r


def compare_data_json1(data, json):
    """将数据库数据与接口返回的json进行比较，返回数据是有序的"""
    m = len(data)
    n = len(json)
    if m != n:
        raise Exception("返回数据数量不正确")
    elif n > 0:
        for i in range(n):
            compare_data_json3(data[i], json[i])


def compare_data_json2(data, json):
    """将数据库数据与接口返回的json进行比较，返回数据是无序的"""
    m = len(data)
    n = len(json)
    if m != n:
        raise Exception("返回数据数量不正确")
    elif n > 0:
        k = list(data[0].keys())[0]
        for i in range(n):
            f = 0
            for j in range(n):
                if str(data[i][k]) == str(json[j][k]):
                    f = 1
                    compare_data_json3(data[i], json[j])
                    break
            if f == 0:
                raise Exception("接口返回数据不正确")
                break


def compare_data_json3(data, json):
    for key, value in data.items():
        if (data[key] == b'\x00') or (data[key] == b'\x01'):
            a = str(bool(ord(data[key])))
        elif isinstance(data[key], str):
            a = data[key]
        else:
            a = str(data[key])

        if isinstance(json[key], str):
            b = json[key]
        else:
            b = str(json[key])

        assert a == b, ("%s不正确: a = %s, b = %s" % (key, a, b))


def assertion_fun(r):
    assert r.status_code == 200
    assert u"成功" in r.text


def remove_none(r):
    """删除字典列表中值为None的键"""
    for i in range(len(r)):
        keys = list(r[i].keys())
        for k in keys:
            if r[i][k] == None:
                del r[i][k]
