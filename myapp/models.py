from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('User must have email address')
        user=self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_staffuser(self, email, password):
        user=self.create_user(
            email, 
            password=password,
        )
        user.staff=True
        user.admin= True
        user.save(using=self.db)
    def create_superuser(self, email, password):
        user=self.create_user(
            email, 
            password=password,
        )
        user.staff=True
        user.admin= True
        user.save(using=self.db)
class UserModel(AbstractBaseUser):
    email= models.EmailField(
        max_length=255,
        verbose_name="Email address",
        unique=True,
        )
    active= models.BooleanField(default=True)
    staff= models.BooleanField(default=False)
    admin= models.BooleanField(default=False)
    USERNAME_FIELD="email"
    REQUIRED_FIELDS=[]
    objects= UserManager()
    def get_full_name(self):
        return self.email
    def get_short_name(self):
        return self.email
    def has_perm(self, perm,obj=None):
        return True
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.staff
    @property
    def is_admin(self):
        return self.admin
    @property
    def is_active(self):
        return self.active