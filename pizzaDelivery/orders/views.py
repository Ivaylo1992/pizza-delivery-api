from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import generics as views, status
from rest_framework.response import Response

from .models import Order
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser

from PizzaDelivery.orders.serializers import OrderCreationSerializer, OrderDetailSerializer, StatusUpdateSerializer

UserModel = get_user_model()

class OrderCreateListView(views.GenericAPIView):
    serializer_class = OrderCreationSerializer
    queryset = Order.objects.all()

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        orders = Order.objects.all()

        serializer = self.serializer_class(
            orders,
            many=True
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)

            return Response(
                data=serializer.data,
                status=status.HTTP_201_CREATED
            )
        
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )

class OrderDetailView(views.GenericAPIView):
    serializer_class = OrderDetailSerializer

    permission_classes = [IsAdminUser]
    
    def get(self, request, order_id):
        order=get_object_or_404(Order, pk=order_id)

        serializer = self.serializer_class(instance=order)

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )
    
    def put(self, request, order_id):
        data = request.data

        order = get_object_or_404(Order, pk=order_id)
        
        serializer = self.serializer_class(
            data=data,
            instance=order,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )



    def delete(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)

        order.delete()

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
    

class UpdateOrderStatus(views.GenericAPIView):
    serializer_class = StatusUpdateSerializer

    permission_classes = [IsAdminUser]

    def put(self, requset, order_id):
        order = get_object_or_404(Order, pk=order_id)

        data = requset.data

        serializer = self.serializer_class(
            data=data,
            instance=order,
        )

        if serializer.is_valid():
            serializer.save()

            return Response(
                data=serializer.data,
                status=status.HTTP_200_OK
            )
        
        return Response(
            data=serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )


class UserOrdersView(views.GenericAPIView):
    serializer_class = OrderDetailSerializer

    parser_classes = [IsAuthenticated]

    def get(self, request, user_id):
        user = UserModel.objects.get(pk=user_id)

        orders = Order.objects.filter(
            customer=user
        )

        serializer = self.serializer_class(
            instance=orders,
            many=True,
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK,
        )


class UserOrderDetailView(views.GenericAPIView):
    serializer_class = OrderDetailSerializer

    parser_classes = [IsAuthenticated]

    def get(self, request, user_id, order_id):
        user = UserModel.objects.get(pk=user_id)

        order = Order.objects.filter(
            customer=user
        ).filter(
            pk=order_id
        ).first()

        serializer = self.serializer_class(
            instance=order,
        )

        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )