from django.urls import path
from .views import (
    AgentListApiView,
    GetProfileAPIView,
    TopAgentsListApiView,
    UpdateProfileApiView)

urlpatterns = [
    path("me/", GetProfileAPIView.as_view(), name="get_profile"),
    path("update/<str:username>/", UpdateProfileApiView.as_view(), name= "update_profile"),
    path("agents/all/", AgentListApiView.as_view(), name="all_agents"),
    path("top-agents/all/", TopAgentsListApiView.as_view(), name="top_agents_all"), 

]
