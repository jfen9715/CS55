from django.http import HttpResponseRedirect, JsonResponse
from django.views import generic
from django.utils import timezone
from .models import User


def read_data(request):  # convert data from Http Request to python dictionary
    user_data = {}
    for key in request.POST.keys():
        user_data[key] = request.POST.get(key, None)

    return user_data


def save_data(user_email, user_data):  # save data from Http Request to database
    user = User.objects.get(user_email=user_email)
    # if no selected data, means the input data is empty, do not need to write to database
    if user_data['current'] == '0' and user_data['module1_advantages'] == '' \
            and user_data['module1_obstacles'] == '':
        return False

    # write data to database
    user.userdata_set.create(
        before_test=user_data['before_test'],
        module1_advantages=user_data['module1_advantages'],
        module1_obstacles=user_data['module1_obstacles'],
        module1_extra=user_data['module1_extra'],
        module2_selections=user_data['module2_selections'],
        module2_extra_need=user_data['module2_extra_need'],
        module3_selections=user_data['module3_selections'],
        module3_extra_value=user_data['module3_extra_value'],
        module4_selections_1=user_data['module4_selections_1'],
        module4_selections_2=user_data['module4_selections_2'],
        module5_personal=user_data['module5_personal'],
        module5_work=user_data['module5_work'],
        module5_personal_selections=user_data['module5_personal_selections'],
        module5_work_selections=user_data['module5_work_selections'],
        module6_selections=user_data['module6_selections'],
        finished=user_data['finished'],
        current=user_data['current'],
        after_test=user_data['after_test'],
        date=timezone.now()
    )

    return True


class Login(generic.View):  # handle the login operation
    def get(self):
        return HttpResponseRedirect('/login')

    def post(self, request):
        request_data = read_data(request)  # read data from request
        user_password = request_data['user_password']
        user_email = request_data['user_email']

        print('---------user login---------')
        print('user email:' + user_email)

        try:
            user = User.objects.get(user_email=user_email)
            finished = True
            if len(user.userdata_set.all()) == 0:
                finished = True
            else:
                user_data = user.userdata_set.all().latest('date')  # get latest record
                if user_data.current < 6:
                    finished = False

            if user.user_password == user_password:  # if user exist and password is correct

                r = {
                    'status': 0,
                    'msg': 'Login Successfully!',
                    'finished': finished
                }
                response = JsonResponse(r)

                return response
            else:  # else password is wrong
                r = {
                    'status': 1,
                    'msg': 'Wrong Password!'
                }
                response = JsonResponse(r)
                return response

        except Exception as e:  # when user do not exist

            print(e)

            r = {
                'status': 2,
                'msg': 'Email incorrect!'
            }

            return JsonResponse(r)


class Register(generic.View):  # handle the register operation
    def get(self):
        return HttpResponseRedirect('/login')

    def post(self, request):
        request_data = read_data(request)
        user_name = request_data['user_name']
        user_password = request_data['user_password']
        user_email = request_data['user_email']

        print('---------user register---------')
        print('user email:' + user_email)

        if len(user_password) > 20:
            r = {
                'status': 2,
                'msg': 'Password Should Not Longer Than 20 Characters!'
            }
            return JsonResponse(r)

        if len(user_name) > 20:
            r = {
                'status': 2,
                'msg': 'User Name Should Not Longer Than 20 Characters!'
            }
            return JsonResponse(r)

        if len(user_email) > 20:
            r = {
                'status': 2,
                'msg': 'Email Address Should Not Longer Than 20 Characters!'
            }
            return JsonResponse(r)

        try:
            user = User(user_name=user_name, user_password=user_password, user_email=user_email)  # try to create user
            user.save()

            r = {
                'status': 0,
                'msg': 'Signup Successfully!'
            }
            return JsonResponse(r)

        except Exception as e:  # when create user unsuccessful
            print(e)
            r = {
                'status': 1,
                'msg': 'Email Already Exist!'
            }
            return JsonResponse(r)


class Save(generic.View):  # handle the operation when user already login and want to save the data
    def get(self):
        return HttpResponseRedirect('/login')

    def post(self, request):
        request_data = read_data(request)
        user_email = request_data['user_email']

        print('---------user save---------')
        print('user email:' + user_email)

        try:
            user = User.objects.get(user_email=user_email)
            if request_data['continue'] == 'true':  # if continue to do the modules, update by deleting the old data
                user_data = user.userdata_set.all().latest('date')  # get latest record
                print('---------updating user data---------')
                print('user email:' + user_email)
                if save_data(user_email, request_data):
                    user_data.delete()
                else:
                    print('---------update failed: empty new data---------')
                    print('user email:' + user_email)
            else:
                save_data(user_email, request_data)

            r = {
                'status': 0,
                'msg': 'Save Successfully！'
            }
            response = JsonResponse(r)
            return response

        except Exception as e:

            print(e)

            r = {
                'status': 1,
                'msg': 'Please Login Again'
            }

            return JsonResponse(r)


class GetUserData(generic.View):  # return user data to front-end
    def get(self):
        return HttpResponseRedirect('/login')

    def post(self, request):
        user_email = request.POST.get('user_email', None)

        print('---------user get data---------')
        print('user email:' + user_email)

        try:
            user = User.objects.get(user_email=user_email)

            if len(user.userdata_set.all()) == 0:
                r = {
                    'state': 0,
                    'msg': 'No Record Exist'
                }
                print('---------empty dataset---------')
                print(r)

                return JsonResponse(r)
            else:
                user_data = user.userdata_set.all().latest('date')  # get latest record
                user_data_dist = dict(user_data.__dict__)  # convert object to dict for Json response
                user_data_dist['state'] = '1'
                del user_data_dist['_state']
                del user_data_dist['id']
                del user_data_dist['user_id']
                del user_data_dist['date']
                user_data_dist['date'] = str(user_data.date.day) + '/' + str(user_data.date.month) + '/' + str(
                    user_data.date.year)
                user_data_dist['user_email'] = user_data.user.user_email

            print('---------return dataset---------')
            print(user_data_dist)

            return JsonResponse(user_data_dist)

        except Exception as e:

            print(e)

            r = {
                'msg': 'Please Login Again'
            }

            return JsonResponse(r)
