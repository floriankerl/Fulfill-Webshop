from django.contrib.auth import login as authorize_login
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from .forms import MySignUpForm, MyEditUpForm, MyExtendedUpForm, MyProfilePictureEditForm
from .models import ExtendedUser, get_extended_user_from_user
from django.contrib.auth.decorators import login_required


class MyLoginView(LoginView):
    template_name = 'registration/login.html'

    def form_valid(self, form):
        authorize_login(self.request, form.get_user())
        user = form.get_user()
        extended_user = get_extended_user_from_user(user)
        if extended_user is not None:  # users are only saved after they logged in after creating account
            extended_user.execute_after_login()

        return HttpResponseRedirect(self.get_success_url())


class MySignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

    def form_valid(self, form):
        data = form.cleaned_data
        user = User.objects.create_user(username=data['username'],
                                        password=data['password'],
                                        first_name=data['first_name'],
                                        last_name=data['last_name'],
                                        email=data['email'],
                                        )

        if data['profile_picture'] == None:
            profile_picture = 'profile-pictures/user_icon.png'
        else:
            profile_picture = data['profile_picture']

        extended_user = ExtendedUser.objects.create(user=user,
                                                    date_of_birth=data['date_of_birth'],
                                                    profile_picture=profile_picture,
                                                    gender=data['gender'],
                                                    street=data['street'],
                                                    house_number=data['house_number'],
                                                    plz=data['plz'],
                                                    city=data['city'],
                                                    mobile_number=data['mobile_number']
                                                    )

        return redirect('/')


@login_required(login_url='/useradmin/login')
def user_profile(request):
    extended_user = get_extended_user_from_user(request.user)
    full_name = extended_user.get_full_name_of_user()
    address = extended_user.get_address_of_user()

    # if extended_user.profile_picture.url not None

    context = {
        'extended_user': extended_user,
        'address': address,
        'full_name': full_name
    }
    return render(request, 'user-profile.html', context)


def edit_user_profile(request, user_id: str):
    user = User.objects.get(id=int(user_id))
    extended_user = get_extended_user_from_user(user)
    user_form = MyEditUpForm(request.POST or None, instance=user)
    extended_user_form = MyExtendedUpForm(request.POST or None, instance=extended_user)
    profile_picture_form = MyProfilePictureEditForm(request.POST or None, request.FILES, instance=extended_user)
    context = {'user_form': user_form, 'extended_user_form': extended_user_form, 'profile_picture_form': profile_picture_form}
    contentOfPage = render(request, 'user-profile-edit.html', context)

    if user_form.is_valid() and extended_user_form.is_valid() and profile_picture_form.is_valid():
        user_form.save()
        new_extended_user = extended_user_form.save(commit=False)
        data = profile_picture_form.cleaned_data
        if data['profile_picture'] == False:
            profile_picture = 'profile-pictures/user_icon.png'
        else:
            profile_picture = data['profile_picture']
        print(data['profile_picture'])
        new_extended_user.profile_picture = profile_picture
        extended_user_form.save()
        return redirect('user-profile')
    return contentOfPage



