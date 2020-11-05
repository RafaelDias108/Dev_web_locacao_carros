from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Como estamos criando um usuário diferente do padrão do Django temos que criar um gerenciador para este usuário
class GerenciadorConta(BaseUserManager):

    #Sobrescrevendo o método da BaseUserManager
	def create_user(self, email, nome, cpf, endereco, telefone, password=None):
		if not email:
			raise ValueError('Favor inserir seu e-mail')
		if not nome:
			raise ValueError('Favor inserir seu nome')
		if not cpf:
			raise ValueError('Favor inserir seu CPF')
		if not endereco:
			raise ValueError('Favor inserir seu Endereço')
		if not telefone:
			raise ValueError('Favor inserir seu Telefone')
		
		user = self.model(
			# normaliza o email colando todas as letras minusculas
			email = self.normalize_email(email),
			nome = nome,
			cpf = cpf,
			endereco = endereco,
			telefone = telefone
		)

		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, nome, cpf, endereco, telefone, password):
		user = self.create_user(
			email=self.normalize_email(email),
			nome = nome,
			cpf = cpf,
			endereco = endereco,
			telefone = telefone,
			password = password,
		)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user

# Create your models here.
# Criando um usuário modificado
class Conta(AbstractBaseUser):
	email = models.EmailField(verbose_name = 'E-mail', max_length = 100, unique=True)
	nome = models.CharField(verbose_name = 'Nome', max_length = 200, null = False, blank = False)
	cpf = models.CharField(verbose_name = 'CPF', max_length = 14, null = False, blank = False)
	endereco = models.CharField(verbose_name = 'Endereço', max_length = 200, null = False, blank = False)
	telefone = models.CharField(verbose_name = 'Telefone', max_length = 14, null = False, blank = False)
	
	# Campos obrigatórios
	date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
	last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['nome', 'cpf', 'endereco', 'telefone']
	
	# Adiciona o Gerenciador de conta sobreescrevendo alguns parametros do Django
	objects = GerenciadorConta()

	def __str__(self):
		return self.nome

	# Campos obrigatórios - Admin tem nível de autorização maior, vamos deixar por questões de simplicidade
	def has_perm(self, perm, obj=None):
		return self.is_admin

	# Verifica se o usuário tem permissão para visualizar a aplicação
	def has_module_perms(self, app_label):
		return True
        
