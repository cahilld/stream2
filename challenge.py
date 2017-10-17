Programming Challenge - Page Generator

In this challenge you will start by creating a simple text
substitution program that replaces keywords in a template
file, to generate a new file.

You will then extend the program to allow new keywords to be
defined.

Finally, you will extend the program again to allow multiple
files to be generated from the same template. All with 
fully customisable keywords.

There is a bonus challenge, to allow different templates to be
used for the various pages.

Preparation
------------
Save the following contents in a file called template.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
</head>
<body>
    <h1>{heading}</h1>
    <body>{body}</body>
<hr>
    {footer}
</body>
</html>

Tasks
-----
Part 1 - Word Substitution
    Write a program that 
        opens this file, 
        reads it's contents, 
        replaces the {tags} (see below for details)
        saves the modifed file to a file called index.html
    
	Substitute the {tags} as follows
        replace {title} with This is the Title
        replace {heading} with This is the Heading
        replace {body} with This is the Body
        replace {footer} with This is the Footer

Part 2 - More Tags
         Modify the program so that it uses a dictionary where
         the key is a tag word like 'title', and the value is the
         text to replace that tag with.
         Add the 4 existing tags, plus add 1 or 2 more tags of your choosing.
         Amend your template so that it contains the new tags that you created.
         Run the program again to regenerate 'index.html' from the new version of the template.

Part 3 - Modify the program to create a dictionary called pages
         which has a key that is a string, and contains the name of a file to be generate. The value of the dictionary should be another dictionary of tags and values as described in part 2 above.
         The dictionary might look something like this.
page_content = 
            {
    'index.html': 
                {   
                    'title': 'Landing Page', 
                    'heading': 'Welcome', 
                    'body': 'This is my cool website'
                },
    'contact.html': 
                {
                    'title': 'Contact Me', 
                    'heading': 'Get In Touch', 
                    'body': 'me@example.com'
                },
            }
            The Program should iterate over the items in this dictionary, generating pages, using the key to set the file name, and the dictionary of tags to set the file content.
            Each page should be generated using 'template.html' as
            the template, as in the challenges above.

Part 4 - Bonus Challange
            Modify the program so that the page_content dictionary described in Part 3, now also contains
            the template to use for each page.
            When generating a page, the program should generate
            a file with the correct name, using the correct template, and substituting the correct tags.
            