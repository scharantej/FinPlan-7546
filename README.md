## Flask Application Design

### HTML Files

1. **index.html**: The main HTML file, responsible for the home page of the web-app.
   - Content:
     - A form for creating financial goals and adding transactions.
     - A table displaying the current financial plan.

2. **success.html**: A confirmation page displayed after successfully creating a financial goal or adding a transaction.
   - Content:
     - A success message indicating the success of the operation.

3. **failure.html**: An error page displayed if any errors occur during financial goal creation or transaction addition.
   - Content:
     - An error message explaining the error.

### Routes

1. **Homepage**: The default route, displaying the index.html file.

2. **Create Goal**: A POST route that handles the creation of a new financial goal.
   - Accepts a form submission with the goal details.
   - Validates the input and creates a new goal in the database.
   - Redirects to success.html on success, or failure.html on error.

3. **Add Transaction**: A POST route that handles the addition of a new transaction.
   - Accepts a form submission with the transaction details.
   - Validates the input and adds a new transaction to the database.
   - Redirects to success.html on success, or failure.html on error.

4. **View Plan**: A route that displays the current financial plan in a table format.
   - Retrieves the financial goals and transactions from the database.
   - Generates an HTML table with the data and displays it.