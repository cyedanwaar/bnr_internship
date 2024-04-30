from django.urls import path
from .views import ReferenceView, ReferenceViewRUD, BidderView, BidderViewRUD


urlpatterns = [
    path('reference/', ReferenceView.as_view()),
    path('reference/<int:pk>', ReferenceViewRUD.as_view()),
    path('bidder/', BidderView.as_view()),
    path('bidder/<int:pk>', BidderViewRUD.as_view()),
]