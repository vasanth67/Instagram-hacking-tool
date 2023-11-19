def clone_account(username):
    # Navigate to the profile page of the account to be cloned
    driver.get(f"https://www.instagram.com/{username}/")

    # Click on the "Follow" button if it exists, indicating that the user is not yet following the account
    try:
        follow_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'button.sqdOP.L3NKy.y3zKF'))))
        follow_button.click()
    except Exception as e:
        print(f"Could not follow the account. Reason: {e}")