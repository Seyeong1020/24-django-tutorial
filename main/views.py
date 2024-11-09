# Create your views here.

from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)

from main.serializers import StudentSerializer


class StudentListAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    GET: 학생 목록 조회
    POST: 학생 추가
    """

    ### assignment2: 이곳에 과제를 작성해주세요
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)
    def post(self, request):
        return self.create(request)
    ### end assignment2


class StudentAPIView(
    RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView
):
    """
    GET: 학생 조회
    PATCH: 학생 수정
    DELETE: 학생 삭제
    """

    ### assignment2: 이곳에 과제를 작성해주세요
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.retrieve(request)
    def patch(self, request):
        return self.partial_update(request)
    def delete(self, request):
        return self.destroy(request)
    ### end assignment2
