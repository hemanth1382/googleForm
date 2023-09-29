In this project, I successfully implemented a program that takes a Google URL as input and autonomously identifies and populates the requisite fields within an HTML form. This functionality is specifically designed to work seamlessly with both "short answer" and "multiple choice" category questions within Google Forms.

For "short answer" questions, the program efficiently populates the field with the text "hello + [name_of_field]" if it happens to be empty. In the case of "multiple choice" questions, the program automatically selects the first option available if no option is selected.

Moreover, the program is capable of navigating through multiple pages within the Google Form, repeating the aforementioned actions on each subsequent page as required.

I accomplished this task by utilizing the Selenium library in Python, leveraging its powerful automation capabilities to ensure a smooth and efficient user experience.
