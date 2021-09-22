Usage: 
$ cd mysite/templates
$ mv YOUR_DOWNLOAD_FOLDER/django-registration-templates.zip .
$ unzip django-registration-templates.zip
$ rm django-registration-templates.zip
$ rm readme.txt

Expected
$ tree
.
├── base.html
├── django_registration
│   ├── activation_complete.html
│   ├── activation_email_body.txt
│   ├── activation_email_subject.txt
│   ├── activation_failed.html
│   ├── registration_closed.html
│   ├── registration_complete.html
│   └── registration_form.html
└── registration
    ├── login.html
    ├── logout.html
    ├── password_change_done.html
    ├── password_change_form.html
    ├── password_reset_complete.html
    ├── password_reset_confirm.html
    ├── password_reset_done.html
    ├── password_reset_email.html
    ├── password_reset_email.txt
    └── password_reset_form.html

2 directories, 18 files
