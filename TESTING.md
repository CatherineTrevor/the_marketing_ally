# Testing

Testing was done throughout site development, with branches created for each feature before it was merged into the master file.

Usability was tested with the below workflow, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.

<INSERT TESTING DOCUMENT>

Testing conducted outside of the Chrome development tool on the following;

* iPhone SE2020
* iPhone 12
* iPad Pro 9.7"
* All on iOS 14.3.

Testing conducted on the following browsers;

* Safari
* Chrome
* Microsoft Edge
* Firefox

## User story testing

| User story   | Requirement met  | Image |
|------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|-------|
| 
| **New site visitors:**                                                                                                                  |                                                                                                                   |       |
| 1. I want to quickly understand the purpose of the site and the products/services offered                                                | Welcome text on the top of the homepage explaining who they are and briefly the services offered                  |       |
| 2. I want to easily register an account                                                                                                  | Top navigation Register link                                                                                      |       |
| 3. I want to feel confident that the data I enter is secure                                                                              | Sign up verification steps include entering the email twice, password twice and then a verification email is sent |       |
| 4. I want to understand the benefits of creating an account                                                                              | Text throughout the site explains the benefits of having an account                                               |       |
| 5. I want to purchase a marketing template quickly and securely, without the need to register an account                                 | Guest checkout option is available                                                                                |       |
| 6. I want to easily purchase work hours for a project                                                                                    | Products can be added on the place an order page                                                                  |       |
| 7. I want to complete a contact form, filling in project requirement details for more detailed work                                      | This page is easily accessible from the top navigation                                                            |       |
| 8. I want to feel confident that my payment was successful and my order received                                                         | An order confirmation email is sent in addition to the checkout confirmation page                                 |       |
| 9. I want to be informed at every step of the purchase process, including information about any errors                                   | Pop-ups / Toasts give information throughout the buying process                                                   |       |
| 10. I want to see previous projects carried out by the consultant and/or companies worked with as proof of the level of work carried out | Portfolio information available on the homepage                                                            
| 
| **Returning visitors:**                                                                                                                  |                                                                                                                   |       |
| 1. I want to easily log into my account                                                                                                  | Log in from the top navigation and various places in the site                                                     |       |
| 2. I want to book project hours and feel confident that the online purchase is secure                                                    |                                                                                                                   |       |
| 3. I want to book project hours at a time that suits me                                                                                  | Timeslot options can be requested upon booking                                                                    |       |
| 4. I want to see previous hours purchased, and for which project / campaign                                                              | Available in an account's profile                                                                                 |       |
| 5. I want to purchase online templates                                                                                                   | Available to purchase as a guest or logged in                                                                     |       |
| 6. I want to have control over my order bag, increasing and decreasing the quantity of items                                             | There is a max of 3 hours project time that can be purchased, but site users can remove items from the bag        |       |
| 7. I want the ability to delete my order before a purchase is made                                                                       | Site users can remove items from the bag                                                                          |       |
| 8. I want the ability to review my order before a purchase is made                                                                       | Visitors are taken to a review page before checkout                                                               |       |             |                                                                                                                   |       |
| **Site administrator:**                                                                                                                  |                                                                                                                   |       |
| 1. I want to log into the administration area quickly and easily                                                                         | Same log in page as users, but can access administration                                                          |       |
| 2. I want to see what orders have been made, by which customers, and the order status                                                    | Order requests available in the administration section of the site                                                |       |
| 3. I want to easily add more online templates for users to purchase                                                                      | Add products available to admin only                                                                              |       |

## Issues

[#11](https://github.com/CatherineTrevor/the_marketing_ally/issues/11)

Bag.html was not rendering bag items. Added print code to relevant .py files and walked through the problem, then re-wrote code to solve issue.

[#14](https://github.com/CatherineTrevor/the_marketing_ally/issues/14)

Initial early deployment to Heroku was successful, however a second later deployment was not. I think this was due to using branches to manage the different features, but not ensuring migrations were managed inline with the branch changes.

Issue solved by resetting the Heroku database - this was a good solution as there were minimal products in the database and a new superuser was created.

[#15](https://github.com/CatherineTrevor/the_marketing_ally/issues/15)

Timeslot options added to calendar.html use datetimepicker from Bootstrap. Upon adding this functionality, the top menu is missaligned.

[#16](https://github.com/CatherineTrevor/the_marketing_ally/issues/16)

Remove items from bag functionality added but not working.

## Code validators