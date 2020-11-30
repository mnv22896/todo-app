
from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='foo.html')),
    path('', include('todo_list.urls')),
    path('polls/', include('polls.urls')),
   # path('addTodo/', include('todo_list.urls')),
    path('admin/', admin.site.urls),
    
]
