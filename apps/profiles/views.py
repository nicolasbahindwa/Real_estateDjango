from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .exceptions import NotYourProfile, ProfileNotFound
from .models import Profile
from .renderers import ProfileJSONRenderer,ProfilesJSONRenderer
from .serializers import ProfileSerializer, UpdateProfileSerializer


class AgentListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.filter(is_agent=True)
    serializer_class = ProfileSerializer


class TopAgentsListApiView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]  # Fix the typo here
    renderer_classes = [ProfilesJSONRenderer]
    queryset = Profile.objects.filter(is_agent=True, top_agent=True)
    serializer_class = ProfileSerializer


class GetProfileAPIView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    def get(self, request):
        user = self.request.user
        user_profile = Profile.objects.filter(user=user).first()
        serializer = ProfileSerializer(user_profile, context={"request":request})

        return Response(serializer.data, status=status.HTTP_200_OK)



class UpdateProfileApiView(APIView):
    permissions_classes = [permissions.IsAuthenticated]
    renderer_classes = [ProfileJSONRenderer]

    serializer_class = UpdateProfileSerializer

    def patch(self, request, username):
        try:
            Profile.objects.get(user__username=username)
        except Profile.DoesNotExist:
            raise ProfileNotFound
        user_name = request.user.username
        if user_name != username:
            raise NotYourProfile
        data = request.data
        serializer = UpdateProfileSerializer(
            instance=request.user.profile,
            data = data,
            partial=True)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        



