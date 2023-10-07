from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, generics
from school.models import Course, Lesson, Subscription
from school.permissions import IsModeratorViewSet, IsOwnerOrSuperuser, IsModerator
from school.serializers import CourseSerializer, LessonSerializer, SubscriptionSerializer
from school.validators import URL_Validator


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser | IsModeratorViewSet]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Course.objects.all()
        else:
            return Course.objects.filter(owner=self.request.user)


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, ~IsModerator]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser | IsModerator]

    def get_queryset(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return Lesson.objects.all()
        else:
            return Lesson.objects.filter(owner=self.request.user)


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser | IsModerator]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser | IsModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsOwnerOrSuperuser, ~IsModerator]
