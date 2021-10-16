# Deployment process

## AWS S3 Bucket account
* Create a new account, or log into [AWS Cloud services](https://aws.amazon.com/).
* Search for S3 and create a new bucket with a unique Bucket name. Select the relevant region.
* Untick Block public access and create bucket.
* Select the bucket, and under Properties go to static website hosting. 
* Select Host a static website, under Index document type 'index.html' and for Error 'error.html'. Save
* Within the permissions tab, edit Bucket policy.
* Generate bucket policy and copy the bucket ARN and generate the policy
* Copy the Policy JSON Document and paste into Bucket policy. Save
* Scroll to Access Control List (ACL) and select public access.
* Within the Permissions tab, scroll to CORS and edit using:
* 
                ``` [
                    {
                        "AllowedHeaders": [
                            "Authorization"
                        ],
                        "AllowedMethods": [
                            "GET"
                        ],
                        "AllowedOrigins": [
                            "*"
                         ],
                        "ExposeHeaders": []
                    }
                ] ```

## AWS IAM
* Still logged in, from the Services dropdown select IAM (Identity and Access Management)
* Select User Groups and create a new group
* Within Policies, select Create policy > Import managed policy
* Under Permissions > Add permissions > Attach policies
* Search AmazonS3FullAccess and import
* Under Action add the ARN using the following code:
* 
           ``` "Resource": [
                "<ARN here>",
                "<ARN here>/*"```
* Review policy and provide name and description, then Create policy
* Within the created User Groups, Permissions > Add permissions, choose Attach Policies and select the relevant policy
* Add a new user, selecting 'Access key - Programmatic access' 
* Add the user to the group just created
**IMPORTANT**
* Download the `.csv` containing the access key and secret access keys. They cannot be downloaded a second time.

## Connecting Heroku to AWS S3

* On Gitpod, install boto3 and django-storages, and freeze into requirements.txt
* Add the values from the .csv you downloaded to the Heroku config vars as:
  * AWS_ACCESS_KEY_ID 
  * AWS_SECRET_ACCESS_KEY
* Remove 'DISABLE_COLLECT_STATIC = 1' from the config vars
* Within gitpod create a custom_storage.py file with the following code:
* 
        ```from django.conf import settings
        from storages.backends.s3boto3 import S3Boto3Storage
        class StaticStorage(S3Boto3Storage): location = settings.STATICFILES_LOCATION
        class MediaStorage(S3Boto3Storage): location = settings.MEDIAFILES_LOCATION```

## Deployment on Heroku

This project was developed using Gitpod, committed to git and pushed to Github using the built-in functionality.

It was then deployed to Heroku.

* Create an account or log into Heroku.
* Navigate to Create New App within the New dropdown.
* Enter App name and select a region

![Picture20](https://user-images.githubusercontent.com/76033080/137580188-9126470e-f9c1-4221-afa1-19939efeca7a.jpg)

Reveal the Config Variables and enter the following information to ensure secure connection with AWS and Stripe:

* AWS_SECRET_KEY_ID
* AWS_SECRET_ACCESS_KEY
* DATABASE_URL
* EMAIL_HOST_PASS
* EMAIL_HOST_USER
* SECRET_KEY
* STRIPE_PUBLIC_KEY
* STRIPE_SECRET_KEY
* STRIPE_WH_SECRET
* USE_AWS

![Picture21](https://user-images.githubusercontent.com/76033080/137580189-add9e308-5a7a-4be8-b8d9-6d321b66eaa0.jpg)

Connect using Github (if appropriate)

Select the branch for deployment

Deploy. The app can now be viewed live.

![Picture22](https://user-images.githubusercontent.com/76033080/137580192-3f7140a0-3716-47e3-978f-077f724efbc7.jpg)
