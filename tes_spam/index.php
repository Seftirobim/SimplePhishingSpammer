<?php
// Database connection details
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = 'db_tespython';

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die('Connection failed: ' . $conn->connect_error);
}

// Process form submission
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Get form data
    $email = $_POST['email'];
    $pass = $_POST['pass'];

    // Prepare and execute SQL query
    $sql = "INSERT INTO tb_user (username, password) VALUES ('$email', '$pass')";
    if ($conn->query($sql) === TRUE) {
        echo 'Form submitted successfully.';
    } else {
        echo 'Form submission failed: ' . $conn->error;
    }
}

// Close the database connection
$conn->close();
?>

<!DOCTYPE html>
<html>
<head>
    <title>Form Submission</title>
</head>
<body>
    <form method="POST" action="">
        <label for="username">Username:</label>
        <input type="text" name="email" required><br>

        <label for="password">Password:</label>
        <input type="password" name="pass" required><br>

        <input type="submit" value="Submit">
    </form>
</body>
</html>