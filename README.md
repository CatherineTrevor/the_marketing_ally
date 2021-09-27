# The Marketing Ally

<div align="center">
    <img src="" width="600">
</div>

<a href="" target="_blank">View the live site here</a>

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

A site promoting the marketing services offered from The Marketing Ally: a marketing consultant assisting small-medium organisations on small, short-term marketing projects, and providing guidance on budgets, plans, copywriting review and general marketing help.

Site visitors can purchase online marketing templates (plans, budgets etc.) using Stripe payments as a guest. Account owners receive a free review of the templates once completed.

Account owners can also purchase work hours required for a project, and see their order history. Time slots for project work can be requested via Calendly, but require confirmation from site admin. In the future signed in account owners can book timeslots and pay for hours within one transaction, using the Calendly and Stripe integration.

# User Experience Design

## Strategy

For small-medium enterprises (SMEs), local to Gothenburg, looking for ad-hoc marketing support, but without the large contracts, costly retainers, or lengthy project pitches offered by larger marketing consultancies / agencies, or without the need to hire staff.

Users can purchase ad-hoc hours for project work, as well as marketing templates online. Purchase of the marketing templates includes a free review of the documentation once completed (i.e. feedback on the budget, strategy, or plan as necessary) for account holders only; this is to encourage users to leave their information. Users do not have to be logged in to purchase just the online templates without the review.

**Services offered:**

* General marketing / business help
* Campaign creation and set-up, including writing and reviewing emails
* LinkedIn campaign manager guidance
* Database cleansing
* Marketing budget review and management
* Advertising plan
* Marketing communications plan
* Copywriting review
* Purchase media / advertising space – do the negotiating for you

**Payment plans:**

| Face-to-face (F2F)  | Digital  | Cost | Purchase / Book online | Account required |
|---|---|---| --- | --- | 
| 30 minutes | 45 minutes |  FREE | Yes | No |
| Template purchase and online review  | | €15 | Yes | For review |
| 1 hour | 1.5 hours | €75 per booking | Yes | Yes |
| 2 hours | 2.5 hours | €120 per booking (€60 per hour) | Yes | Yes |

**Options as a guest**

* Purchase blank marketing templates only
* Request / Book free consultation

**Options as an account owner**

* Purchase blank marketing templates, including a free online review
* Purchase project hours for work
* See historic orders 

### Target audience

Small business owners / sole traders who know what they are doing regarding their business, and know their customers and products, but require ad-hoc assistance with marketing. They do not need an employee or agency for the work, but rather the ability to purchase hours as needed, at a reasonable cost, to get the work done.

It is unnecessary and expensive for them to hire a full marketing agency, consultant, or employee, but rather what they are looking for is a more informal “chat” from someone who has marketing experience and can be a trusted source of feedback/sounding board, and/or create campaigns, but can be turned off at short notice. This simple fee structure makes budgeting easier. 

Allowing account owners to purchase and book hours through an online booking system fulfils this need.

Businesses in the main are local to Gothenburg to provide physical meetings, however digital hours can be purchased, allowing for custom further afield, as well as tapping into the remote work culture that exists due to covid. When purchasing digital hours, users are offered slightly longer for the same rate to compensate for the lack of travel needed from the consultant.

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
10. I want to see previous projects carried out by the consultant and/or companies worked with as proof of the level of work carried out

**Returning visitors:**

1. I want to easily log into my account
2. I want to book project hours and feel confident that the online purchase is secure
3. I want to book project hours at a time that suits me
4. I want to see previous hours purchased, and for which project / campaign
5. I want to purchase online templates
6. I want to have control over my order bag, increasing and decreasing the quantity of items
7. I want the ability to delete my order before a purchase is made
8. I want the ability to review my order before a purchase is made
9. I want the ability to delete my account

**Site administrator:**

1. I want to log into the administration area quickly and easily
2. I want to see what orders have been made, by which customers, and the order status
3. I want to easily add more online templates for users to purchase
4. I want to securely change hour timeslot requests to confirm booked meetings

## Scope

### Features

| Feature  | Details  | Internal links |
|---|---|---|
| Contact | Basic contact details: email, phone, address | N/A |
| Request a quote | Complete form to request a quote for more detailed work | N/A |
| About Us | Background info | N/A |
| Favicon | Top left of all pages using Django templating | Home page |
| Social links | Bottom right of all pages using Django templating | N/A |
| Previous projects / Companies worked with | Carousel on the homepage | N/A |
| Secure purchase project hours | Using Stripe payments | N/A |
| Booking hours | Access to the consultants calendar to request a timeslot | N/A |
| Securely purchase online templates | Using Stripe payments | N/A |
| Toasts | Live feedback to the user | N/A |
| Account profile | Basic account information and purchase history, including status of current hours | N/A |
| Navbar | Consistant on all pages. Collapsible on mobile devices | N/A |
| Footer | Consistant on all pages | N/A |
| Log In |  | N/A |
| Log Out | | N/A |
| Register | Minimum basic information required | N/A |

**Future features**

* Calendly and Stripe integration: rather than having different transactions, the site will benefit from the existing integration between Calendly and Stripe when booking and paying for project hours. At the moment the process is the user can request a timeslot, but it needs to be confirmed by the consultant and payment is an additional transaction.
* Blog to enhance the consulant's presence in the market and encourage site visitors.
* Online portal personal to the account owner, which contains their digital work and messages, reducing the need for emails and the risk of missed telephone conversations. This will streamline the collaboration process between consultant and client.
* Partners: connect with local marketing professionals such as graphic designers, photographers, copy writers to collaborate on projects and recommend the business to their clients.

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

![database_schema](https://user-images.githubusercontent.com/76033080/134001763-e9dfbf1e-90f5-4e8e-af04-3dc4c69a86a0.png)

## Surface

**Template**

The site uses the [Tempo template from Bootstrapmade](https://bootstrapmade.com/demo/Tempo/). The template has been heavily modified for the purpose of the project.

**Typography**

**Color scheme**

**Imagery**

See separate [IMAGERY.md](/IMAGERY.md) file for all images and icons.

# Technologies Used

# Testing

# Deployment

# Credits
