import json
import os
import uuid

from django.http import HttpResponse


def index(request):
    result_json = {'success': True, 'resultCode': 200, 'data': 'tf'}
    return HttpResponse(json.dumps(result_json), content_type="application/json")


def predictions(request):
    if request.method == "POST":
        img_file = request.FILES.get("file", None)
        tmp_dir = 'D:\\workspace\\workspace-python\\plant\\tmp\\'
        path = tmp_dir + str(uuid.uuid4()) + '.' + img_file.name.split('.')[-1]

        if not img_file:
            pass
            # returnHttpResponse("no files for upload!")
        destination = open(path, 'wb+')
        for chunk in img_file.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()

    cmd = 'python D:\\workspace\\workspace-python\\tensorflow-image\\pro.py ' + path
    data = exec_cmd(cmd)
    result = json.loads(data)
    result_json = {'success': True, 'resultCode': 200, 'data': result}
    return HttpResponse(json.dumps(result_json), content_type="application/json")


def exec_cmd(cmd):
    r = os.popen(cmd)
    text = r.read()
    r.close()
    return text
