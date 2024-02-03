0. Parameterize a unit test
mandatory
Familiarize yourself with the utils.access_nested_map function and understand its purpose. Play with it in the Python console to make sure you understand.
In this task you will write the first unit test for utils.access_nested_map.
Create a TestAccessNestedMap class that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method to test that the method returns what it is supposed to.
2. Mock HTTP calls
mandatory
Familiarize yourself with the utils.get_json function.
Define the TestGetJson(unittest.TestCase) class and implement the TestGetJson.test_get_json method to test that utils.get_json returns the expected result.
We don’t want to make any actual external HTTP calls. Use unittest.mock.patch to patch requests.get. Make sure it returns a Mock object with a json method that returns test_payload which you parametrize alongside the test_url that you will pass to get_json with the following inputs
3. Parameterize and patch
mandatory
Read about memoization and familiarize yourself with the utils.memoize decorator.
Implement the TestMemoize(unittest.TestCase) class with a test_memoize method.
Inside test_memoize, define following class
4. Parameterize and patch as decorators
mandatory
Familiarize yourself with the client.GithubOrgClient class.
In a new test_client.py file, declare the TestGithubOrgClient(unittest.TestCase) class and implement the test_org method.
This method should test that GithubOrgClient.org returns the correct value.
Use @patch as a decorator to make sure get_json is called once with the expected argument but make sure it is not executed.
Use @parameterized.expand as a decorator to parametrize the test with a couple of org examples to pass to GithubOrgClient, in this order:
google
abc
Of course, no external HTTP calls should be made.
5. Mocking a property
mandatory
memoize turns methods into properties. Read up on how to mock a property (see resource).
Implement the test_public_repos_url method to unit-test GithubOrgClient._public_repos_url.
Use patch as a context manager to patch GithubOrgClient.org and make it return a known payload.
Test that the result of _public_repos_url is the expected one based on the mocked payload.
6. More patching
mandatory
Implement TestGithubOrgClient.test_public_repos to unit-test GithubOrgClient.public_repos.
Use @patch as a decorator to mock get_json and make it return a payload of your choice.
Use patch as a context manager to mock GithubOrgClient._public_repos_url and return a value of your choice.
Test that the list of repos is what you expect from the chosen payload.
Test that the mocked property and the mocked get_json was called once.
7. Parameterize
mandatory
Implement TestGithubOrgClient.test_has_license to unit-test GithubOrgClient.has_license.
8. Integration test: fixtures
mandatory
We want to test the GithubOrgClient.public_repos method in an integration test. That means that we will only mock code that sends external requests.
Create the TestIntegrationGithubOrgClient(unittest.TestCase) class and implement the setUpClass and tearDownClass which are part of the unittest.TestCase API.
9. Integration tests
#advanced
Implement the test_public_repos method to test GithubOrgClient.public_repos.
Make sure that the method returns the expected results based on the fixtures.
Implement test_public_repos_with_license to test the public_repos with the argument license="apache-2.0" and make sure the result matches the expected value from the fixtures.
