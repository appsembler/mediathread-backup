./manage.py dumpdata --settings=settings_test --indent=4 > mediathread_main/fixtures/sample_course.json
./manage.py dumpdata --settings=settings_test --exclude contenttypes --exclude tagging --indent=4 > mediathread_main/fixtures/unittest_sample_course.json