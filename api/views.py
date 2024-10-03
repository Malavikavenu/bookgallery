from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from api.models import Books,Review

from rest_framework import viewsets

from api.serializers import BookSerializer,ReviewSerializer

from rest_framework.decorators import action

from rest_framework import authentication,permissions

from rest_framework import generics

class BookListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Books.objects.all()

        serializer_instance=BookSerializer(qs,many=True)

        # print(serializer_instance)

        return Response(data=serializer_instance.data)


    def post(self,request,*args,**kwargs):

        serializer_instance=BookSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors) #return errror if validation is fail



        

#get-detail, put-update ,
class BookRetrieveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Books.objects.get(id=id) #type->Query set

        serializer_instance=BookSerializer(qs) #serialize


        return Response(data=serializer_instance.data)
    
    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        book_obj=Books.objects.get(id=id)

        serializer_instance=BookSerializer(data=request.data,instance=book_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:
            return Response(data=serializer_instance.errors)
        

       
       
    
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("pk")

        qs=Books.objects.get(id=id).delete()

        data={"message":"deleted"}

        return Response(data)
    

#ViewSet

class BookViewSetView(viewsets.ViewSet):

    authentication_classes=[authentication.BasicAuthentication]

    permission_classes=[permissions.IsAuthenticatedOrReadOnly]

    

   


    #list()
    # create()
    # retrieve()
    # update()
    # destroy()

#list()
    def list(self,request,*args,**kwargs):

        qs=Books.objects.all()

        serializer_instance=BookSerializer(qs,many=True) #query-> python native

        return Response(data=serializer_instance.data)

#create()

    def create(self,request,*args,**kwargs):

        serializer_instance=BookSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
#retrieve()

    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Books.objects.get(id=id)

        serializer_instance=BookSerializer(qs)

        return Response(data=serializer_instance.data)
    
#update()

    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        book_object=Books.objects.get(id=id)
        
        serializer_instance=BookSerializer(data=request.data,instance=book_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        
             
#destroy()

    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Books.objects.get(id=id).delete()

        data={"message":"deleted"}

        return Response(data=data)
    
    @action(methods=["GET"],detail=False)
    def genre_list(self,request,*args,**kwargs):

        genres=Books.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=genres)
    

    @action(methods=["GET"],detail=False)
    def authors_list(self,request,*args,**kwargs):

        authors=Books.objects.all().values_list("author",flat=True).distinct()

        return Response(data=authors)
    
    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):

        book_id=kwargs.get("pk")

        book_obj=Books.objects.get(id=book_id)

        serializer_instance=ReviewSerializer(data=request.data)

        if serializer_instance.is_valid():

            serializer_instance.save(book_object=book_obj)

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)



   


class GenreListView(APIView):

    def get(self,request,*args,**kwargs):

        genres=Books.objects.all().values_list("genre",flat=True).distinct()

        return Response(data=genres)


class AuthorListView(APIView):

    def get(self,request,*args,**kwargs):

        author=Books.objects.all().values_list("author",flat=True).distinct()

        return Response(data=author)


class ReviewUpdateDestroyViewSetView(viewsets.ViewSet):

    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Review.objects.get(id=id).delete()

        data={"message":"review deleted"}

        return Response(data)
    
    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        review_object=Review.objects.get(id=id)

        serializer_instance=ReviewSerializer(data=request.data,instance=review_object)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)
        

    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Review.objects.get(id=id)

        serializer_instance=ReviewSerializer(qs)

        return Response(data=serializer_instance.data)


#generic class

class BookListView(generics.ListAPIView):

    serializer_class=BookSerializer

    queryset=Books.objects.all()


class BookRetriUpDestroyView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class=BookSerializer

    queryset=Books.objects.all()






        
