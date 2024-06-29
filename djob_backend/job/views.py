from rest_framework import status, authentication, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job, Category
from .serializers import JobSerializer, JobDetailSerializer, CategorySerializer
from .forms import JobForm


class CategoriesView(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)

        return Response(serializer.data)

class NewestJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()[0:4]
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)

class MyJobsView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        jobs = Job.objects.filter(created_by=request.user)

        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)
    
class CreateJobView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        form = JobForm(request.data)

        if form.is_valid():
            job = form.save(commit=False)
            job.created_by = request.user
            job.save()

            return Response({'status': 'created'})
        return Response({'status': 'errors', 'errors': form.errors})
    
class BrowseJobsView(APIView):
    def get(self, request, format=None):
        jobs = Job.objects.all()
        categories = request.GET.get('categories', '')
        query = request.GET.get('query', '')

        if query:
            jobs = jobs.filter(title__icontains=query)

        if categories:
            jobs = jobs.filter(category_id__in=categories.split(','))
        
        serializer = JobSerializer(jobs, many=True)

        return Response(serializer.data)

class JobsDetailView(APIView):
    def get(self, request, pk, format=None):

        job = Job.objects.get(pk=pk)
        print(job)
        serializer = JobDetailSerializer(job)
        return Response(serializer.data)
        
