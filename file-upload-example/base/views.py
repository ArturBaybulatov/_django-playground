from django import http
from django.views.generic import View
import os


class FileUploadView(View):
    def post(self, request, *args, **kwargs):
        base_dir = 'media'
        os.makedirs(base_dir, exist_ok=True)

        print('-------------------------');
        print(request.POST.get('metadata'));
        print('-------------------------');

        for key in request.FILES.keys():
            files = request.FILES.getlist(key)

            for file in files:
                with open(os.path.join(base_dir, file.name), 'wb') as dest:
                    for chunk in file.chunks():
                        dest.write(chunk) # `dest.write(request.body)` if single file

        return http.HttpResponse()
        #return http.HttpResponseNotFound() # Same as `raise http.Http404`
        #return http.HttpResponse(status=418) # Custom status code


# import code; code.interact(local=dict(globals(), **locals()))
