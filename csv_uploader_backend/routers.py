from rest_framework import routers
from csv_uploader_api.viewsets import StudentViewSet

router = routers.SimpleRouter()
router.register(r'csv_uploader_api', StudentViewSet, basename='csv_uploader_api')