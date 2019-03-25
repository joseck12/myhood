from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
def display(request):
    images = Profile.objects.all()
    try:
        hoodpro_id = get_object_or_404(hoodpro,pk=request.user.profile.hoodpro.id)

        photo = hoodpro.objects.get(pk=request.user.profile.location.id)
        photos = Post.objects.filter(hoodpro=photo)
        post = hoodpro.objects.get(pk=request.user.profile.hoodpro.id)
        posts = Post.objects.filter(hoodpro=post)
    except:
        message='create neighbourhood'
    return render (request,'home.html',locals())
