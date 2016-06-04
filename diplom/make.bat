cd %~dp0
cd ./src/
python correlations.py
cd ../
pdflatex ./diplom.tex > nul
pdflatex ./diplom.tex > nul
cd ./presentation/
call ./make.bat
cd ../
texworks ./diplom.pdf ./presentation/presentation.pdf ./presentation/text.pdf