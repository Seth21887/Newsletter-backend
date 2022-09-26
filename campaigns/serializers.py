#used to validate incoming info from the user
#and also to specify different outputs from the user

from rest_framework import serializers
from .models import Campaign, Subscriber


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model=Campaign
        fields="__all__" #this dunder all will ensure all fields are included

class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subscriber
        fields="__all__"