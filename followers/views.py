from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer

# Create your views here.


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user'.
    Create a follower, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a follower.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FollowerDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a follower
    No Update view, as we either follow or unfollow users
    Destroy a follower, i.e. unfollow someone if owner
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
