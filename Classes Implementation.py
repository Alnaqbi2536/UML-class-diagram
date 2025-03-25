#the USER class
class User:
    """
    Represents a system user with authentication, profile management, and communication features.
    """

    def __init__(self, user_id: int, name: str, contact_info: str, username: str, password: str, user_role: str):
        # Private attributes to store user details securely
        self.__user_id = user_id
        self.__name = name
        self.__contact_info = contact_info
        self.__username = username
        self.__password = password  # Storing plain text passwords is not secure
        self.__user_role = user_role

    def login(self, username: str, password: str) -> bool:
        """
        Authenticates the user based on username and password.
        Ideally, password should be hashed and compared securely.
        """
        if self.__username == username and self.__password == password:
            print("Login successful.")
            return True
        print("Invalid credentials.")
        return False  # Consider limiting login attempts to prevent brute-force attacks

    def logout(self) -> None:
        """Logs out the user."""
        print("User logged out.")

    def update_profile(self, new_info: dict) -> None:
        """
        Updates the user's profile details.
        Ensures that only valid data is updated.
        """
        self.__name = new_info.get("name", self.__name)
        self.__contact_info = new_info.get("contact_info", self.__contact_info)
        print("Profile updated.")

    def reset_password(self, new_password: str) -> bool:
        """
        Resets the user's password.
        It should ideally enforce password complexity rules.
        """
        self.__password = new_password  # Password should be hashed for security
        print("Password reset successfully.")
        return True

    def deactivate_account(self) -> bool:
        """Deactivates the user's account."""
        print("Account has been deactivated.")
        return True  # Consider implementing a reactivation mechanism

    def get_account_details(self) -> dict:
        """
        Retrieves the user's account details.
        The password is not included for security reasons.
        """
        return {
            "user_id": self.__user_id,
            "name": self.__name,
            "contact_info": self.__contact_info,
            "username": self.__username,
            "user_role": self.__user_role,
        }

    def check_booking_history(self) -> list:
        """
        Retrieves the user's booking history.
        This should be fetched from a database instead of returning static data.
        """
        return ["Booking 1", "Booking 2", "Booking 3"]  # Placeholder for actual booking history

    def send_message(self, receiver: "User", message: str) -> None:
        """
        Sends a message to another user.
        Consider implementing a message queue for better handling.
        """
        print(f"Message sent to {receiver.__username}: {message}")

    def change_contact_info(self, new_contact: str) -> bool:
        """
        Updates the user's contact information.
        Validation should be added to ensure a valid email/phone format.
        """
        self.__contact_info = new_contact
        print("Contact information updated.")
        return True

    def upgrade_account(self, new_role: str) -> bool:
        """
        Upgrades the user's role in the system.
        Admin-level approval may be required for security.
        """
        self.__user_role = new_role
        print(f"Account upgraded to {new_role}.")
        return True

    def verify_identity(self, document: str) -> bool:
        """
        Verifies the user's identity using a provided document.
        Ideally, this should integrate with a secure verification system.
        """
        print(f"Verifying identity with document: {document}")
        return True  # Placeholder for actual verification logic

    def request_support(self, issue: str) -> str:
        """
        Submits a support request for the user.
        Consider logging these requests for tracking and response management.
        """
        return f"Support request submitted: {issue}"


# Employee class
class Employee:
    """
    Represents an employee responsible for handling service
    requests, managing schedules, and reporting work progress.
    """

    def __init__(self, employee_id: int, name: str, role: str, admin_id: int, username: str, password: str):
        # Private attributes for employee information
        self.__employee_id = employee_id
        self.__name = name
        self.__role = role
        self.__assigned_requests = []  # List to store assigned service requests
        self.__admin_id = admin_id  # ID of the admin supervising this employee
        self.__username = username
        self.__password = password  # Password should be stored securely (hashed)

    def handle_service_request(self, request_id: int) -> None:
        """
        Processes a service request.
        Ideally, this should update the request status in a database.
        """
        print(f"Handling service request {request_id}.")

    def get_assigned_requests(self) -> list:
        """
        Returns a list of assigned service requests.
        Should be dynamically retrieved from a database.
        """
        return self.__assigned_requests

    def update_request_status(self, request_id: int, status: str) -> None:
        """
        Updates the status of a service request.
        Ideally, this should interact with a service request tracking system.
        """
        print(f"Service request {request_id} status updated to {status}.")

    def view_schedule(self) -> dict:
        """
        Retrieves the employee's schedule.
        Should be dynamically loaded instead of a static dictionary.
        """
        return {"Monday": "Shift 9 AM - 5 PM", "Tuesday": "Off-duty"}

    def submit_work_report(self) -> None:
        """
        Submits a work report.
        Consider implementing a logging system to track reports.
        """
        print("Work report submitted.")

    def request_leave(self, days: int) -> bool:
        """
        Allows an employee to request leave.
        The approval limit is currently set to 14 days.
        """
        if days <= 14:
            print("Leave request approved.")
            return True
        print("Leave request denied.")
        return False

    def receive_notification(self, message: str) -> None:
        """
        Receives a notification.
        Consider integrating with an actual notification system.
        """
        print(f"Notification received: {message}")

    def log_hours_worked(self, hours: int) -> None:
        """
        Logs the number of hours worked by the employee.
        Should store this data in a database for payroll calculations.
        """
        print(f"Logged {hours} hours worked.")

    def transfer_request_to_another_employee(self, employee: "Employee", request_id: int) -> None:
        """
        Transfers a service request to another employee.
        This should update the request ownership in the system.
        """
        print(f"Transferred request {request_id} to {employee.__name}")

    def view_employee_performance(self) -> dict:
        """
        Retrieves performance metrics of the employee.
        Performance tracking should be based on real data.
        """
        return {"Performance": "Excellent", "Tasks Completed": 50}

#Room Class
class Room:
    """
    Represents a hotel room with details like room number, type, amenities, price, and availability.
    """

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, availability_status: bool = True):
        """
        Initializes a Room object with its details.
        
        Parameters:
        - room_number (int): Unique number assigned to the room.
        - room_type (str): Type of room (e.g., Single, Double, Suite).
        - amenities (list): List of amenities available in the room.
        - price_per_night (float): Cost of staying per night.
        - availability_status (bool): Whether the room is available (default: True).
        """
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities  # List of amenities like Wi-Fi, AC, TV, etc.
        self.__price_per_night = price_per_night
        self.__availability_status = availability_status  # True if the room is available, False otherwise.

    def check_availability(self) -> bool:
        """
        Returns the availability status of the room.
        
        Returns:
        - bool: True if the room is available, False otherwise.
        """
        return self.__availability_status

    def update_status(self, new_status: bool) -> None:
        """
        Updates the availability status of the room.
        
        Parameters:
        - new_status (bool): The new availability status (True for available, False for occupied).
        """
        self.__availability_status = new_status

    def get_price(self) -> float:
        """
        Returns the price per night for the room.
        
        Returns:
        - float: The price per night.
        """
        return self.__price_per_night

    def add_amenity(self, amenity: str) -> None:
        """
        Adds a new amenity to the room if it's not already present.
        
        Parameters:
        - amenity (str): The name of the amenity to be added.
        """
        if amenity not in self.__amenities:
            self.__amenities.append(amenity)

    def remove_amenity(self, amenity: str) -> None:
        """
        Removes an existing amenity from the room.
        
        Parameters:
        - amenity (str): The name of the amenity to be removed.
        """
        if amenity in self.__amenities:
            self.__amenities.remove(amenity)

    def get_room_info(self) -> dict:
        """
        Returns a dictionary containing all the room details.
        
        Returns:
        - dict: Room details including room number, type, amenities, price, and availability.
        """
        return {
            "room_number": self.__room_number,
            "room_type": self.__room_type,
            "amenities": self.__amenities,
            "price_per_night": self.__price_per_night,
            "availability_status": self.__availability_status
        }

    def update_price(self, new_price: float) -> None:
        """
        Updates the price per night of the room.
        
        Parameters:
        - new_price (float): The new price for the room.
        """
        self.__price_per_night = new_price

    def calculate_discounted_price(self, discount: float) -> float:
        """
        Calculates the price of the room after applying a discount.
        
        Parameters:
        - discount (float): Discount percentage to be applied.
        
        Returns:
        - float: The discounted price.
        """
        return self.__price_per_night * (1 - discount / 100)

    def release_room(self) -> None:
        """
        Marks the room as available when a guest checks out.
        """
        self.__availability_status = True

    def schedule_maintenance(self, date: str) -> None:
        """
        Marks the room as unavailable due to scheduled maintenance.
        
        Parameters:
        - date (str): The scheduled maintenance date (currently not stored).
        
        Note: Ideally, the date should be recorded in a maintenance log.
        """
        self.__availability_status = False

 
 # guest class
class Guest:
    """
    Represents a guest with personal details and loyalty program status.
    """

    def __init__(self, guest_id: int, name: str, contact_info: str, loyalty_status: bool = False):
        """
        Initializes a Guest object.
        
        Parameters:
        - guest_id (int): Unique ID for the guest.
        - name (str): Guest's full name.
        - contact_info (str): Guest's contact details.
        - loyalty_status (bool): Whether the guest is enrolled in the loyalty program.
        """
        self.__guest_id = guest_id
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_status = loyalty_status
        self.__loyalty_points = 0  # Start with 0 points
        self.__reservation_history = []  # List of booking IDs

    def create_account(self, name: str, contact_info: str) -> None:
        """
        Creates a guest account.
        """
        self.__name = name
        self.__contact_info = contact_info
        print("Account created successfully.")

    def update_profile(self, new_name: str, new_contact: str) -> None:
        """
        Updates guest profile details.
        """
        self.__name = new_name
        self.__contact_info = new_contact
        print("Profile updated successfully.")

    def view_reservation_history(self) -> list:
        """
        Returns the guest's reservation history.
        """
        return self.__reservation_history

    def join_loyalty_program(self) -> None:
        """
        Enrolls the guest in the loyalty program.
        """
        if not self.__loyalty_status:
            self.__loyalty_status = True
            self.__loyalty_points = 50  # Give initial bonus points
            print("Joined loyalty program successfully. Earned 50 points!")
        else:
            print("Already enrolled in the loyalty program.")

    def request_service(self, service: str) -> str:
        """
        Requests an additional service for the stay.
        """
        return f"Service request '{service}' has been placed."

    def cancel_booking(self, booking_id: int) -> None:
        """
        Cancels a booking and removes it from the reservation history.
        """
        if booking_id in self.__reservation_history:
            self.__reservation_history.remove(booking_id)
            print(f"Booking {booking_id} has been canceled.")
        else:
            print(f"Booking {booking_id} not found.")

    def give_feedback(self, rating: int, comments: str) -> str:
        """
        Allows the guest to give feedback on their stay.
        """
        return f"Feedback submitted with rating {rating}: {comments}"

    def view_loyalty_points(self) -> int:
        """
        Returns the number of loyalty points the guest has.
        """
        return self.__loyalty_points

    def earn_loyalty_points(self, amount_spent: float) -> None:
        """
        Adds loyalty points based on the amount spent on bookings.
        
        - Earn 1 point per $10 spent.
        """
        points_earned = int(amount_spent / 10)
        self.__loyalty_points += points_earned
        print(f"You earned {points_earned} loyalty points! Total: {self.__loyalty_points} points.")

    def redeem_loyalty_points(self, points: int) -> bool:
        """
        Redeems loyalty points if the guest has enough.
        """
        if points > self.__loyalty_points:
            print("Not enough loyalty points.")
            return False
        self.__loyalty_points -= points
        print(f"{points} loyalty points redeemed successfully. Remaining: {self.__loyalty_points} points.")
        return True

    def add_reservation(self, booking_id: int) -> None:
        """
        Adds a booking ID to the guest's reservation history.
        """
        self.__reservation_history.append(booking_id)

    def view_invoice(self, booking_id: int) -> str:
        """
        Displays invoice details for a given booking.
        """
        if booking_id in self.__reservation_history:
            return f"Invoice for booking {booking_id} is available."
        return f"No invoice found for booking {booking_id}."

#Booking Class
class Booking:
    """
    Represents a hotel booking with guest details, room assignment, and booking status.
    """

    def __init__(self, booking_id: int, guest: "Guest", room: "Room", check_in_date: str, check_out_date: str, status: str = "Pending"):
        """
        Initializes a Booking instance.

        :param booking_id: Unique identifier for the booking.
        :param guest: The Guest object associated with the booking.
        :param room: The Room object assigned to the booking.
        :param check_in_date: The check-in date in YYYY-MM-DD format.
        :param check_out_date: The check-out date in YYYY-MM-DD format.
        :param status: The booking status (e.g., Pending, Confirmed, Cancelled).
        """
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in_date = check_in_date
        self.__check_out_date = check_out_date
        self.__status = status
        self.__special_requests = []

    def confirm_booking(self) -> None:
        """
        Confirms the booking by updating its status.
        """
        self.__status = "Confirmed"
        print(f"Booking {self.__booking_id} confirmed.")

    def cancel_booking(self) -> None:
        """
        Cancels the booking by updating its status.
        """
        self.__status = "Cancelled"
        print(f"Booking {self.__booking_id} cancelled.")

    def modify_booking(self, new_dates: tuple) -> None:
        """
        Modifies the booking dates.

        :param new_dates: A tuple containing (new_check_in_date, new_check_out_date).
        """
        self.__check_in_date, self.__check_out_date = new_dates
        print(f"Booking {self.__booking_id} modified to new dates: {new_dates}")

    def calculate_total_cost(self) -> float:
        """
        Calculates the total cost of the booking based on room price and duration.

        :return: The total cost of the stay.
        """
        num_nights = int(self.__check_out_date.split('-')[2]) - int(self.__check_in_date.split('-')[2])
        return num_nights * self.__room.get_price()

    def apply_discount(self, discount: float) -> None:
        """
        Applies a discount to the room price.

        :param discount: The discount percentage (0-100).
        """
        new_price = self.__room.calculate_discounted_price(discount)
        print(f"Discount applied. New room price: {new_price}")

    def generate_booking_summary(self) -> str:
        """
        Generates a summary of the booking details.

        :return: A formatted booking summary.
        """
        return f"Booking {self.__booking_id}: Guest {self.__guest.get_account_details()['name']}, Room {self.__room.get_room_info()['room_number']}, Status: {self.__status}"

    def extend_booking(self, extra_days: int) -> None:
        """
        Extends the booking by a given number of days.

        :param extra_days: The number of additional days to extend the booking.
        """
        new_checkout_day = int(self.__check_out_date.split('-')[2]) + extra_days
        self.__check_out_date = f"{self.__check_out_date[:8]}{new_checkout_day}"
        print(f"Booking {self.__booking_id} extended for {extra_days} extra days.")

    def add_special_request(self, request: str) -> None:
        """
        Adds a special request for the booking.

        :param request: The special request description.
        """
        self.__special_requests.append(request)
        print(f"Special request added: {request}")

    def assign_room(self, room: "Room") -> None:
        """
        Assigns a new room to the booking.

        :param room: The new Room object.
        """
        self.__room = room
        print(f"Booking {self.__booking_id} assigned to Room {room.get_room_info()['room_number']}")

    def change_guest_details(self, new_guest: "Guest") -> None:
        """
        Updates the guest details associated with the booking.

        :param new_guest: The new Guest object.
        """
        self.__guest = new_guest
        print(f"Guest details updated for Booking {self.__booking_id}")

    def notify_guest(self) -> None:
        """
        Sends a notification to the guest about their booking.
        """
        print(f"Notification sent to Guest {self.__guest.get_account_details()['name']} for Booking {self.__booking_id}")

#Payment Class 
class Payment:
    """
    Handles payment processing, invoices, refunds, and validation.
    """

    def __init__(self, payment_id: int, booking: "Booking", amount: float, payment_method: str, status: str = "Pending"):
        self.__payment_id = payment_id
        self.__booking = booking
        self.__amount = amount
        self.__payment_method = payment_method
        self.__status = status

    def process_payment(self) -> bool:
        """Processes the payment if it's still pending."""
        if self.__status == "Pending":
            self.__status = "Completed"
            print("Payment processed successfully.")
            return True
        print("Payment failed or already processed.")
        return False

    def generate_invoice(self) -> str:
        """Generates an invoice for the payment."""
        return f"Invoice: Payment ID {self.__payment_id}, Amount: {self.__amount}, Method: {self.__payment_method}, Status: {self.__status}"

    def refund_payment(self) -> None:
        """Refunds the payment if it was completed."""
        if self.__status == "Completed":
            self.__status = "Refunded"
            print("Payment refunded successfully.")

    def apply_vat(self, vat: float) -> None:
        """Applies VAT to the payment amount."""
        self.__amount += self.__amount * (vat / 100)
        print(f"VAT applied. New amount: {self.__amount}")

    def split_payment(self, methods: list[str], amounts: list[float]) -> None:
        """Splits the payment across multiple methods if the total matches."""
        if sum(amounts) == self.__amount:
            self.__payment_method = ", ".join(methods)
            print(f"Payment successfully split across methods: {methods}")
        else:
            print("Error: Split payment amounts do not match the total amount.")

    def validate_payment_details(self) -> bool:
        """Validates payment details (amount must be positive and a payment method must be provided)."""
        return self.__amount > 0 and bool(self.__payment_method)

    def get_payment_status(self) -> str:
        """Returns the current payment status."""
        return self.__status

    def send_payment_receipt(self) -> None:
        """Sends a payment receipt."""
        print(f"Receipt sent for Payment ID {self.__payment_id}")

    def apply_coupon(self, coupon_code: str) -> bool:
        """Applies a coupon discount if valid."""
        if coupon_code == "DISCOUNT10":
            self.__amount *= 0.9
            print("Coupon applied successfully.")
            return True
        print("Invalid coupon code.")
        return False

    def record_failed_transaction(self) -> None:
        """Records a failed transaction."""
        self.__status = "Failed"
        print("Payment failed and recorded.")

    def verify_card_details(self, card_number: str) -> bool:
        """Verifies if a card number is valid (must be 16 digits and numeric)."""
        return len(card_number) == 16 and card_number.isdigit()
    #Admin class 
class Admin:
    """
    Represents an administrative user who manages hotel operations.
    """

    def __init__(self, admin_id: int, username: str, password: str):
        """
        Initializes an Admin instance.

        :param admin_id: Unique identifier for the admin.
        :param username: Admin's username.
        :param password: Admin's password (should be securely stored in a real application).
        """
        self.__admin_id = admin_id
        self.__username = username
        self.__password = password  # Consider using a hashing function for security.

    def manage_rooms(self) -> None:
        """
        Manages hotel rooms, such as adding or removing rooms.
        """
        print("Managing rooms...")

    def view_reports(self) -> str:
        """
        Retrieves and displays system reports.

        :return: A string representing the system reports.
        """
        return "Displaying system reports..."

    def approve_service_requests(self, request_id: int) -> None:
        """
        Approves a service request based on its ID.

        :param request_id: The ID of the service request to approve.
        """
        print(f"Service request {request_id} approved.")

    def assign_employees_to_requests(self) -> None:
        """
        Assigns employees to handle specific service requests.
        """
        print("Assigning employees to service requests...")

    def monitor_system_activity(self) -> dict:
        """
        Monitors the system's current activity, including status and active users.

        :return: A dictionary with system status and active user count.
        """
        return {"status": "System running smoothly", "active_users": 120}

    def update_hotel_policies(self, policy: str) -> None:
        """
        Updates hotel policies.

        :param policy: The new hotel policy to implement.
        """
        print(f"Updated hotel policy: {policy}")

    def generate_financial_report(self) -> str:
        """
        Generates a financial report for the hotel.

        :return: A string representing the financial report.
        """
        return "Financial report generated."

    def block_guest(self, guest_id: int) -> None:
        """
        Blocks a guest from making further bookings.

        :param guest_id: The ID of the guest to be blocked.
        """
        print(f"Guest {guest_id} has been blocked.")

    def change_room_prices(self, new_price: float, room_type: str) -> None:
        """
        Updates the price for a specific type of room.

        :param new_price: The new price to be set.
        :param room_type: The type of room (e.g., single, double, suite).
        """
        print(f"Updated price of {room_type} rooms to {new_price}.")

    def add_new_employee(self, employee: "Employee") -> None:
        """
        Adds a new employee to the system.

        :param employee: The Employee object to be added.
        """
        print(f"New employee {employee} added to the system.")

    def remove_employee(self, employee_id: int) -> None:
        """
        Removes an employee from the system.

        :param employee_id: The ID of the employee to be removed.
        """
        print(f"Employee with ID {employee_id} has been removed.")

#Feedback Class
class Feedback:
    """
    Represents guest feedback with rating and comments, along with admin interactions.
    """

    all_feedbacks = []  # Stores all feedback instances for filtering and analysis

    def __init__(self, feedback_id: int, guest: "Guest", rating: int, comments: str):
        self.__feedback_id = feedback_id
        self.__guest = guest
        self.__rating = rating
        self.__comments = comments
        Feedback.all_feedbacks.append(self)  # Store feedback globally

    def submit_feedback(self, rating: int, comments: str) -> None:
        """Updates feedback rating and comments."""
        self.__rating = rating
        self.__comments = comments
        print(f"Feedback submitted: Rating {rating}, Comment: {comments}")

    def view_feedback(self) -> str:
        """Returns feedback details."""
        return f"Feedback ID: {self.__feedback_id}, Rating: {self.__rating}, Comments: {self.__comments}"

    @staticmethod
    def get_average_rating() -> float:
        """Calculates and returns the average rating from all feedbacks."""
        if not Feedback.all_feedbacks:
            return 0.0
        total_rating = sum(f.__rating for f in Feedback.all_feedbacks)
        return total_rating / len(Feedback.all_feedbacks)

    @staticmethod
    def filter_feedback_by_rating(min_rating: int) -> list:
        """Filters and returns feedback with ratings greater than or equal to min_rating."""
        return [f for f in Feedback.all_feedbacks if f.__rating >= min_rating]

    def edit_feedback(self, new_rating: int, new_comments: str) -> None:
        """Edits an existing feedback entry."""
        self.__rating = new_rating
        self.__comments = new_comments
        print(f"Feedback updated: Rating {new_rating}, Comment: {new_comments}")

    def delete_feedback(self) -> None:
        """Deletes a feedback entry."""
        Feedback.all_feedbacks.remove(self)
        print("Feedback deleted successfully.")

    @staticmethod
    def get_guest_feedback(guest_id: int) -> list:
        """Retrieves all feedback entries for a specific guest ID."""
        return [f for f in Feedback.all_feedbacks if f.__guest.get_id() == guest_id]

    def reply_to_feedback(self, admin: "Admin", response: str) -> None:
        """Allows an admin to reply to feedback."""
        print(f"Admin {admin.get_username()} replied to Feedback {self.__feedback_id}: {response}")

    @staticmethod
    def analyze_feedback_trends() -> dict:
        """Analyzes feedback trends and returns relevant data."""
        return {
            "Total Feedbacks": len(Feedback.all_feedbacks),
            "Average Rating": Feedback.get_average_rating(),
        }

