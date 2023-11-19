def login(username, password):
    # Locate the input fields for the username and password
    username_input = driver.find_element_by_name("username")
    password_input = driver.find_element_by_name("password")

    # Send the username and password to the input fields
    username_input.send_keys(username)
    password_input.send_keys(password)

    # Locate the submit button and click on it
    submit_button = driver.find_element_by_css_selector('button[type="submit"]')
    submit_button.click()

    # Locate the "Not Now" button and click on it to dismiss the notification prompt
    not_now_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'button.sqdOP.yWX7d.y3zKF'))))
    not_now_button.click()