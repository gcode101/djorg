from django.shortcuts import render
from .models import Bookmark, PersonalBookmark

def index(request):
	context = {}
	context['bookmarks'] = Bookmark.objects.exclude(id__in=PersonalBookmark.objects.values_list('id'))
	if request.user.is_anonymous:
		context['personal_bookmarks'] = PersonalBookmark.objects.none()
	else:
		context['personal_bookmarks'] = PersonalBookmark.objects.filter(user=request.user)
	return render(request, 'bookmarks/index.html', context)
