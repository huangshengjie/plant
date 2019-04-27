import json
import logging

from django.http import HttpResponse
from django.db import connection


logger = logging.getLogger('app.log')


# 打印日志
def debug(message):
    logger.info(message)


def index(request):
    result_json = {'success': True, 'resultCode': 200, 'data': ''}
    return HttpResponse(json.dumps(result_json), content_type="application/json")


def update_user(request):
    body = request.body
    json_data = json.loads(body.decode())

    id = json_data['id']
    name = json_data['name']
    password = json_data['password']
    email = json_data['email']
    phone = json_data['phone']

    with connection.cursor() as cursor:
        sql = "UPDATE user SET name = '%s', password = '%s', email = '%s', phone = '%s' WHERE id = %d" \
              % (name, password, email, phone, id)
        debug('daniel'+sql)
        cursor.execute(sql)
        sql_result = cursor.rownumber

    if sql_result != -1:
        return convert_result(True, 200, '修改成功')
    else:
        return convert_result(False, 400, '修改失败')


def convert_result(success, result_code, data):
    result_json = {'success': success, 'resultCode': result_code, 'data': data}
    return HttpResponse(json.dumps(result_json), content_type="application/json")
