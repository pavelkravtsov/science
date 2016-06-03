cd %~dp0
pdflatex ./diplom.tex > nul
pdflatex ./diplom.tex > nul
cd ./src/
python3 correlation.bat
cd ../presentation/
call ./presentation/make.bat