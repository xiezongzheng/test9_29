#coding=utf-8   # 添加此头文件，中文注释才不会报错
from django.conf.urls import patterns, include, url
from django.contrib import admin
from myapp.views import *
from django.conf import settings



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test9_29.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
                       (r'^login/$',login),
                       (r'^index/$',index),
                        (r'^dict/$',dict),
                       ######################网站正式#######################
                       (r'^dataBackground/$',dataBackground),
                       (r'^dataShow/$',dataShow),
                       (r'^jqPaginator/$',jqPaginator),
                       (r'^jqPaginatorDataShow/$',jqPaginatorDataShow),
                       (r'^searchTool/$',searchTool),
                       (r'^searchTool2/$',searchTool2),
                       (r'^searchToolQuerydata/$',searchToolQuerydata),
                       (r'^detailedQuery/$',detailedQuery),

                       ######################################################
                       (r'^functionTab/$',functionTab),
    url(r'^admin/', include(admin.site.urls)),
)

# if settings.DEBUG:
#          import debug_toolbar
#         urlpatterns += patterns('',
#             url(r'^__debug__/', include(debug_toolbar.urls)),
#         )
