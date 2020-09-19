from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RouterDetails
from .serializers import RouterSerializer
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RouterForm
from django.views.generic import ListView, DetailView


class RouterView(APIView):
    def get(self, request):
        route_data = RouterDetails.objects.all()
        serializer = RouterSerializer(route_data, many=True)
        return Response({"route_data": serializer.data})

    def post(self, request):
        route_data = request.data.get('route_data')

        # Create an article from the above data
        serializer = RouterSerializer(data=route_data)
        if serializer.is_valid(raise_exception=True):
            route_saved = serializer.save()
        return Response({"success": "Router Detail '{}' created successfully".format(route_saved.Host_name)})

    def put(self, request, pk):
        saved_router = get_object_or_404(RouterDetails.objects.all(), pk=pk)
        data = request.data.get('route_data')
        serializer = RouterDetails(instance=saved_router, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            router_saved = serializer.save()
        return Response({"success": "Article '{}' updated successfully".format(router_saved.Host_name)})

    def delete(self, request, pk):
        # Get object with this pk
        router = get_object_or_404(RouterDetails.objects.all(), pk=pk)
        router.delete()
        return Response({"message": "Route with id `{}` has been deleted.".format(pk)}, status=204)


class IndexView(ListView):
    template_name = 'app1/index.html'
    context_object_name = 'router_list'

    def get_queryset(self):
        return RouterDetails.objects.all()


class RouterDetailsView(DetailView):
    model = RouterDetails
    template_name = 'app1/router-detail.html'


def create(request):
    if request.method == 'POST':
        form = RouterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    form = RouterForm()

    return render(request, 'app1/create.html', {'form': form})


def edit(request, pk, template_name='app1/edit.html'):
    router = get_object_or_404(RouterDetails, pk=pk)
    form = RouterForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, template_name, {'form': form})


def delete(request, pk, template_name='app1/confirm_delete.html'):
    router = get_object_or_404(RouterDetails, pk=pk)
    if request.method == 'POST':
        router.delete()
        return redirect('index')
    return render(request, template_name, {'object': router})
