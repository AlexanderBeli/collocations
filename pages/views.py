from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.http import HttpResponse, HttpRequest
from .add_word import Check
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
            with open('pages/eng_dict.pickle', 'rb') as f:
                dict_data = pickle.load(f)

            coll_data_result = ""

            for i in sorted(list(dict_data)):
                if i == word:
                    # print(f"{i} is {word} in dict")
                    # 13.10.2023 {'n + n_after', 'adv + v', 'adj + n', 'v + n', 'adj + n_after', 'n + n', 'adv + adj', 'adj + v', 'phr_v + n_after', 'n + v', 'v + n_after', 'phr_v + n'}
                    # 14.10.2023 {'abbreviation unknown + abbreviation unknown', 'abbreviation unknown + n', 'phr_v + n_after', 'phr_v + abbreviation unknown', 'abbreviation unknown + n_after', 'abbreviation unknown + v', 'phr_v + n', 'abbreviation unknown + adj'}
                    for k in dict_data[i].keys():
                        for o in dict_data[i][k]:
                            if o == 'collocations':
                                for l in dict_data[i][k][o].keys():
                                    if k == 'adj' and l == 'n':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'v' and l == 'n':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'n' and l == 'v':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'phr_v' and l == 'n':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'adv' and l == 'v':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'adv' and l == 'adj':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'n' and l == 'n':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'n' and l == 'n_after':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'adj' and l == 'n_after':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'v' and l == 'n_after':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'phr_v' and l == 'n_after':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'abbreviation unknown' and l == 'abbreviation unknown':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'abbreviation unknown' and l == 'n':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'phr_v' and l == 'abbreviation unknown':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'abbreviation unknown' and l == 'n_after':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    # {'phr_v + n', 'phr_v + n_after', 'adv + v', 'abbreviation unknown + n_after', 'adv + adj', 'abbreviation unknown + n'}
                                    if k == 'n' and l == 'adj':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'n' and l == 'v_after':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'n' and l == 'prep':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'n' and l == 'phrases':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + ': ' + n + ", "
                                    if k == 'adj' and l == 'v_after':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'adj' and l == 'adv':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'adj' and l == 'prep':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'adj' and l == 'phrases':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + ': ' + n + ", "
                                    if k == 'v' and l == 'adv':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'v' and l == 'v_after':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + n + " " + word + ", "
                                    if k == 'v' and l == 'prep':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + " " + n + ", "
                                    if k == 'v' and l == 'phrases':
                                        for n in sorted(list(dict_data[i][k][o][l])):
                                            coll_data_result = coll_data_result + word + ': ' + n + ", "
                # if i != word:
                for k in dict_data[i].keys():
                    for o in dict_data[i][k]:
                        if o == 'collocations':
                            for l in dict_data[i][k][o].keys():
                                if word in tuple(dict_data[i][k][o][l]):
                                    if k == 'adj' and l == 'n':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'v' and l == 'n':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'n' and l == 'v':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'phr_v' and l == 'n':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'adv' and l == 'v':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'adv' and l == 'adj':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'n' and l == 'n':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'n' and l == 'n_after':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'adj' and l == 'n_after':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'v' and l == 'n_after':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'phr_v' and l == 'n_after':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'abbreviation unknown' and l == 'abbreviation unknown':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'abbreviation unknown' and l == 'n':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'phr_v' and l == 'abbreviation unknown':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'abbreviation unknown' and l == 'n_after':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    # 13.10.2023 {'n + n_after', 'adv + v', 'adj + n', 'v + n', 'adj + n_after', 'n + n', 'adv + adj', 'adj + v', 'phr_v + n_after', 'n + v', 'v + n_after', 'phr_v + n'}
                                    if k == 'n' and l == 'adj':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'n' and l == 'v_after':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'n' and l == 'prep':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'n' and l == 'phrases':
                                        coll_data_result = coll_data_result + word + ': ' + i + ", "
                                    if k == 'adj' and l == 'v_after':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'adj' and l == 'adv':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'adj' and l == 'prep':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'adj' and l == 'phrases':
                                        coll_data_result = coll_data_result + word + ': ' + i + ", "
                                    if k == 'v' and l == 'adv':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'v' and l == 'v_after':
                                        coll_data_result = coll_data_result + word + " " + i + ", "
                                    if k == 'v' and l == 'prep':
                                        coll_data_result = coll_data_result + i + " " + word + ", "
                                    if k == 'v' and l == 'phrases':
                                        coll_data_result = coll_data_result + word + ': ' + i + ", "
            return {"context": coll_data_result}
        else:
            return {"context": "Please check what you wrote: " + word }

