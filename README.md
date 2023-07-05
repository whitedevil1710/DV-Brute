# DV-Brute
DV-Brute is a Python script for performing login scans using a configured set of options. It allows you to set the target URL, load usernames and passwords from files, set parameters for POST requests, and perform the scan.

## Prerequisites

- certifi
- charset-normalizer
- idna
- requests
- termcolor
- urllib3

## Installation
Clone the DV-Brute repository from GitHub:
```
git clone https://github.com/whitedevil1710/DV-Brute.git
```
Install the required dependencies:
```
pip install -r requirements.txt
```
## Usage
Run the script as root:
```
sudo python dv_brute.py
```
Once the script is running, you can use the following commands:
  - set_url <url>: Set the target URL for the login page.
  - set_user <username or filename>: Set the username or load usernames from a file.
  - set_pass <password filename>: Set the password file.
  - set_param_user <post parameter>: Set the parameter for the username in POST requests.
  - set_param_pass <password parameter>: Set the parameter for the password in POST requests.
  - count_pass: Count the number of passwords loaded.
  - print_users: Print the loaded usernames.
  - options: Display the current configuration options.
  - scan: Perform a login scan using the configured options.
  - add_pass <password>: Add a password to the loaded password list.
  - clear_pass: Clear the loaded password list.
  - clear_user: Clear the loaded username list.
  - cls: Clear all the configuration options and loaded data.
  - restart: Restart the script.
  - quit or exit: Quit the script.

Follow the instructions provided by the script to configure the necessary parameters and perform the bruteforce attack.

## Example

Here is an example scenario using DV-Brute:

Set the target URL:
```
set_url http://example.com/login
```
Set the username parameter:
```
set_param_user username
```
Set the password parameter:
```
set_param_pass password
```
Set the username:
```
set_user admin
```
Set the password file:
```
set_pass passwords.txt
```
Run the scan:
```
scan
```
DV-Brute will iterate through the list of usernames and passwords, sending POST requests to the target URL. If a successful login attempt is detected, it will be displayed.

## Disclaimer

### Usage of DV-Brute for attacking targets without prior mutual consent is illegal. It is the user's responsibility to obey all applicable local, state, and federal laws. The author assumes no liability and is not responsible for any misuse or damage caused by this tool.

## Author

DV-Brute is coded by [whitedevil](https://github.com/whitedevil1710/).
