from django.contrib.auth.models import accountLimited
from rest_framework import serializers


class AccountLimitedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('branch', 'bank', 'account')
