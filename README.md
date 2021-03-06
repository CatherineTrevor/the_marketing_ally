# The Marketing Ally

<div align="center">
    <img src="media/am_i_responsive.jpg" width="600">
</div>

<a href="https://the-marketing-ally.herokuapp.com/" target="_blank">View the live site here</a>

# Contents

* [Project Overview](#project-overview)
* [User Experience Design](#user-experience-design)
   * [Strategy](#strategy)
   * [Scope](#scope)
   * [Structure](#structure)
   * [Skeleton](#skeleton)
   * [Surface](#surface)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)


<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


# Project Overview

A site promoting the marketing services offered from The Marketing Ally: a marketing consultant assisting small-medium organisations with small, short-term marketing projects, and providing guidance on budgets, plans, copywriting review and general marketing help.

Site visitors can purchase online marketing templates (plans, budgets etc.) using Stripe payments as a guest. Account owners receive a free review of the templates once completed.

Account owners can also purchase work hours required for a project, and see their order history. Time slots for project work can be requested in the booking form, but require confirmation from site admin. In the future signed in account owners can book timeslots and pay for hours within one transaction, using the Calendly and Stripe integration.

# User Experience Design

## Strategy

For small-medium enterprises (SMEs), local to Gothenburg, looking for ad-hoc marketing support, but without the large contracts, costly retainers, or lengthy project pitches offered by larger marketing consultancies / agencies, or without the need to hire staff.

Users can purchase ad-hoc hours for project work, as well as marketing templates online. Purchase of the marketing templates includes a free review of the documentation once completed (i.e. feedback on the budget, strategy, or plan as necessary) for account holders only; this is to encourage users to leave their information. Users do not have to be logged in to purchase the online templates without the review.

**Services offered:**

* General marketing / business help
* Campaign creation and set-up, including writing and reviewing emails
* LinkedIn campaign manager guidance
* Database cleansing
* Marketing budget review and management
* Advertising plan
* Marketing communications plan
* Copywriting review
* Purchase media / advertising space ??? do the negotiating for you

**Payment plans:**

| Face-to-face (F2F)  | Digital  | Cost | Purchase / Book online | Account required |
|---|---|---| --- | --- | 
| 20 minutes | 20 minutes |  FREE | Yes | No |
| Template purchase and online review  | | ???15 | Yes | For review |
| 1 hour | 1.5 hours | ???75 per booking | Yes | Yes |
| 2 hours | 2.5 hours | ???120 per booking | Yes | Yes |

**Options as a guest**

* Purchase blank marketing templates only
* Request / Book free consultation

**Options as an account owner**

* Purchase blank marketing templates, including a free online review
* Purchase project hours for work
* See historic orders 

### Target audience

Small business owners / sole traders who know what they are doing regarding their business, and know their customers and products, but require ad-hoc assistance with marketing. They do not need an employee or agency for the work, but rather the ability to purchase hours as needed, at a reasonable cost, to get the work done.

It is unnecessary and expensive for them to hire a full marketing agency, consultant, or employee, but rather what they are looking for is a more informal ???chat??? from someone who has marketing experience and can be a trusted source of feedback/sounding board, and/or create campaigns, but can be turned off at short notice. This simple fee structure makes budgeting easier. 

Businesses in the main are local to Gothenburg to provide physical meetings, however digital hours can be purchased, allowing for custom further afield, as well as tapping into the remote work culture that exists due to covid. When purchasing digital hours, users are offered slightly longer for the same rate to compensate for the lack of travel needed from the consultant.

Site visitors can only purchase one type of product ie. 1 face-to-face. In the future, the connection with Calendly booking will automate this process and make it possible to purchase multiple options in one transaction.

### User stories

**First-time visitors:**

1. I want to quickly understand the purpose of the site and the products/services offered
2. I want to easily register an account
3. I want to feel confident that the data I enter is secure
4. I want to understand the benefits of creating an account
5. I want to purchase a marketing template quickly and securely, without the need to register an account
6. I want to easily purchase work hours for a project
7. I want to complete a contact form, filling in project requirement details for more detailed work
8. I want to feel confident that my payment was successful and my order received
9. I want to be informed at every step of the purchase process, including information about any errors
10. I want to see information about previous projects carried out by the consultant and/or companies worked with as proof of the level of work carried out

**Returning visitors:**

1. I want to easily log into my account
2. I want to book project hours and feel confident that the online purchase is secure
3. I want to see the consultant's availability before making a purchase 
4. I want to see previous hours purchased, and for which project / campaign
5. I want to purchase online templates
6. I want to have control over my order bag, increasing and decreasing the quantity of items
7. I want the ability to delete my order before a purchase is made
8. I want the ability to review my order before a purchase is made

**Site administrator:**

1. I want to log into the administration area quickly and easily
2. I want to see what orders have been made, by which customers, and the order status
3. I want to easily add more online templates for users to purchase

## Scope

### Features

| Feature  | Details  | Internal links |
|---|---|---|
| Contact | Basic contact details: email, phone, address | N/A |
| Request a quote | Complete form to request a quote for more detailed work | N/A |
| About Us | Background info | N/A |
| Favicon | Top left of all pages using Django templating | Home page |
| Social links | Bottom right of all pages using Django templating | N/A |
| Previous projects / Companies worked with | Information on the homepage | N/A |
| Secure purchase project hours | Using Stripe payments | N/A |
| Request timeslot hours | Access to the consultants calendar to request a timeslot | N/A |
| Securely purchase online templates | Using Stripe payments | N/A |
| Toasts | Live feedback to the user | N/A |
| Account profile | Basic account information and purchase history | N/A |
| Navbar | Consistant on all pages. Collapsible on mobile devices | N/A |
| Footer | Consistant on all pages | N/A |
| Log In |  | N/A |
| Log Out | | N/A |
| Register | Minimum basic information required | N/A |

**Future features**

* Calendly and Stripe integration: rather than having different transactions, the site will benefit from the existing integration between Calendly and Stripe when booking and paying for project hours. At the moment the process is the user can request a timeslot, but it needs to be confirmed by the consultant and payment is an additional transaction and is a note on the booking form.
* Blog to enhance the consulant's presence in the market and encourage site visitors.
* Online portal personal to the account owner, which contains their digital work and messages, reducing the need for emails and the risk of missed telephone conversations. This will streamline the collaboration process between consultant and client.
* Partners: connect with local marketing professionals such as graphic designers, photographers, copy writers to collaborate on projects and recommend the business to their clients.
* Administration process: in the future this will be automated so only certain fields show for different products, when adding a new product via the site ie. images are only required for marketing templates.
* Emails: confirmation emails are not working on the deployed site. A future feature is that the customer will receive an automated email upon order receipt and once project hours have been booked, including regarding the review of the marketing templates.

## Structure

### Sitemap

![sitemap](https://user-images.githubusercontent.com/76033080/133998983-1e533623-ec48-4d55-ab61-922e2309edfb.png)

### Purchase process / Buyers journey

[Click to open **process overview**](https://github.com/CatherineTrevor/the_marketing_ally/files/7196040/process_overview.pdf)

[Click to open **project hours process**](https://github.com/CatherineTrevor/the_marketing_ally/files/7196041/process_project_hours.pdf)

[Click to open **marketing template**](https://github.com/CatherineTrevor/the_marketing_ally/files/7196042/process_templates.pdf)

## Skeleton

### Wireframes

See separate [SKELETON.md](/SKELETON.md) file for wireframes.

### Database schema

The database schema has been generated using [DB Diagram](https://dbdiagram.io/home)

![database_schema](https://user-images.githubusercontent.com/76033080/137586593-5c1b9796-7bc5-4f84-8f44-68031a63f633.jpg)

**Database models**

**guest_user_purchase:** allows anoynmous users to purchase marketing templates, without a user profile. Connects to the products, via order_request. Administration can review these purchases, but no profile information is saved on the site.

**user / profile**: allows for registration, sign in and for the site user to view previous purchases, as well as for the administrator to manage bookings.

**product:** management of the information required for the two product categories.

**category:** connected to the product table above.

**order_request:** used to manage the secure checkout and if a user is signed in, update their profile.

**quote_request_form:** disconnected from any other table, this enables a user to request a free consultation, or specific quote, allowing administration to make contact with the potential customer.

## Surface

**Template**

The site uses the [Tempo template from Bootstrapmade](https://bootstrapmade.com/demo/Tempo/). The template has been heavily modified for the purpose of the project.

**Typography**

The site uses Caveat and Montserrat from [Google fonts](https://fonts.google.com/specimen/Caveat?preview.text=The%20Marketing%20Ally&preview.text_type=custom#license), with sans-serif should either of those fonts not load.

**Color scheme**

The site uses a mix of standard black (#000000), and shades of grey (#a9a9a9) and red (#e43c5c).

**Imagery**

See separate [IMAGERY.md](/IMAGERY.md) file for all images and icons.

# Technologies Used

The site uses the following languages;

* HTML5
* CSS
* JavaScript
* jQuery
* Python

The project was created on GitHub and uses the following libraries and frameworks:

 - [Balsamiq](https://balsamiq.cloud/) - used to create all wireframes
 - [Bootstrap Made](https://bootstrapmade.com/demo/Tempo/) - the site layout uses the Tempo template from Bootstrap Made, which has been heavily modified
 - [Google Fonts](https://fonts.google.com/) - Caveat, Montserrat, sans-serif
 - [Django](https://www.djangoproject.com/) - the main site framework, including Allauth and Admin
 - [Heroku](https://id.heroku.com/login) - for site deployment
 - [Amazon Web Services](https://aws.amazon.com/free/) - S3 for file storage
 - [DB Diagram](https://dbdiagram.io/home) - used to generate the database schema layout
 - [PEP 8](https://www.python.org/dev/peps/pep-0008) - help following PEP 8 styling guidelines
 - [Free Formatter HTML](https://www.freeformatter.com/html-formatter.html) - for HTML code formatting
 - [Free Formatter CSS](https://www.freeformatter.com/css-beautifier.html) - to beautify CSS code
 - [Code Beautify](https://codebeautify.org/python-formatter-beautifier) - help with line indentation in Python
 - [Grammarly](https://app.grammarly.com/) - the free service to double check grammar and spelling 
 - [Monday.com](https://view.monday.com/1395852594-25c75140f7633755c3bd0aa1947579cf?r=use1) - used for project/task management 
 - [Am I responsive](http://ami.responsivedesign.is/) - supplied the responsive image for the top of README.md
 - [Remove BG](https://www.remove.bg/) - remove background from Am I Responsive image
 - [Google Maps](https://www.google.se/maps) - interactive map on contact page

# Testing

[See separate Testing file](TESTING.md) for information on testing and issues.

# Deployment

[See separate Deployment file](DEPLOYMENT.md) for information about site deployment using Heroku.

**How to fork the GitHub Repository**

Forking the repository allows you to make a copy of the original in your GitHub account, and make changes without affecting the original.

1. Log onto Github.
2. From the list of repositories, select CatherineTrevor/the_marketing_ally.
3. At the top of the repository, select the "Fork" button.
4. This should create a copy within your account.

**How to run this project locally**

1. Log onto Github: create an account if required.
2. From the list of repositories, select CatherineTrevor/the_marketing_ally.
3. Click the "Code" dropdown within the menu above the commits.
4. Copy the URL address, or Download ZIP and save locally.
5. Open your chosen IDE and navigate to the location you want the cloned directory to be saved.
6. Type git clone and copy the URL within the CLI and press enter.
7. Alternatively, select "Open with Github Desktop".

# Credits

* [Help with calendar input](https://tutorialdeep.com/live-editor/bootstrap-datepicker-with-inputbox/)
* [Stack overflow](https://stackoverflow.com/questions/40035730/bootstrap-date-time-picker/40035938)
* [Add Django dropdown in admin](https://stackoverflow.com/questions/8252101/django-admin-drop-down-selections)
* [Code to add a personalised message inside an email template](https://www.joehageonline.com/marketing/html-code-to-open-an-email-window-with-subject-body-copy/)
* [Remove BG - remove the white background from the logo](https://www.remove.bg/)
* [Help with the logo](https://stackoverflow.com/questions/14775507/link-my-logo-to-homepage-html/14775562)
* [Phone field help on contact form](https://pypi.org/project/django-phone-field/)
* [Google maps help](https://developers.google.com/maps/documentation/embed/map-generator)
* [Help with favicon](https://stackoverflow.com/questions/9371378/warning-not-found-favicon-ico)
* [Telusko MVC tutorial](https://www.youtube.com/watch?v=GGkFg52Ot5o)
* [Django apps research](https://stackoverflow.com/questions/32795227/what-is-the-purpose-of-apps-py-in-django-1-9)
* [Django signals research](https://simpleisbetterthancomplex.com/tutorial/2016/07/28/how-to-create-django-signals.html)
* [General Django help](https://docs.djangoproject.com/en/3.2/ref/csrf/)
* [General help](https://stackoverflow.com/)
* Code Institute Slack community
* Narender Singh, Code Institute mentor for his time, support and guidance
* Ex-colleagues, friends and family for their support and time testing the site
* Tutors at the Code Institute, in particular Alan for his support with Heroku deployment
