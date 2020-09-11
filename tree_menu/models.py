from django.db import models


class MenuNode(models.Model):
    parent = models.ForeignKey(to='self', verbose_name='Родительский пункт', on_delete=models.DO_NOTHING, null=True,
                               blank=True)
    name = models.CharField(verbose_name='Имя', max_length=100, default='Нет имени')
    link = models.CharField(verbose_name='Ссылка', max_length=100, default='', blank=True)
    menu_name = models.CharField(verbose_name='Имя меню', max_length=100, default='')
    level = models.IntegerField(verbose_name='Уровень отступа', default=0)

    def __str__(self):
        return f"Пункт меню {self.menu_name}: {self.name}"

    class Meta:
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'

    def cascade_node_correction(self, child):
        child.save()
        for next_child in child.menunode_set.all():
            self.cascade_node_correction(next_child)

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1
            self.menu_name = self.parent.menu_name  # I don't want children to be separated from their parents!
        else:
            self.level = 0
        for child in self.menunode_set.all():
            self.cascade_node_correction(child)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        children = list(self.menunode_set.all())
        super().delete(*args, **kwargs)
        for child in children:
            self.cascade_node_correction(child)
