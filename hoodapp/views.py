from django.shortcuts import render,redirect,get_object_or_404
import datetime as dt

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
def create_profile_view(request):
    current_user = request.user
    profile = Profile.objects.filter(user=request.user)
    if request.method == 'POST':
            form = ProfileForm(request.POST,request.FILES,instance=current_user.profile)
        if form.is_valid():
           form.save()
        else:
        form =ProfileForm()
    return render(request,'profile/profile.html',{"form":form,"profile":profile})
def create_post_view(request):
    current_user = request.user
    # post = Post.objects.filter(hoodpro=request.user.profile.hoodpro.id)
    if request.method == 'POST':
                post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.user = current_user
            post.profile = current_user.profile
            hoodpro = current_user.profile.hoodpro
            post.save()
        return redirect('display')
            else:
        post_form =PostForm()
    return render(request,'post.html',{"post_form":post_form})
#views to display posts


#views to create business
def create_buisiness_view(request):
    current_user = request.user
    business = Business.objects.filter(hoodpro_id=request.user.profile.hoodpro.id)
    if request.method == 'POST':
        business_form = BusinessForm(request.POST, request.FILES)
        if business_form.is_valid():
            business = business_form.save(commit=False)
            business.user = current_user
            business.profile = current_user.profile
            business.save()
        return redirect('business')
    else:
        business_form = BusinessForm()
    return render(request,'bizz.html',locals())
#views to display business
def business(request):
    images = Profile.objects.all()
    business = Business.objects.all()
    return render (request,'business.html',{"business":business,"images":images})
#views for creating for creating hoodpro
def create_community(request, user_id=None):
   current_user = request.user
   ordering=['-date_posted']
   if request.method == 'POST':
       form =CommunityForm(request.POST, request.FILES)

       if form.is_valid():
           post = form.save(commit=False)
           post.user = current_user
           post.save()
           return redirect('display')
   else:
       form = CommunityForm()
   return render(request, 'community.html', {"form":form})
#searching for businesses
def search_results(request):
    if 'business_name' in request.GET and request.GET['business_name']:
        search_term = request.GET.get('business_name')
        search_businesses = Business.search_by_business_name(search_term)
        message = f"{search_term}"
        print(search_businesses)
        return render(request, 'profile/search.html',{"message":message,"biznes":search_businesses})
    else:
        message = "you havent seached for any term"
    return render(request, 'profile/search.html',{"message":message})
