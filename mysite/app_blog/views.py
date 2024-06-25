class HomePageView(ListView):
  model = Article
  template_name = 'index.html'
  context_object_name = 'categories'

 def get_context_data(self, **kwargs):
   context = super(HomePageView,
  self).get_context_data(**kwargs)
  context['articles'] =\
  Article.objects.filter(main_page=True)[:5]

  return context

 def get_queryset(self, *args, **kwargs):
   categories = Category.objects.all()

 return categories