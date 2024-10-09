<h1 id="hotel-management-system---readme">Hotel Management System - README</h1>
<h2 id="introduction">Introduction</h2>
<p>This is a basic <strong>Hotel Management System</strong> developed in Python using MySQL for managing guest bookings, room services, and records. The system allows users to book rooms, order food and beverages, and check their booking details and bills.</p>
<h2 id="features">Features</h2>
<ol>
<li><strong>Booking</strong>: Guests can book a room by providing their personal details.</li>
<li><strong>Room Service</strong>: Guests can order food and beverages, and the system will generate a bill.</li>
<li><strong>Records</strong>: Guests can view their booking details, room type, and bill by providing their phone number.</li>
</ol>
<h2 id="prerequisites">Prerequisites</h2>
<p>To run this system, you need the following:</p>
<ul>
<li><strong>Python</strong> (version 3.x)</li>
<li><strong>MySQL</strong> server installed and running.</li>
<li>Python libraries:
<ul>
<li><code>mysql-connector-python</code> (for MySQL connectivity)</li>
<li><code>datetime</code> (for date handling)</li>
</ul>
</li>
</ul>
<p>To install <code>mysql-connector-python</code>, use:</p>
<p>bash</p>
<p>Copy code</p>
<p><code>pip install mysql-connector-python</code></p>
<h2 id="database-configuration">Database Configuration</h2>
<p>Before running the program, make sure that your MySQL server is up and running. The system connects to MySQL using the following credentials:</p>
<ul>
<li><strong>Host</strong>: <code>localhost</code></li>
<li><strong>User</strong>: <code>root</code></li>
<li><strong>Password</strong>: <code>root123</code></li>
</ul>
<p>The database and necessary tables will be created automatically if they don’t exist. The database used is named <code>HotelManagement</code>.</p>
<h3 id="database-tables">Database Tables</h3>
<ol>
<li>
<p><strong>guests</strong>: Stores information about guests, including:</p>
<ul>
<li><code>Name</code>: Guest’s name</li>
<li><code>PhoneNo</code>: Guest’s phone number</li>
<li><code>Address</code>: Guest’s address</li>
<li><code>Check_In</code>: Check-in date</li>
<li><code>Check_Out</code>: Check-out date</li>
</ul>
</li>
<li>
<p><strong>rooms</strong>: Stores information about room bookings, including:</p>
<ul>
<li><code>PhoNo</code>: Phone number of the guest</li>
<li><code>TypeOfRoom</code>: Type of room booked (AC or Non-AC)</li>
</ul>
</li>
<li>
<p><strong>bill</strong>: Dynamically created based on bill number when an order is placed during room service.</p>
</li>
</ol>
<h2 id="functions">Functions</h2>
<h3 id="validation-functions">Validation Functions</h3>
<ul>
<li><strong>validate_name(name)</strong>: Checks if the name contains only alphabets and spaces.</li>
<li><strong>validate_phone_number(phone)</strong>: Checks if the phone number is 10 digits long and contains only numbers.</li>
<li><strong>validate_date(date)</strong>: Validates the date format as <code>YYYY-MM-DD</code>.</li>
</ul>
<h3 id="main-menu-options">Main Menu Options</h3>
<ol>
<li>
<p><strong>Booking</strong>:</p>
<ul>
<li>Collects guest details such as name, phone number, address, check-in, and check-out dates.</li>
<li>Validates inputs before storing them in the <code>guests</code> table.</li>
<li>Assigns a room type (AC/Non-AC) to the guest and stores it in the <code>rooms</code> table.</li>
</ul>
</li>
<li>
<p><strong>Room Service</strong>:</p>
<ul>
<li>Guests can order food or beverages from a predefined menu.</li>
<li>Each order is recorded in a dynamically created bill table.</li>
<li>A bill is generated after the order is complete, summarizing the items and total cost.</li>
</ul>
</li>
<li>
<p><strong>Records</strong>:</p>
<ul>
<li>Allows guests to check their booking details, their bill, and the type of room booked.</li>
</ul>
</li>
</ol>
<h2 id="running-the-program">Running the Program</h2>
<ol>
<li>Ensure the MySQL server is running.</li>
<li>Run the Python script.</li>
<li>Follow the prompts on the console to book a room, order food/beverages, or check records.</li>
</ol>
<h2 id="exiting-the-program">Exiting the Program</h2>
<p>To exit the program, choose the <code>0.Exit</code> option from the main menu.</p>
<h2 id="credits">Credits</h2>
<ul>
<li><strong>Developed by</strong>: Purushottam Kumar</li>
<li><strong>Project Name</strong>: Hotel Management System</li>
</ul>

