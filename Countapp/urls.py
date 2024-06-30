
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('stop-tracking/', views.stop_tracking, name='stop_tracking'),  # 걷기 기록 종료 시
    path('record/<int:record_id>/upload/', views.upload_certification, name='upload_certification'),  # 인증샷 업로드 페이지
    path('record/<int:record_id>/upload/success/', views.upload_success, name='upload_success'),  # 인증샷 업로드 성공 페이지
]
