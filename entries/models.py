from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from django.conf import settings
from django.db import models

MAX_SECRET_LENGTH = 512
BLOCK_SIZE = 16


def generate_iv_value():
    return get_random_bytes(16)


class Folder(models.Model):
    """Represents a folder containing other folders and entries."""
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, default=None, related_name='sub_folders', on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Entry(models.Model):
    """Represents a secret entry stored inside a Folder."""
    name = models.CharField(max_length=255)
    folder = models.ForeignKey(Folder, related_name='entries', on_delete=models.CASCADE)
    url = models.URLField(null=True, blank=True)
    login = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    _iv = models.BinaryField(max_length=16, default=generate_iv_value)
    _secret = models.BinaryField(max_length=MAX_SECRET_LENGTH+BLOCK_SIZE, blank=True)

    def __str__(self):
        return self.name

    def set_secret(self, secret):
        key = bytes(settings.SECRET_KEY, 'utf-8')[:16]
        enc_suite = AES.new(key, AES.MODE_CBC, iv=self._iv)
        data = pad(secret.encode(), enc_suite.block_size)
        self._secret = enc_suite.encrypt(data)

    def get_secret(self):
        return self._secret

    secret = property(get_secret, set_secret)

    def decrypt(self):
        key = bytes(settings.SECRET_KEY, 'utf-8')[:16]
        enc_suite = AES.new(key, AES.MODE_CBC, iv=self._iv)
        clear_text = unpad(enc_suite.decrypt(self.secret), enc_suite.block_size)
        return clear_text.decode('utf-8')
