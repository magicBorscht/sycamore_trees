from django.db import models
from django.forms import ValidationError


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
        if child == self.parent:
            raise ValidationError('A node cannot be a child of its own children')
        child.save()
        for next_child in child.menunode_set.all():
            self.cascade_node_correction(next_child)

    def get_family_tree(self, nodes):
        nodes_to_operate = list(nodes)
        family_tree = [self.pk]
        if self in nodes_to_operate:
            nodes_to_operate.remove(self)
        if not self.parent_id:
            return family_tree
        family_tree.append(self.parent_id)

        while nodes_to_operate:
            node = nodes_to_operate.pop()
            if not node.menu_name == self.menu_name:
                continue
            if node.pk in family_tree:
                if not node.parent_id:
                    break
                else:
                    family_tree.append(node.parent_id)
        return family_tree

    def save(self, *args, **kwargs):
        if self.parent:
            self.level = self.parent.level + 1
            self.menu_name = self.parent.menu_name  # I don't want children to be separated from their parents!
        else:
            self.level = 0
        if self.parent in self.menunode_set.all():
            raise ValidationError('A node cannot be a child of its own children')
        for child in self.menunode_set.all():
            self.cascade_node_correction(child)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        children = list(self.menunode_set.all())
        for child in children:
            child.parent = self.parent
        super().delete(*args, **kwargs)
        for child in children:
            self.cascade_node_correction(child)
