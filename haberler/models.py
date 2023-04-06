from django.db import models


class Gazeteci(models.Model):
    isim = models.CharField(max_length=150)
    soyisim = models.CharField(max_length=150)
    biyografi = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.isim} {self.soyisim}'
    


class Makale(models.Model):
    yazar = models.ForeignKey(Gazeteci, on_delete=models.CASCADE, related_name='makaleler')
    baslik = models.CharField(max_length=120)
    aciklama = models.CharField(max_length=200)
    metin = models.TextField()
    sehir = models.CharField(max_length=120)
    yayimlanma_tarihi = models.DateTimeField()
    aktif = models.BooleanField()
    yaratilma_tarihi=models.DateTimeField(auto_now_add=True)
    güncellenme_tarihi = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.baslik
    