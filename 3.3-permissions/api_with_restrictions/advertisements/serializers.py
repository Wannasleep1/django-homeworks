from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement, AdvertisementStatusChoices


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        ad_status = data.get('status', AdvertisementStatusChoices.OPEN)
        opened_ads_by_user = len(Advertisement.objects.filter(creator=self.context["request"].user,
                                                              status='OPEN'))
        if (opened_ads_by_user + (ad_status == AdvertisementStatusChoices.OPEN) > 10 and
                not ad_status == AdvertisementStatusChoices.CLOSED):
            raise serializers.ValidationError("Количество открытых объявлений для одного пользователя "
                                              "не может превышать 10 штук.")

        return data
