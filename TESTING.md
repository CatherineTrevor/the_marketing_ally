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
| **New site visitors:**                                                                                                                  |                                                                                                                   |       |
| 1. I want to quickly understand the purpose of the site and the products/services offered                             | Welcome text on the top of the homepage explaining who they are and briefly the services offered                  |   ![1](https://user-images.githubusercontent.com/76033080/137577658-ed956965-c816-41f5-9d8f-2a1347bb254f.jpg)
| 2. I want to easily register an account                                                                | Top navigation Register link                                                                                      |   ![2a](https://user-images.githubusercontent.com/76033080/137578302-7d338e3e-1cdb-4710-9884-a6ca6aef1165.jpg) 
| 3. I want to feel confident that the data I enter is secure                                              | Sign up verification steps include entering the email twice, password twice and then a verification email is sent |    ![2](https://user-images.githubusercontent.com/76033080/137578303-402af604-4ca6-4b54-aea6-fecebbcf3430.jpg) 
| 4. I want to understand the benefits of creating an account                                                                              | Text throughout the site explains the benefits of having an account                                               |   ![Picture4](https://user-images.githubusercontent.com/76033080/137578301-ac836025-2eeb-4929-b83c-a53f61b1ae3b.jpg)    |
| 5. I want to purchase a marketing template quickly and securely, without the need to register an account                                 | Guest checkout option is available                                                                                |    ![Picture5](https://user-images.githubusercontent.com/76033080/137578300-75a3a22c-bb13-4f7b-a166-835bb1f163b8.jpg)   |
| 6. I want to easily purchase work hours for a project                                                                                    | Products can be added on the place an order page                                                                  |    ![Picture7](https://user-images.githubusercontent.com/76033080/137578299-e3bf0271-05fa-43ba-9867-cec37f5cf1e5.jpg)   |
| 7. I want to complete a contact form, filling in project requirement details for more detailed work                                      | This page is easily accessible from the top navigation                                                            |   ![Picture18](https://user-images.githubusercontent.com/76033080/137579349-3094cf86-26c5-4ead-98d7-573fc2a79f82.jpg)    |
| 8. I want to feel confident that my payment was successful and my order received                                                         | User is redirected to the checkout confirmation page upon purchase                                 |   ![Picture8](https://user-images.githubusercontent.com/76033080/137578297-270ee64e-4ffd-4323-8442-337cff533d88.jpg)    |
| 9. I want to be informed at every step of the purchase process, including information about any errors                                   | Pop-ups / Toasts give information throughout the buying process                                                   |  ![Picture9](https://user-images.githubusercontent.com/76033080/137578295-a5d36cb1-2a33-4ade-ae4e-5fc47b787dd8.jpg)
| 10. I want to see previous projects carried out by the consultant and/or companies worked with as proof of the level of work carried out | Portfolio information available on the homepage   | ![Picture10](https://user-images.githubusercontent.com/76033080/137578294-84d9bfd1-47b8-40f5-a0ca-ee3cc2ccd548.jpg)                                                        
| **Returning visitors:**                                                                                                                  |                                                                                                                   |       |
| 1. I want to easily log into my account                                                        | Log in from the top navigation and various places in the site                                                     |   ![Picture11](https://user-images.githubusercontent.com/76033080/137578292-8cab359a-8de0-4d68-a094-8ae94b5aba01.jpg)    |
| 2. I want to book project hours and feel confident that the online purchase is secure                                                    |        Payments are handled by a third party site and no records saved to the deployed site                           |     ![Picture12](https://user-images.githubusercontent.com/76033080/137578291-b3d89335-46e7-4e1d-80fc-1e24cc99855c.jpg)  |
| 3. I want to see previous hours purchased                                                              | Available in an account's profile                                                                                 |   ![Picture13](https://user-images.githubusercontent.com/76033080/137578309-3a905cb0-4ab1-4987-977b-769f69d558cc.jpg)  
| 4. I want to purchase online templates                                                                                                   | Available to purchase as a guest or logged in                                                                     |     ![Picture5](https://user-images.githubusercontent.com/76033080/137578300-75a3a22c-bb13-4f7b-a166-835bb1f163b8.jpg) 
| 5. I want the ability to delete my order before a purchase is made                                                               | Site users can remove items from the bag                                                                          |      ![Picture14](https://user-images.githubusercontent.com/76033080/137579038-47a86de3-a5e2-4c7d-95ad-788036474a7b.jpg)
| 6. I want the ability to review my order before a purchase is made                                                                       | Visitors are taken to a review page before checkout                                                               |      ![Picture15](https://user-images.githubusercontent.com/76033080/137578306-52563587-db09-4a49-9eed-0cc07b2dc5a0.jpg)
| **Site administrator:**                                                                                                                  |                                                                                                                   |   
| 1. I want to log into the administration area quickly and easily                                                                         | Same log in page as users, but can access administration                                                          |   ![Picture11](https://user-images.githubusercontent.com/76033080/137578292-8cab359a-8de0-4d68-a094-8ae94b5aba01.jpg) |
| 2. I want to see what orders and contact requests have been made           | Order requests available in the administration section of the site                                               |![Picture19](https://user-images.githubusercontent.com/76033080/137579330-7cf0421a-9ff7-4228-bbb3-1116f86b0bcc.jpg) |
| 3. I want to easily add more online templates for users to purchase                                                                      | Add products available to admin only                                                                              |  ![Picture17](https://user-images.githubusercontent.com/76033080/137578273-625e18b5-5892-4ee5-8c00-4e97e9a4ee89.jpg) |

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
