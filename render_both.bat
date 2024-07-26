@echo off
echo Current directory: %CD%
call render_website.bat
call render_pdf.bat
call render_word.bat
