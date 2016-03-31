\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{recipe}[1996/11/22 MLO recipe class v0.9]

%Cette classe est une modification de la classe recipie
%faite par :
% Author: Maurizio Loreti, aka MLO or (HAM) I3NOO
% Work:   University of Padova - Department of Physics
%         Via F. Marzolo, 8 - 35131 PADOVA - Italy
% Phone:  ++39(49) 827-7216     FAX: ++39(49) 827-7102
% EMail:  loreti@padova.infn.it
% WWW:    http://mvxpd5.pd.infn.it/wwwcdf/mlo.html

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{book}}
\ProcessOptions
\LoadClass[10pt,twoside,openright]{book}
\usepackage[a5paper,top=1cm, bottom=1.25cm, left=1.25cm, right=1.25cm]{geometry}



%\usepackage{vmargin}
%\usepackage{manfnt}
\usepackage{stmaryrd} % pour les ingrédient
%\setmarginsrb{2.5cm}{2cm}{2cm}{2cm}{10mm}{6mm}{0cm}{10mm}
\usepackage{color}
\usepackage{marvosym}
\usepackage{multicol} % Pour les deux colonnes dans les ingrédients

%\pagestyle{empty}


\setcounter{secnumdepth}{2}	% subsubsections not numbered
\setcounter{tocdepth}{3}	% subsubsections in the .toc file


%%%%%%%%%%%%%% Accès rapide à certaines commandes %%%%%%%%%%%%%%%%%%%%%%
\newcommand{\puces}{$~~\leftslice$}
%\newcommand{\lpage}{15cm}
%\newcommand{\hpage}{15cm}
%\newcommand{\niveaugris}{.90}
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%\definecolor{gris}{gray}{\niveaugris}
\newcommand{\rechead}
    {\centering\normalfont\Large\sffamily\bfseries}

\newcommand{\bsi}[2]{\fontsize{#1}{#2}\usefont{T1}{pbsi}{xl}{n}}
\renewcommand{\rechead}{\centering\bsi{24pt}{30pt}}

\renewcommand{\subsection}
    {\@startsection{subsubsection}{3}{\z@}%
    {-5ex\@plus -1ex \@minus -.2ex}%
    {1.5ex \@plus .2ex}%
    {\rechead}}

\newcommand{\recette}[1]{\subsection{#1}%
    \vspace{.1cm}
    \hrule height0.75pt width\hsize\vspace*{1\p@}%
    \hrule height0.25pt width\hsize%
    \nobreak
    \vskip\parskip \vspace{.3cm}}

%\newcommand{\inghead}{\relax}

\newcommand{\otor}[1]
    {{\list{}{\rightmargin 1em\leftmargin 1em}%
\item[]\textit{\textbf{\huge \WritingHand \normalsize Auteur} : #1} \endlist}%
    \vspace{.2cm}\hrule height0.25pt width\hsize \vspace{.2cm}}

\newcommand{\ingredients}[2][]
    {{\list{}{\rightmargin 1em\leftmargin 1em}%
    \item[]\textit{\textbf{Ingr\'edients #1}: \vspace{-.3cm}\begin{multicols}{2}\begin{itemize}\renewcommand{\labelitemi}{\puces} #2 \end{itemize}\end{multicols}}\endlist}%
    \vspace{.2cm} \hrule height0.25pt width\hsize \vspace{.3cm}}

    
\newcommand{\degrees}{$^\circ$}
%\newcommand{\attention}[1]{\vspace{.3cm} \textdbend ~~ #1}