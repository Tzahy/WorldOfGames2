from selenium import webdriver
import sys


def test_scores_service(app_url):
    # load chromedriver as driver
    driver = webdriver.Chrome(executable_path="L:\\DevOps\\Python\\Downloads\\chromedriver.exe")
    # try to catch any errors in the following (e.g. get element text, wrong range number, score is NaN etc.)
    try:
        # load the page to the given url
        driver.get(app_url)
        # catch the element by its id
        element = driver.find_element_by_id('score')
        # split the text in the element to array so i can get the number
        text = element.text.split()
        # get the forth element of the text which is the number
        score = text[3]
        # check that the number & convert the string to int so we can use the range function
        if int(score) in range(0, 1001):
            # kill the browser and the driver process
            driver.quit()
            # test succeeded, return true and default exit status is 0
            return True
        else:
            # test fail return false
            return False
    except:
        # get any exceptions (this is why its bare except) and return exit status of -1
        return sys.exit(-1)


def main_function():
    # run the test function and get its status (True or False)
    test_succeed = test_scores_service("http://192.168.99.100:8777")
    # check the status and print the test results to the console
    if test_succeed:
        print("Test Pass!")
    else:
       exit 1


# run main function
main_function()

