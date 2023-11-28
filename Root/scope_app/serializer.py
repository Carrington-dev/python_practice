from rest_framework import serializers
from scope_app.models import Dino, Zone

class DinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dino
        fields = ['name', 'id', 'species', 'gender', 'digestion_period_in_hours', 'herbivore', 'created_at', 'updated_at', 'park_id',]

    park_id = serializers.PrimaryKeyRelatedField(read_only=True)



# class ZoneUpdateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Zone
#         fields = ('last_action', 'park_id', 'location', 'dino', 'updated_at')

#     park_id = serializers.PrimaryKeyRelatedField(read_only=True)
    # dino = serializers.PrimaryKeyRelatedField()