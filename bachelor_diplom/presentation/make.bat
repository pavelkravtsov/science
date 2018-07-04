cd %~dp0
pdflatex ./presentation.tex 1> nul
pdflatex ./presentation.tex 1> nul
call ./do_jpeg.bat
pdflatex ./text.tex 1> nul
