# PRODIGY_CS_03

.......................**"Check It" Password Strength Checker Tool**...............
This version of the "Check It" password strength checker tool is designed to be visually appealing and easy to use, while maintaining its functionality. It guides the user to create stronger passwords and ensures that they meet common security standards.

### **Check It Tool - Password Strength Checker**

**Overview**:
The **Check It** tool is a Python-based program that assesses the strength of a password entered by the user. It evaluates the password based on several security criteria, including length, use of uppercase and lowercase letters, numbers, and special characters. The tool provides clear feedback to help users improve their password strength.

**Key Features**:
1. **Password Strength Evaluation**:
   - The tool checks if the password meets the following criteria:
     - At least 8 characters long.
     - Contains at least one uppercase letter.
     - Contains at least one lowercase letter.
     - Contains at least one number.
     - Contains at least one special character (e.g., @, #, $, %, etc.).
   
2. **Strength Classification**:
   - Based on the number of criteria the password meets, it is classified as:
     - **Very Strong**: Meets all criteria.
     - **Moderate**: Meets most criteria but still has room for improvement.
     - **Weak**: Meets a few criteria.
     - **Very Weak**: Does not meet the basic security standards.
   
3. **Feedback for Improvement**:
   - If the password is weak or moderate, the tool provides specific feedback on how to improve it, e.g., adding a special character, using uppercase letters, etc.
   
4. **User-Friendly Interface**:
   - The tool includes an ASCII art header to make the user experience more engaging.
   - It also uses clean formatting, including separator lines, to organize the output for easy readability.

**How to Use**:
1. **Input a Password**: When the program runs, you will be prompted to enter a password.
2. **Strength Feedback**: The program evaluates the strength of the password and gives feedback.
3. **Suggested Improvements**: If the password is not strong, the program will suggest improvements, such as adding special characters or numbers.
4. **Final Password Strength Rating**: The program will give a strength rating (e.g., "Very Strong," "Weak") based on the password's compliance with the set criteria.

**How to Run**:
1. **Save the Code**: Save the Python script (`check it.py`).
2. **Run in Terminal**: Open the terminal or command prompt, navigate to the directory containing the file, and run the script using:
   ```bash
   python check it.py
   ```
3. **Enter Password**: Input a password when prompted, and receive an immediate strength evaluation along with feedback.

**Example Output**:
```bash
Password Strength: Weak
Feedback for improving your password:
- Password must contain at least one uppercase letter.
- Password must contain at least one special character (e.g., @, #, $, %, etc.).
```

**Conclusion**:
The **Check It** tool is a straightforward, user-friendly password strength checker that helps individuals create stronger, more secure passwords by assessing their compliance with common password security standards.

