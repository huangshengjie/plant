from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from application.models import *


class LoginMiddleware(MiddlewareMixin):

    @staticmethod
    def process_request(request):
        # 设置需要经过登录验证过滤的URL
        urls = [
            '/plant/user_center/',
            '/plant/new_plant/',
            '/plant/new_gallery/',
            '/plant/user_update/',
            '/plant/news/',
            '/plant/news_content/',
            '/plant/notify/',
            '/plant/notify_content/',
            '/plant/rank/',
            '/plant/gallery/'
        ]

        filter_url = False
        for url in urls:
            if request.path == url:
                filter_url = True
                break

        is_login = True
        if filter_url is True:
            user_id = request.COOKIES.get('user_id', None)
            if user_id is not None:
                has_user = User.objects.filter(id=user_id).first()
                if has_user is not None:
                    is_login = True
                else:
                    is_login = False
            else:
                is_login = False

        if is_login is True:
            pass
        else:
            return HttpResponseRedirect('/plant/account/')
