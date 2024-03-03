from typing import Type
import unittest
from concurrent.futures import ThreadPoolExecutor
from infra.config_loader import ConfigLoader
from Test.parallel.parallel_tasks_page_test import ParallelTasksPageTests
from Test.parallel.parallel_sprints_page_test import ParallelSprintPageTests
from Test.parallel.parallel_epics_page_test import ParallelEpicsPageTests
from Test.parallel.parallel_login_test import ParallelLoginPageTests
# from Test.parallel.parallel_home_page_test import ParallelHomePageTests

from Test.non_parallel.non_parallel_tasks_page_test import NonParallelTasksPageTests
from Test.non_parallel.non_parallel_sprints_page_test import NonParallelSprintPageTests
from Test.non_parallel.non_parallel_epics_page_test import NonParallelEpicsPageTests
# from Test.non_parallel.non_parallel_login_test import NonParallelLoginPageTests
from Test.non_parallel.non_parallel_home_page_test import NonParallelHomePageTests

# [LoginPageTests, HomePageTests, TasksPageTests, SprintPageTests, EpicsPageTests]


serial_cases = [NonParallelEpicsPageTests]
parallel_cases = [ParallelEpicsPageTests]
test_cases = [NonParallelEpicsPageTests, ParallelEpicsPageTests]


# serial_cases = [NonParallelTasksPageTests, NonParallelSprintPageTests, NonParallelEpicsPageTests,
#                 NonParallelHomePageTests]
# parallel_cases = [ParallelTasksPageTests, ParallelSprintPageTests, ParallelEpicsPageTests, ParallelLoginPageTests]
# test_cases = [NonParallelTasksPageTests, NonParallelSprintPageTests, NonParallelEpicsPageTests,
#               NonParallelHomePageTests, ParallelTasksPageTests, ParallelSprintPageTests,
#               ParallelEpicsPageTests, ParallelLoginPageTests]


def run_tests_for_browser(browser: str, test_case: Type[unittest.TestCase]):
    test_case.browser = browser
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
    unittest.TextTestRunner().run(test_suite)


def run_tests_for_browser_serial(browsers, serial_tests):
    for test in serial_tests:
        for browser in browsers:
            run_tests_for_browser(browser, test)


def run_tests_for_browser_parallel(browsers, parallel_tests):
    tasks = [(browser, test_case) for browser in browsers for test_case in parallel_tests]

    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(run_tests_for_browser, browser, test_case) for browser, test_case in tasks]

    # for test_case in parallel_tests:
    #     with ThreadPoolExecutor(max_workers=len(_browsers)) as executor:
    #         futures = list()
    #         for _browser in _browsers:
    #             test_case.browser = _browser
    #             future = executor.submit(run_tests_for_browser, _browser, test_case)
    #             futures.append(future)
    #
    #         for future in concurrent.futures.as_completed(futures):
    #             try:
    #                 future.result()
    #             except Exception as e:
    #                 logging.error(f"An error occurred during the tests: {e}")

    # with ThreadPoolExecutor(max_workers=len(_browsers)) as executor:
    #     futures = []
    #     for test_case in parallel_tests:
    #         for _browser in _browsers:
    #             future = executor.submit(run_tests_for_browser, _browser, test_case)
    #             futures.append(future)
    #
    #     for future in concurrent.futures.as_completed(futures):
    #         try:
    #             future.result()
    #         except Exception as e:
    #             logging.error(f"An error occurred during the tests: {e}")


# def dived_tests_parallel_non_parallel(test_cases):
#     for test_case in test_cases:
#         if hasattr(test_case, '_non_parallel') and getattr(test_case, '_non_parallel'):
#             serial_cases.append(test_case)
#         else:
#             parallel_cases.append(test_case)


if __name__ == "__main__":
    config_loader = ConfigLoader()
    config = config_loader.load_config()
    is_parallel = config['parallel']
    is_serial = not config['parallel']
    browsers = config["browser_types"]
    grid_url = config["hub"]
    if is_parallel:
        # run_tests_for_browser_parallel(browsers, parallel_cases)
        run_tests_for_browser_serial(browsers, serial_cases)
        # dived_tests_parallel_non_parallel(test_cases)
        # run_tests_for_browser_parallel(browsers, parallel_cases)
        # run_tests_for_browser_serial(browsers, serial_cases)
    elif is_serial:
        run_tests_for_browser_serial(browsers, test_cases)
    # else:
    #     browser = config["browser"]
    #     for test in test_cases:
    #         test.browser = browser
    #         run_tests_for_browser(browser, test)
