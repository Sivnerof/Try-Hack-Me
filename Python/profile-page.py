"""Fills in an HTML template with user data to construct a custom webpage."""

import webpage

# Collect user profile data.
first_name = input("What's your first name? ")
last_name = input("What's your last name? ")
age = input("What age are you? ")
favorite_book = input("What's your favorite book? ")

# Construct a personalized page header for the logged in user.
header_title = "<h1>Guest's profile</h1>"
header_subtitle = "<h2>Hello, " + first_name + " " + last_name + "!</h2>"
header_content = "<p>unknown@example.com</p>"
page_header = header_title + header_subtitle + header_content

# Construct the main profile page content.
section_title = "<h2>About guest</h2>"
section_text = "<p>This is a cool bio.</p>"
section_text += "<p>Full Name: " + first_name + " " + last_name
section_text += "</p>" +  "<p>Age: " + age + "</p>"
section_text += "<p>Favorite Book: " + favorite_book + "</p>"
button = "<button>Like</button>"
section_footer = "<p>Notifications: 4</p>"
page_content = section_title + section_text + button + section_footer

# The final HTML body combines all the elements, in order.
webpage.render(page_header + page_content)

