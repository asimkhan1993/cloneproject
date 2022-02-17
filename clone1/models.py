from django.db import models

# Create your models here.

# Data collection Wizard models will be created here


class Tree(models.Model):
    english_name = models.CharField(max_length=100, verbose_name='English Name')
    latin_name = models.CharField(max_length=100, verbose_name='Latin Name')
    dbh = models.IntegerField(verbose_name='DBH')
    drb = models.IntegerField(verbose_name='DRB')
    spread = models.IntegerField(verbose_name='Spread')
    observations = models.CharField(primary_key=True)
    landscape_significance = models.CharField(verbose_name='Landscape Significance')
    actions = models.CharField(verbose_name='Actions')
    comments = models.CharField(verbose_name='Comments')
    risk = models.CharField(verbose_name='RISK')
    specie = models.CharField(max_length=100)


    def __str__(self):
        return '%s %s %d %d %d %s %s %s %s %s %s' % (self.english_name, self.latin_name, self.dbh, self.drb, self.spread, self.observations, self.landscape_significance, self.actions, self.comments, self.risk, self.specie)


class Species(models.Model):
    type = models.ForeignKey(Tree, max_length=100, on_delete=models.CASCADE, verbose_name='Species Type')


class NewSpecies(models.Model):
    new_specie = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name='Add New Specie')

    def __str__(self):
        return self


class DataInput(models.Model):
    dbh = models.ForeignKey(Tree, on_delete=models.CASCADE, verbose_name='Enter DBH')
    dbr = models.ForeignKey(Tree, on_delete=models.CASCADE, verbose_name='Enter DBR')
    