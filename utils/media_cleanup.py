import os
def delete_old_file_on_update(instance, model,field_name):
    if not instance.pk:
        return
    try:
        old_instance = model.objects.get(pk=instance.pk)
    except model.DoesNotExist:
        return
    old_file = getattr(old_instance, field_name)
    new_file = getattr(instance,field_name)
    if old_file and old_file != new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    def delete_file_on_delete(instance, field_name):
        file_field = getattr(instance,field_name)
        if file_field and os.path.isfile(file_field.path):
            os.remove(file_field.path)