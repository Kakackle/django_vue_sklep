from sklep.models import Review, Product
from django.contrib.auth.models import User
from sklep.api.serializers import ReviewSerializer
from sklep.api.pagination import CustomPagination

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django_filters import CharFilter, BooleanFilter, ChoiceFilter, NumberFilter

from django.http import JsonResponse

class ReviewFilters(FilterSet):
    product = CharFilter(field_name='product__slug', lookup_expr='contains')
    author = CharFilter(field_name='author__username', lookup_expr='iexact')

    class Meta:
        model = Review
        fields = ['product__slug', 'author__username']

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = CustomPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ReviewFilters
    permission_classes = (IsAuthenticatedOrReadOnly,) 

    def post(self, request, *args, **kwargs):
        print('received request: ', request.data)
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            print('serializer errors: ', serializer.errors)
    
    def perform_create(self, serializer):
        product_slug = self.request.data.get('product')
        product = Product.objects.get(slug=product_slug)
        author_username = self.request.data.get('author')
        author = User.objects.get(username=author_username)
        serializer.save(product=product, author=author)

        product_ratings = list(product.reviews.all().values_list('rating', flat=True))
        product.rating_average = sum(product_ratings)/len(product_ratings)
        product.save()


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'slug'
    permission_classes = (IsAuthenticatedOrReadOnly,) 

class ReviewLikeAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,) 
    lookup_field = 'slug'

    def patch(self, request, *args, **kwargs):
        print('update request data:', self.request.data)
        return self.partial_update(request, *args, **kwargs)
    
    def perform_update(self, serializer):
        # print('update request data:', self.request.data)
        # post wybrany przez endpoint
        review_slug = self.kwargs.get('slug')
        review = Review.objects.get(slug=review_slug)
        
        user_slug = self.request.data.get('user')
        user = User.objects.get(username=user_slug)
        
        if user not in review.liked_by.all():
            review.liked_by.add(user)
            review.like_count +=1
            review.save()
        else:
            review.liked_by.remove(user)
            review.like_count -=1
            review.save()

        liked_by_names = list(review.liked_by.all().values_list('username', flat=True))

        return JsonResponse({'liked_by': liked_by_names, 
                             'message': 'liked_by changed'},status=200)