@echo off
ren _quarto.yml _quarto_website.yml
ren ignore_pdf.yml _quarto.yml

quarto render --to pdf

ren _quarto.yml ignore_pdf.yml
ren _quarto_website.yml _quarto.yml
