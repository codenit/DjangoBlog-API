# DjangoBlog-API

This repo include API creation for the blog [DjangoBlog](https://github.com/codenit/DjangoBlog) using [Django Rest Framework](http://www.django-rest-framework.org/)

# Features
In addition to features of [DjangoBlog](https://github.com/codenit/DjangoBlog), this API consists of features:
>>
>>- Generic Views
>>- Permissions
>>- Serializers
>>- Filtering
>>- Pagination

To access API, head to : `http://127.0.0.1:8000/api/posts/`

![api](https://cloud.githubusercontent.com/assets/25683188/25991458/d22956c2-3720-11e7-8dc0-9599435cd75d.jpg)
-----

Similarly after registering, if you want `Edit/Update` , head to `http://127.0.0.1:8000/api/posts/`< post-id >`/edit`

For `Creating` head to `http://127.0.0.1:8000/api/posts/create` 

For `Deleting` head to `http://127.0.0.1:8000/api/posts/`< post-id >`/delete`

# Screenshots
-----
For registration head to `http://127.0.0.1:8000/register/`
- Registration:
![register](https://cloud.githubusercontent.com/assets/25683188/25780791/b1bed87c-334b-11e7-80c8-3c4a84c07079.jpg)
-----
For login head to `http://127.0.0.1:8000/login/`
- Login:
![login](https://cloud.githubusercontent.com/assets/25683188/25780798/e749b3e0-334b-11e7-9e42-2d26a9da36e5.jpg)
-----
For Homepage head to `http://127.0.0.1:8000/`
- Hompage:
![homepage](https://cloud.githubusercontent.com/assets/25683188/25780845/a3ac23a6-334c-11e7-95f0-e427cc0130d3.jpg)
-----

# Technology Stack:
- Python 3
- django 1.10
- django-markdown-deux
>> Installing the latest `django-markdown-deux` release from PyPI:
`pip install django-markdown-deux`

>>- Add `markdown_deux` to `INSTALLED_APPS` in your project's "settings.py".

For further help on `django-markdown-deux` visit [https://github.com/trentm/django-markdown-deux](https://github.com/trentm/django-markdown-deux)

- django-pagedown
>> Installing: `pip install django-pagedown`

>>- Add `django-pagedown` to your `INSTALLED_APPS`

For further help on `django-pagedown` visit [https://github.com/timmyomahony/django-pagedown](https://github.com/timmyomahony/django-pagedown)


- Django REST Framework
>> Installing 
```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support
```
>>- Add `rest_framework` to your `INSTALLED_APPS`

For further help on `DjangoRESTFramework` visit [http://www.django-rest-framework.org/](http://www.django-rest-framework.org/)
