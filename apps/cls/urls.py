from django.urls import path
from .views import BranchImageAPIList, BranchAPIList, RegionAPIList

urlpatterns = [
    path('branchs/', BranchAPIList.as_view({'get': 'list'}), name='all-branchs'),
    path('branchs/<int:pk>/', BranchAPIList.as_view({'get': 'retrieve'})),
    path('branchs/create/', BranchAPIList.as_view({'post': 'create'})),

    path('branch_img/', BranchImageAPIList.as_view({'get': 'list'}), name='all-branchs'),
    path('branch_img/<int:pk>', BranchImageAPIList.as_view({'get': 'retrieve'})),
    path('branch_img/create/', BranchImageAPIList.as_view({'post': 'create'})),

]
