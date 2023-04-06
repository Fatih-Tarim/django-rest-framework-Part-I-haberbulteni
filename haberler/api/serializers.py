from rest_framework import serializers
from haberler.models import Makale, Gazeteci


# Time 
from django.utils.timesince import timesince
from django.utils import timezone
from datetime import datetime, date


class MakaleSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()
    # yazar = serializers.StringRelatedField()
    # yazar = GazeteciSerializer()
    class Meta:
        model = Makale
        fields = '__all__'
        read_only_fields = ['id','yaratilma_tarihi','guncellenme_tarihi']
        #exclude = []
        
    
    def get_time_since_pub(self, object):
        if object.aktif == True:
            now = timezone.now()
            pub_date = object.yayimlanma_tarihi
            time_delta = timesince(pub_date, now)
            return time_delta
        else:
            return None

    def validate_yayimlanma_tarihi(self, date_value):
        today = timezone.now()
        if date_value > today:
            raise serializers.ValidationError('Yayımlanma tarihi ileri bir tarih olamaz!')
        return date_value




class GazeteciSerializer(serializers.ModelSerializer):

    # makaleler = MakaleSerializer(many=True, read_only=True) #-> makaleler --> 'related name'
    makaleler = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='makale-detail',
    )

    class Meta:
        model = Gazeteci
        fields = '__all__'




















############# STANDAART SERIALIZER #################
class MakaleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    aciklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayimlanma_tarihi = serializers.DateTimeField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncellenme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.aciklama = validated_data.get('aciklama', instance.aciklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayimlanma_tarihi = validated_data.get('yayimlanma_tarihi', instance.yayimlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.yaratilma_tarihi = validated_data.get('yaratilma_tarihi', instance.yaratilma_tarihi)
        instance.güncellenme_tarihi = validated_data.get('güncellenme_tarihi', instance.güncellenme_tarihi)
        instance.save()
        return instance
        
    def validate(self, data): #Object Level Validate
        if data['baslik'] == data['aciklama']:
            raise serializers.ValidationError('Başlık ve açıklama alanları aynı olamaz!')
        return data

    def validate_baslik(self, value):
        if len(value) < 10:
            raise serializers.ValidationError(f'Başlık 10 karakterden küçük olamaz. Girilen değer len {len(value)} karakter')
        return value