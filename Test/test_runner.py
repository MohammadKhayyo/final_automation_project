from typing import Type
import unittest
from concurrent.futures import ThreadPoolExecutor
from infra.configurations import ConfigurationManager
from Test.parallel.parallel_tasks_tests import ParallelTasksTests
from Test.parallel.parallel_sprints_tests import ParallelSprintsTests
from Test.parallel.parallel_epics_tests import ParallelEpicsTests
from Test.parallel.parallel_login_tests import ParallelLoginTests
from Test.parallel.parallel_home_tests import ParallelHomeTests
from Test.parallel.parallel_bugs_queue_test import ParallelBugsQueueTests
from Test.parallel.parallel_retrospectives_page_test import ParallelRetrospectivesTests

from Test.non_parallel.serial_tasks_tests import SerialTasksTests
from Test.non_parallel.serial_sprints_tests import SerialSprintsTests
from Test.non_parallel.serial_epics_tests import SerialEpicsTests
from Test.non_parallel.serial_login_tests import SerialLoginTests
from Test.non_parallel.serial_home_tests import SerialHomeTests
from Test.non_parallel.serial_bugs_queue_tests import BugsQueuePage
from Test.non_parallel.serial_retrospectives_tests import RetrospectivesPage

# Grouping test cases
serial_test_groups = [SerialTasksTests, SerialSprintsTests, SerialEpicsTests, SerialLoginTests, SerialHomeTests,
                      BugsQueuePage, RetrospectivesPage]
parallel_test_groups = [ParallelTasksTests, ParallelSprintsTests, ParallelEpicsTests, ParallelLoginTests,
                        ParallelHomeTests, ParallelBugsQueueTests, ParallelRetrospectivesTests]
all_test_groups = serial_test_groups + parallel_test_groups

demo_test = [SerialHomeTests]


def execute_test_with_browser(browser_name: str, test_group: Type[unittest.TestCase]):
    test_group.browser = browser_name
    test_suite = unittest.TestLoader().loadTestsFromTestCase(test_group)
    unittest.TextTestRunner().run(test_suite)


def run_tests_for_browser_serial(browser_list, test_groups):
    for test in test_groups:
        for browser in browser_list:
            execute_test_with_browser(browser, test)


def run_tests_for_browser_parallel(browser_list, test_groups):
    task_list = [(browser, test_case) for browser in browser_list for test_case in test_groups]

    with ThreadPoolExecutor(max_workers=4) as executor:
        [executor.submit(execute_test_with_browser, browser, test) for browser, test in task_list]


if __name__ == "__main__":
    config_manager = ConfigurationManager()
    settings = config_manager.load_settings()
    is_parallel = settings['parallel']
    is_serial = not settings['parallel']
    browsers = settings["browser_types"]
    grid_url = settings["hub"]
    if is_parallel:
        # run_tests_for_browser_parallel(browsers, parallel_test_groups)
        # run_tests_for_browser_serial(browsers, serial_test_groups)
        run_tests_for_browser_serial(browsers, demo_test)
    elif is_serial:
        run_tests_for_browser_serial(browsers, all_test_groups)
