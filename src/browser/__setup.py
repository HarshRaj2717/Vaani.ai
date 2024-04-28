from .setup_selenium import getDriver


def main():
    driver = getDriver()
    _ = input("Do your thing and press enter boi...")
    driver.quit()


if __name__ == "__main__":
    main()
