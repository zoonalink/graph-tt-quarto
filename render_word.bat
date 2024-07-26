@echo off
echo Current directory: %CD%
copy /Y "_ignore_word.yml" "_quarto.yml" > nul
if %errorlevel% neq 0 (
    echo Error: Failed to copy _ignore_quarto_word.yml
    exit /b 1
) else (
    echo Copy completed successfully!
)
quarto render --to docx
