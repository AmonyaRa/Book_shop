from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.EmailField(required=False)

    class Meta:
        model = Book
        fields = '__all__'

        def create(self, validated_data):
            request = self.context.get('request')
            user = request.user

            product = Book.objects.create(
                owner=user, **validated_data
            )
            return product

        def update(self, instance, validated_data):
            instance.title = validated_data.get('title', instance.title)
            instance.descriptions = validated_data.get('descriptions', instance.descriptions)



