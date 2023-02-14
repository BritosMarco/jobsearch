from django.db import models



class Professional(models.Model):
    name = models.CharField(max_length=150, verbose_name= 'Nome')
    marital_status = models.CharField(max_length=100, verbose_name= 'Estado civil')
    profession = models.CharField(max_length=70, verbose_name= 'Profissão')
    degree = models.CharField(max_length=70, verbose_name= 'Graduação')
    date_of_birth = models.DateField(verbose_name= 'Data de nascimento')
    work_area = models.CharField(max_length=70, verbose_name= 'Qual área deseja atuar')
    gender = models.CharField(max_length=70, verbose_name= 'Gênero')
    skin_color = models.CharField(max_length=25, verbose_name= 'Cor')
    disability = models.BooleanField(default=False, verbose_name= 'Possui alguma deficiência?')
    telefone = models.CharField(blank=True,max_length=20, verbose_name='telefone')
    email= models.EmailField(blank=True,max_length=100, verbose_name='email')
    Endereco = models.CharField(blank=True, max_length=120, verbose_name='endereco')
    numero = models.CharField(blank=True, max_length=6, verbose_name='numero')
    complemento = models.CharField(blank=True, max_length=120, verbose_name='complemento')
    bairro = models.CharField(blank=True, max_length=80, verbose_name='bairro')
    cep = models.CharField(blank=True, max_length=15, verbose_name='cep')
    cidade = models.CharField(blank=True, max_length=120, verbose_name='cidade')
    estado = models.CharField(blank=True, max_length=2, verbose_name='estado')

    class Meta:
        verbose_name= 'Professional'
        verbose_name_plural = 'Professional'

    def __str__(self):
        return self.name
    
class JobExperience(models.Model):
    company = models.CharField(max_length=150, verbose_name= 'Empresa')
    position = models.CharField(max_length=70, verbose_name= 'Cargo ou função')
    start_date = models.CharField(max_length=10, verbose_name= 'Mês/ano de início')
    end_date = models.CharField(max_length=10, verbose_name= 'Mês/ano de saída')

    professional = models.ForeignKey(Professional, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Job Experience'
        verbose_name_plural = 'Job Experience'

    def __str__(self):
            return self.company


class JobAcademic(models.Model):
    College = models.CharField(max_length=150, verbose_name= 'Insituição')
    degree = models.CharField(max_length=70, verbose_name= 'Formação ou curso')
    start_date = models.CharField(max_length=10, verbose_name= 'mês/ano de início')
    end_date = models.CharField(max_length=10, verbose_name= 'Mês/ano de conclusão')
    type_degree = models.CharField(max_length=70, verbose_name= 'Tipo de curso')

    professional = models.ForeignKey(Professional, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name= 'Job Academic'
        verbose_name_plural = 'Job Academic'

    def __str__(self):
            return self.College




