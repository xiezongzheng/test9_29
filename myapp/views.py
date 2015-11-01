#coding=utf-8   # 添加此头文件，中文注释才不会报错
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| -_- |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#          佛祖保佑       永无BUG

from django.shortcuts import render
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from myapp.models import *
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext#将context改为使用RequestContext防跨站攻击
from django.core.paginator import Paginator#分页显示
from django.http import JsonResponse
from django.db.models import Q
import json

# Create your views here.
PaginatorData=Paginator


class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())

#登录
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        uuuu = User.objects.filter(username=username,password=password)
        if uuuu:
            return HttpResponseRedirect('/index/')
    return render_to_response('login.html',context_instance=RequestContext(request))




#登录成功index页面
@csrf_exempt
def index(request):
    if request.method=='POST':
        if request.POST['sel']=="chaxun":
            return HttpResponseRedirect('/data/')
            # return render_to_response('index.html',{'username':"chaxun"},content_type=RequestContext(request))
    else:
        return render_to_response('index.html',{'username':"xiezong"},context_instance=RequestContext(request))









###########################################网站正式############################

def dataBackground(request):
    return render_to_response('dataBackground.html',{'tabNum':'0'})#tabNum=0,1,2,3控制初始进入的是哪一栏

def dataShow(request):#初始查询数据并保存到全局变量中
    b = Bactname.objects.all()
    # B = Paginator(b,20)#对查询数据进行分页
    global PaginatorData
    PaginatorData=Paginator(b,15)#对查询数据进行分页并保存到全局数据里
    # return render_to_response('dataShow.html',{'Bactname':B.page(1)})
    return HttpResponse("初始化显示数据成功")


def jqPaginator(request):#生成分页组件
    return render_to_response('jqPaginator.html',{'totalPages':PaginatorData.num_pages})



def jqPaginatorDataShow(request):#分页组件查询数据
    nowPage = request.GET.get("nowPage")

    return render_to_response('dataShow.html',{'Bactname':PaginatorData.page(nowPage)})


def searchTool(request):
    return render_to_response('searchTool.html')

def searchTool2(request):
    return render_to_response("searchTool2.html")

def searchToolQuerydata(request):
    id = request.GET.get("id")
    if id=="2":
        searchText2 = request.GET.get("searchText2")
        searchData2 = Bactname.objects.filter(type_strains__contains = searchText2)
        temp2 = Paginator(searchData2,15)
        global PaginatorData
        PaginatorData = temp2
        return HttpResponse("第二个搜索数据成功")
    if id=="1":
        searchText = request.GET.get("searchText")
        searchData = Bactname.objects.filter(Q(genus__contains = searchText) | Q(species__contains = searchText) | Q(subspecies__contains = searchText))
        temp = Paginator(searchData,15)
        global PaginatorData
        PaginatorData = temp
        return HttpResponse("第一个搜索数据成功")
    return HttpResponse("查询失败")


def detailedQuery(request):
    searchId = request.GET.get("id")
    b = Bactname.objects.get(id = searchId)
    return render_to_response('detailedQuery.html',{'genus':b.genus,'species':b.species,'subspecies':b.subspecies,'reference':b.reference,'status':b.status,'authors':b.authors,'remarks':b.remarks,'risk_grp':b.risk_grp,'type_strains':b.type_strains,'taxonid':b.taxonid,'ncbitaxonid':b.ncbitaxonid,'mclid':b.mclid,'sequence':b.sequence,'id':b.id})

def functionTab(requset):
    tabNum = requset.GET.get("tabNum")
    return render_to_response("functionTab.html",{'start':tabNum})


def separateQuery(request,dataId):#外链查询
    b = Bactname.objects.get(id = dataId)
    return render_to_response('detailedQuery.html',{'genus':b.genus,'species':b.species,'subspecies':b.subspecies,'reference':b.reference,'status':b.status,'authors':b.authors,'remarks':b.remarks,'risk_grp':b.risk_grp,'type_strains':b.type_strains,'taxonid':b.taxonid,'ncbitaxonid':b.ncbitaxonid,'mclid':b.mclid,'sequence':b.sequence,'id':b.id})

###########################################网站正式############################

def test(request):
    return render_to_response('dataBackground.html',{'tabNum':'2'})




