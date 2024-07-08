% -----------------------------------------------------------------------------
% LaTeX Class 'unicam_resume' - LaTeX class for composing MSc and BSc resume
% 
% Giorgio Saldana <giorgio.saldana@studenti.unicam.it>
% -----------------------------------------------------------------------------

% -----------------------------------------------------------------------------
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{unicam_resume}[2024/04/02 - LaTeX class for composing resume at 
                  University of Camerino - School of Science ant Technologies]
% -----------------------------------------------------------------------------

\newcommand{\@ptoption}{1pt}
\newcommand{\@tipo}{twoside}

\ExecuteOptions{oneside,12pt}
\ProcessOptions\relax
\typeout{*************************************************************************}
\typeout{****** Document Class 'unicam_resume' <April, 2 2024> *******************}
\typeout{****** Please report bugs, comments, suggestions, and improvements ******}
\typeout{****** to Giorgio Saldana <giorgio.saldana@studenti.unicam.it> ***********************}
% -----------------------------------------------------------------------------
% Load the book class for a4 paper dimension
% -----------------------------------------------------------------------------
\LoadClass[\@tipo,a4paper,1\@ptoption]{book}

% -----------------------------------------------------------------------------
% Load support packages
%
% Get the missing packages at ftp://ftp.dante.de/tex-archive
% -----------------------------------------------------------------------------

% set page geometry
\RequirePackage[top=3cm, bottom=3cm, inner=3.5cm, outer=3cm]{geometry}%

% italian character set
\RequirePackage[utf8]{inputenc}%

\RequirePackage{graphicx}%
\RequirePackage{makeidx}%
\RequirePackage{wrapfig}%
\RequirePackage[metapost]{mfpic}%
\RequirePackage{arydshln}%
\RequirePackage{amssymb}%
\RequirePackage{amsmath}%
\RequirePackage{amsthm}%
%\RequirePackage[pdftex,bookmarks=true,colorlinks=true,linkcolor=black]{hyperref}%
\RequirePackage[pdftex,bookmarks=true,hidelinks]{hyperref}
\RequirePackage{subfig}%
\RequirePackage{xspace}%
\RequirePackage{array}%
\RequirePackage{times}%
\RequirePackage{longtable}%
\RequirePackage{fancyhdr}%
\pagestyle{fancy}%

\setlength{\headheight}{15pt}
\renewcommand{\sectionmark}[1]{\markright{#1}{}} \fancyhf{}
\fancyhead[LE]{\textit{\nouppercase{\rightmark}}}
\fancyhead[RO]{\textit{\nouppercase{\rightmark}}}
\fancyfoot[LE,RO]{\thepage}

\fancypagestyle{plain}{ %
  \fancyhf{} %
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}%
}

% \RequirePackage{helvet}
\renewcommand{\familydefault}{\rmdefault}
\renewcommand{\rmdefault}{cmr}

% titoli in italiano
\renewcommand\figurename{Figura} \renewcommand\tablename{Tabella}
\renewcommand\contentsname{Indice}

% comando per TODO added later
\newcommand\todo[1]{\textcolor{red}{TODO: #1}}

\makeindex %
\date{} %

\RequirePackage[english]{varioref}
\RequirePackage[english]{babel}
\RequirePackage[babel]{csquotes}
\RequirePackage[style=numeric, sorting=none, maxbibnames=999, backend=biber]{biblatex}
\RequirePackage{colortbl}

\RequirePackage[final]{listings}
\definecolor{listingsBackground}{rgb}{0.9,0.9,0.9}
%****color terminal
\definecolor{mycomments}{rgb}{0.88,0.110,0.117}
\definecolor{mygray}{rgb}{0.5,0.5,0.5}
\definecolor{mymauve}{rgb}{0.58,0,0.82}
\definecolor{terminalbgcolor}{rgb}{0,0.43,0.54}
\definecolor{terminalrulecolor}{rgb}{0.131,0.148,0.150}
%*********

\lstdefinestyle{xmlCode}{language=XML,frame=tbrl,
  basicstyle=\scriptsize\ttfamily,keywordstyle=\ttfamily\bf,
  stringstyle=\itshape,flexiblecolumns=true,
  commentstyle=\itshape,captionpos=b,abovecaptionskip=10pt,belowcaptionskip=0pt,
  backgroundcolor=\color{listingsBackground}, frame=none
, numbers=left, numberstyle={\tiny }
}

\lstdefinelanguage{JavaScript}{
  keywords={typeof, new, true, false, catch, function, return, null, catch, switch, var, if, in, while, do, else, case, break},
  keywordstyle=\color{blue}\bfseries,
  ndkeywords={class, export, boolean, throw, implements, import, this},
  sensitive=false,
  comment=[l]{//},
  morecomment=[s]{/*}{*/},
  morestring=[b]',
  morestring=[b]"
}
\lstdefinestyle{javaScriptCode}{language=JavaScript,frame=tbrl,
  basicstyle=\scriptsize\ttfamily,keywordstyle=\ttfamily\bf,
  stringstyle=\itshape,flexiblecolumns=true,
  commentstyle=\itshape,captionpos=b,abovecaptionskip=10pt,belowcaptionskip=0pt,
  backgroundcolor=\color{listingsBackground}, frame=none, 
  numbers=left, numberstyle={\tiny }
}
\lstdefinestyle{javaCode}{language=Java,frame=tbrl,
  basicstyle=\scriptsize\ttfamily,keywordstyle=\ttfamily\bf,
  stringstyle=\itshape,flexiblecolumns=true,
  commentstyle=\itshape,captionpos=b,abovecaptionskip=10pt,belowcaptionskip=0pt,
  backgroundcolor=\color{listingsBackground}, frame=none, 
  numbers=left, numberstyle={\tiny }
}

%-------------------------------
%------Code for emulate terminal

%\newcommand{\lstconsolestyle}{
%    \lstset{
    	%backgroundcolor=\color{terminalbgcolor},
    	%basicstyle=\color{white}\fontfamily{fvm}\footnotesize\selectfont,
    	%breakatwhitespace=false,  
    	%breaklines=true,
    	%captionpos=b,
    	%commentstyle=\color{mycomments},
    	%deletekeywords={...},
    	%escapeinside={\%*}{*)},
    	%extendedchars=true,
    	%frame=single,
    	%keepspaces=true,
    	%keywordstyle=\color{blue},
    	%language=none,
    	%morekeywords={*,...},
    	%numbers=none,
    	%numbersep=5pt,
            %framerule=1pt,
    	%numberstyle=\color{mygray}\tiny\selectfont,
    	%rulecolor=\color{terminalrulecolor},
            %showlines=false,
    	%showspaces=false,
    	%showstringspaces=false,
    	%showtabs=false,
    	%stepnumber=2,
    	%stringstyle=\color{mymauve},
    	%tabsize=2
%    }
%}
\lstdefinestyle{bashCode}{
    language=Bash,
    frame=tbrl,
    basicstyle=\scriptsize\ttfamily,
    showstringspaces=false,
    commentstyle=\color{red},
    keywordstyle=\color{blue}
}

\addto\captionsitalian{
\renewcommand{\lstlistingname}{Codice}}

\addto\captionsitalian{
\renewcommand{\lstlistlistingname}{Elenco dei codici}}

% ---------------------------------------------------------------------------
% --- Numbering
% ---------------------------------------------------------------------------
%\setcounter{secnumdepth}{1}

% ---------------------------------------------------------------------------
% --- Empty pages...
% ---------------------------------------------------------------------------

\let\origdoublepage\cleardoublepage
%\newcommand{\clearemptydoublepage}{%
%  \clearpage
%  {\pagestyle{empty}\origdoublepage}%
%}
%\let\cleardoublepage\clearemptydoublepage
\renewcommand{\cleardoublepage}{\clearpage}

\newcommand{\mychaptertitlefont}{\fontseries{s}\fontsize{20}{24}\selectfont}
\newcommand{\mytitlefont}{\fontseries{b}\sc\fontsize{15}{24}\selectfont}
\newcommand{\mysubtitlefont}{\fontseries{s}\fontsize{13}{16}\selectfont}
\newcommand{\authorfont}{\fontseries{s}\fontsize{14}{14}\selectfont}
\newcommand{\largefont}{\fontseries{s}\fontsize{18}{14}\selectfont}
\newcommand{\bigfont}{\fontseries{s}\fontsize{20}{14}\selectfont}
\newcommand{\biggerfont}{\fontseries{s}\fontsize{26}{22}\selectfont}

\def\author#1{\gdef\@theauthor{#1}}
\def\coauthor#1{\gdef\@thecoauthor{#1}}
\def\cocoauthor#1{\gdef\@thecocoauthor{#1}}
\def\university#1{\gdef\@theuniversity{#1}}
\def\school#1{\gdef\@theschool{#1}}
\def\course#1{\gdef\@thecourse{#1}}
\def\academicyear#1{\gdef\@theacademicyear{#1}}
\def\matricola#1{\gdef\@thematricola{#1}}

\def\title#1{\gdef\@thetitle{#1}}
\def\subtitle#1{\gdef\@thesubtitle{#1}}

\def\deliverabletype#1{\gdef\@thedeliverabletype{#1}}
\def\deliverableno#1{\gdef\@thedeliverableno{#1}}
\def\naturedeliverable#1{\gdef\@thenaturedeliverable{#1}}
\def\disseminationlevel#1{\gdef\@thedisseminationlevel{#1}}
\def\internalno#1{\gdef\@theinternalno{#1}}
\def\contractualdeliverydate#1{\gdef\@thecontractualdeliverydate{#1}}
\def\actualdeliverydate#1{\gdef\@theactualdeliverydate{#1}}
\def\contributingwp#1{\gdef\@thecontributingwp{#1}}
\def\editors#1{\gdef\@theeditors{#1}}
\def\reviewers#1{\gdef\@thereviewers{#1}}

\def\@theauthors{}
\def\@thetitle{}
\def\@thesubtitle{}

\newcommand{\HRule}{\rule{\linewidth}{0pt}}

\renewcommand{\maketitle}{%
\thispagestyle{empty}
%\enlargethispage{4\baselineskip}
\setlength{\parindent}{0mm}
\setlength{\parskip}{0mm}

\begin{center}
  \includegraphics[width=15mm]{Images/unicam.png}\par%
  \vspace{0.15cm}%
  {\rmfamily \Large \bfseries \@theuniversity \par}%
  \vspace{0.15cm}%
  \hrule%
  \vspace{0.15cm}%
  {\rmfamily \Large \scshape School of \@theschool \par}%
  \vspace{0.15cm}%
  {\rmfamily \large \@thecourse \par}%
  \vspace{0.5cm}%
  \vspace*{\stretch{2}}%
  \vspace*{\stretch{3}}%
  {\rmfamily \LARGE \bfseries \@thetitle \par}%
  \vspace*{\stretch{3}}%
  {\rmfamily \Large \scshape  Student \par}%
  \vspace*{\stretch{0.5}}%
  {\bfseries \large \@theauthor \par}%
  \vspace*{\stretch{7}}%
  \hrule%
  \vspace{0.15cm}%
  {\large A.A. \@theacademicyear}%
\end{center}

\newpage
\setlength{\parindent}{1em}
\setlength{\parskip}{2pt}
\cleardoublepage
}

% ---------------------------------------------------------------------------
%    Headers
% ---------------------------------------------------------------------------
\pagestyle{fancy}

% ---------------------------------------------------------------------------
% --- MISC COMMANDS
% ---------------------------------------------------------------------------

\def\date#1{\gdef\@thedate{#1}}

% \newcommand{\comment}[2]{}
\newcommand{\comment}[2]{\marginpar{\textcolor{red}{\ding{74}}}\footnote{\textcolor{red}{\it\scriptsize {\textbf{\sf \underline{#1}:~}#2}}}}



\newcommand{\abstract}[1]{
\newpage
\noindent
\fbox{\parbox{.98\linewidth}{
\vspace{-5mm}
\section*{Abstract}
\par
#1
}}\\[1cm]}
\newcommand{\keywords}[1]{
\noindent\fbox{\parbox{.98\linewidth}{
\vspace{-5mm}
\section*{Keyword List }
\par
#1
}}
}

\setlength{\baselineskip}{17pt}

\newcommand{\historyitem}[3]{
#1 & #2 & #3 \\ \hline
}
\newenvironment{history}
{
\newpage
\section*{Document History}
\begin{tabular}{|p{20mm}|p{82mm}|p{40mm}|}
\hline 
\textbf{Version} &  \textbf{Type of change}  & \textbf{Author(s)} \\
\hline
}
{
\end{tabular}
}
\newcommand{\reviewitem}[4]{
#1 & #2 & #3 & #4 \\ \hline
}
\newenvironment{review}
{
\newpage
\section*{Document Reviews}
\begin{tabular}{|p{22mm}|p{20mm}|p{33mm}|p{63mm}|}
\hline 
\textbf{Date} & \textbf{Version} & \textbf{Reviewer} & \textbf{Comment} \\
\hline
}
{
\end{tabular}
}
\newcommand{\acronym}[2]{
#1 & #2 \\ \hline
}
\newenvironment{acronyms}
{
\newpage
\chapter*{Table of Acronyms}
\addcontentsline{toc}{chapter}{Table of Acronyms}
\begin{tabular}{|>{\centering}p{41mm}|p{106mm}|}
\hline
\textbf{Acronym} & \textbf{Expanded Version} \\
\hline
}
{
\end{tabular}
}



\renewcommand\chapter{\if@openright\cleardoublepage\else\clearpage\fi
                    \thispagestyle{plain}%
                    \global\@topnum\z@
                    \@afterindentfalse
                    \secdef\@chapter\@schapter}
\def\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
                       \if@mainmatter
                         \refstepcounter{chapter}%
                         \typeout{\@chapapp\space\thechapter.}%
                         \addcontentsline{toc}{chapter}%
                                   {\protect\numberline{\thechapter}#1}%
                       \else
                         \addcontentsline{toc}{chapter}{#1}%
                       \fi
                    \else
                      \addcontentsline{toc}{chapter}{#1}%
                    \fi
                    \chaptermark{#1}%
                    \addtocontents{lof}{\protect\addvspace{10\p@}}%
                    \addtocontents{lot}{\protect\addvspace{10\p@}}%
                    \if@twocolumn
                      \@topnewpage[\@makechapterhead{#2}]%
                    \else
                      \@makechapterhead{#2}%
                      \@afterheading
                    \fi}

\def\@makechapterhead#1{%
  \vspace*{50\p@}%
  {\parindent \z@ \raggedright \normalfont 
    \ifnum \c@secnumdepth >\m@ne
      \if@mainmatter
        \Huge \bfseries % \@chapapp\space
         \thechapter .  #1\par\nobreak
%        \par\nobreak
%        \vskip 20\p@
%      \fi
%    \fi
%    \interlinepenalty\@M
%    \Huge \bfseries #1\par\nobreak
    \vskip 40\p@
  }}
\def\@schapter#1{\if@twocolumn
                   \@topnewpage[\@makeschapterhead{#1}]%
                 \else
                   \@makeschapterhead{#1}%
                   \@afterheading
                 \fi}
\def\@makeschapterhead#1{%
  \vspace*{50\p@}%
  {\parindent \z@ \raggedright
    \normalfont
    \interlinepenalty\@M
    \Huge \bfseries  #1\par\nobreak
    \vskip 40\p@
  }}

  