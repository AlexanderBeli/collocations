from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpRequest
from .add_word import Check
from .search_col_logic import search_col
import pickle


# Create your views here.
class MainPageView(TemplateView):
    template_name = 'main.html'


class SearchPageView(TemplateView):
    template_name = 'searchpage.html'


class SearchResult(ListView):
    template_name = 'resultpage.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        data = {"data":query}
        return {"query": query}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        word = context["object_list"]["query"]
        check_in = Check(word)
        # if check_in.check_w(word) == 1:
        if word != 0:

            search_res = search_col(word)
            return {"context": search_res}
        else:
            return {"context": "Please check what you wrote: " + word }

with open('pages/eng_dict.pickle', 'rb') as f:
    dict_data = pickle.load(f)
dict_list = sorted(list(dict_data))
def dict_view(response):
    #dict_list = ('grand', 'small')
    contact_list = dict_list
    paginator = Paginator(contact_list, 100)

    page_number = response.GET.get("page")
    page_obj = paginator.get_page(page_number)
    # page_extra = paginator.get_elided_page_range(page_number)
    return render(response, "dictpage.html", {'page_obj': page_obj})
# class DictView(ListView):
#     template_name = 'dictpage.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('q')
#         data = {"data": query}
#         return {"query": query}
#     def get_context_data(self, *, object_list=None, **kwargs):
#         with open('pages/eng_dict.pickle', 'rb') as f:
#             dict_data = pickle.load(f)
#
#         return {"dict_list": dict_data}

