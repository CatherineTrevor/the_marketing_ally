# Deployment process

Deployment on Heroku

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
