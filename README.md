#WeChat
This web app allows its users to chat with each other, add contacts, and show unread notifications when active.
It uses WeChat.db as its database with 1 table for all users. And 3 tables for each user to store their chats, contacts, history of other people to chat with.
I used 2 CSS files. One for the sidebar, header, and footer. Other for the letter.
I have used the following languages and programs: HTML, CSS, Javascript, AJAX, flask, and JQuery.
I used Bootstrap, some code from the "autocomplete.html" source to do this project.

harry.py is a demo python file that I used to add Harry Potter characters as users
index.html is the main chat page, where most of the stuff happens. It starts with rendering the header of the page with the logo and then uses Jinja code to then render all the contacts that are there. By default, a self contact is already present, so that the users can chat with themselves. Then, on top of it, there is an anchor that links it to the add_people page. Next comes the chat bar. This is where the magic happens. This part at the right refreshes every 2 seconds and also every time, a chat icon on the left sidebar is clicked. This takes message data from a SQL table and displays it constantly updating  itself every second. Finally, there is the footer, which is essentially a text box section to send a message. It is a form, which when submitted, adds to the aforementioned SQL table. I used Ajax to make all the divs constantly reload

add_people.html: here I can add more people to my contact list to chat with. I used some code from 'autocomplete.html' and prettified it using Bootstrap. I also used AJAX to add a contact div every time the button to add that contact is pressed. But here, the contacts are a list and not all buttons. For that, you first go back into the chat section. And then, the contacts act as buttons

app.py is the Flask python program that runs everything. It intricately collects both JSON and form requests and separates them to run the app. The system uses and creates 3 SQL tables for each of its users to store their contact, messages, and history of people they chat with.

Inside static, I have added all the images and CSS style sheets for the sidebar, and letter

My JS is within my HTML, separated via layout.html. I understand it might feel clumsy but since I use it to refresh my page, keeping it there helps me toggle it easily. I generally use it to add profile buttons on the left sidebar and constantly refreshes the page (AJAX) and the fetch API of course.

Enjoy!!!
