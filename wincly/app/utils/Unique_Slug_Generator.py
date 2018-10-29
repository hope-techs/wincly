from django.utils.text import slugify

# import time
# Now = time.localtime(time.time())
# FORMAT = str(Now.tm_year) + '-' + str(Now.tm_mon)
# print(time.localtime(time.time()))
# print(time.gmtime(time.time()))
# print (FORMAT)


import datetime
# tmp = datetime.datetime.now()
tmp = datetime.datetime.now().strftime('%Y-%b-%d')
# new = tmp.strftime('%Y-%b-%d')
# new = tmp.strftime('%Y-%m-%d')
# print (tmp)


'''
random_string_generator is located here:
http://joincfe.com/blog/random-string-generator-in-python/
'''

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.name, allow_unicode=True)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()
    if qs_exists and not instance.slug:
        new_slug = "{slug}-{date}".format(
                    slug=slug,
                    date=tmp
                )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug
