from rest_framework import serializers
from .models import Label, Translation

class TranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Translation
        fields = ['language_code', 'text']

class LabelSerializer(serializers.ModelSerializer):
    translations = TranslationSerializer(many=True)

    class Meta:
        model = Label
        fields = ['id', 'key', 'translations']

    def create(self, validated_data):
        translations_data = validated_data.pop('translations')
        label = Label.objects.create(**validated_data)
        for trans in translations_data:
            Translation.objects.create(label=label, **trans)
        return label

    def update(self, instance, validated_data):
        translations_data = validated_data.pop('translations')
        instance.key = validated_data.get('key', instance.key)
        instance.save()

        for trans in translations_data:
            Translation.objects.update_or_create(
                label=instance,
                language_code=trans['language_code'],
                defaults={'text': trans['text']}
            )
        return instance
