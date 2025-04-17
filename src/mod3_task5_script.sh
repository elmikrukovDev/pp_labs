PROGRAM_FILE="mod2/task7.py"
PYLINT_OUTPUT="pylint_report.json"

echo "Запуск статического анализатора pylint..."
pylint --output-format=json "$PROGRAM_FILE" > "$PYLINT_OUTPUT"
pylint_res=$?

if [[ $pylint_res -eq 0 ]]; then
    echo "Pylint OK"
else
    echo "Pylint not OK"
fi

cat "$PYLINT_OUTPUT"

echo "Запуск юнит-тестов..."
python3 -m unittest discover -s . -p "mod3_task3_tests_m2t7.py"
test_res=$?

if [[ $test_res -eq 0 && $pylint_res -eq 0 ]]; then
    echo "ОК"
else
    echo "Имеются ошибки"
fi

rm -f "$PYLINT_OUTPUT"