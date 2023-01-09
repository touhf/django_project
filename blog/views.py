from django.views import generic
from .forms import CommentForm, ImageForm
from .models import Post, Image
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
# Create your views here.

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})


class AboutPageView(TemplateView):
    template_name = "about.html"


def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            # getting the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'index.html', {'form':form, 'img_obj': imb_obj})
        else:
            form = ImageForm()
        
        return render(request, 'index.html', {'form':form})
