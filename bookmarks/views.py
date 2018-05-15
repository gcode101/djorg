from django.shortcuts import render
from .forms import BookmarkForm
from .models import Bookmark, PersonalBookmark

def index(request):
	# break point used for debuging
	# import pdb; pdb.set_trace()
	if request.method == 'POST':
		form = BookmarkForm(request.POST)
		if form.is_valid():
			form.save()
	context = {}
	context['bookmarks'] = Bookmark.objects.exclude(id__in=PersonalBookmark.objects.values_list('id'))
	if request.user.is_anonymous:
		context['personal_bookmarks'] = PersonalBookmark.objects.none()
	else:
		context['personal_bookmarks'] = PersonalBookmark.objects.filter(user=request.user)
	context['form'] = BookmarkForm()
	return render(request, 'bookmarks/index.html', context)
