# security-pipeline-polyakov-ap

Учебный репозиторий для курсовой работы студента **Поляков А. П.**.

Тема: создание security pipeline для GitHub. Акцент реализации: **контроль цепочки поставки GitHub Actions и запрет mutable tags**. Теоретический кейс: **CVE-2025-30066**, компрометация стороннего GitHub Action `tj-actions/changed-files` и риск использования изменяемых тегов в CI/CD.

## Что проверяет pipeline

- SAST: CodeQL и Bandit для Python-кода;
- SCA: `pip-audit` для зависимостей Python;
- workflow audit: `zizmor` для файлов GitHub Actions;
- secret scanning: `detect-secrets` и учебное Semgrep-правило;
- IaC/container: Trivy filesystem scan;
- отчеты сохраняются в artifacts GitHub Actions.

## Как запустить

1. Опубликуйте репозиторий на GitHub.
2. Откройте вкладку **Actions**.
3. Запустите workflow **Security pipeline - supply chain focus** через `workflow_dispatch` или сделайте push.
4. Проверьте artifacts: `security-reports-polyakov`.

## Ожидаемый учебный результат

Pipeline должен показать несколько демонстрационных finding: устаревшие зависимости, небезопасный вызов shell-команды, учебный псевдосекрет и предупреждения по Dockerfile. Все уязвимые фрагменты намеренно добавлены только для демонстрации работы security pipeline.
