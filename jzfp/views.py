from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Person
from django.db.models import Q
# Create your views here.

# 未使用，注释掉
# def index(request):
#     person_list = Person.objects.order_by('sn')
#     template = loader.get_template('jzfp/index.html')
#     context = {'person_list': person_list, }
#     return HttpResponse(template.render(context, request))


def detail(request, id_num):
    person = get_object_or_404(Person, pk=id_num)
    return render(request, 'jzfp/detail.html',
                  {'person': person})


def search_form(request):
    return render_to_response('jzfp/search.html')


def search(request):
    errmsg = []
    request.encoding = 'utf-8'
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errmsg.append('提交内容为空')
        elif len(q) > 20:
            errmsg.append('输入字符串超长')
        else:
            person_list = Person.objects.filter(Q(id_num__contains=request.GET['q']) | Q(name__icontains=request.GET['q']))
            template = loader.get_template('jzfp/index.html')
            context = {'person_list': person_list, }
            return HttpResponse(template.render(context, request))
        return render_to_response('jzfp/search.html', {'errmsg': errmsg})
