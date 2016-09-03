from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.http import urlquote
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User


class CustomUserManager(BaseUserManager):
    def _create_user(self, number, owner, email,password, is_staff, is_superuser, **extra_fields):
        now = timezone.now()

        # if username != None:
        #     email = username

        if not email:
            raise ValueError("Email must be set")
        email = self.normalize_email(email)
        user = self.model(email = email,
                        is_staff=is_staff,
                        is_active=True,
                        number = number,
                        owner = owner,
                        is_superuser=is_superuser,
                        date_joined=now,
                        **extra_fields
                        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, number, owner,email,password=None,**extra_fields):
        return self._create_user(number, owner,email,password,False,False,**extra_fields)


    def create_superuser(self,email,password,**extra_fields):
        return self._create_user(None,True,email,password,True,True,**extra_fields)



class CustomUser(AbstractBaseUser, PermissionsMixin):
    username=models.CharField(null=True,blank=True,max_length=255, unique=True)
    email = models.EmailField('email address', max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=30, blank=True, null=True)
    last_name = models.CharField('last name', max_length=30, blank=True, null=True)
    number = models.IntegerField(null=True, blank=True)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    owner = models.BooleanField('Owner Status', default=False)
    date_joined = models.DateTimeField('date joined', auto_now_add=True)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name='user'
        verbose_name_plural='users'

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.email)

    def get_full_name(self):
        full_name = " %s %s " % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])

class Image(models.Model):
    image_name = models.CharField(max_length=100, null=True, blank=True)
    file = models.ImageField(null=True, blank=True, upload_to='gym_images/')
    def __unicode__(self):
        return '%s' % self.image_name

class Gym(models.Model):
    gym_name = models.CharField(max_length=100, null=True, blank=True)
    lati = models.FloatField(null=True,blank=True)
    longi = models.FloatField(null=True,blank=True)
    logo = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'),('F', 'Female'),('Z', 'Mixed')))
    number = models.IntegerField(null=True, blank=True)
    # images = models.ManyToManyField(Image, null=True, blank=True)
    file1 = models.ImageField(null=True, blank=True)
    file2 = models.ImageField(null=True, blank=True)
    file3= models.ImageField(null=True, blank=True)
    file4 = models.ImageField(null=True, blank=True)
    file5 = models.ImageField(null=True, blank=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='gym_owner')
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, null=True, related_name='gym_members')

    def __unicode__(self):
        return '%s' % self.gym_name