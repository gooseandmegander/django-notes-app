from rest_framework import serializers, viewsets
from .models import BookMark, PersonalBookMark

# TODO: CRITICAL: Implement better security
class BookMarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookMark
        # TODO: add bookmark_folder field
        fields = ('bookmark_name', 'hyperlink')

class BookMarkViewSet(viewsets.ModelViewSet):
    serializer_class = BookMarkSerializer
    queryset = BookMark.objects.all()

class PersonalBookMarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PersonalBookMark
        fields = ('bookmark_name', 'hyperlink')
    
    def create(self, validated_data):
        user = self.context['request'].user
        personal_bookmark = PersonalBookMark.objects.create(user=user, **validated_data)
        return personal_bookmark

class PersonalBookMarkViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalBookMarkSerializer
    queryset = PersonalBookMark.objects.none()

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous:
            return queryset
        else:
            return PersonalBookMark.objects.filter(user=user)