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