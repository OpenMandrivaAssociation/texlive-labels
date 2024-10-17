Name:		texlive-labels
Version:	15878
Release:	2
Summary:	Print sheets of sticky labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/labels
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labels.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labels.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/labels.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A LaTeX package to print a regular grid of ragged-right labels
on a page, suitable for sheets of labels which can be fed
through a printer. Macros are provided to allow easy input of
names and addresses in a form free of TeX markup. Equally
useful is a feature for making multiple copies of a single
label, e.g., return address stickers to go with the labels.
Rows, columns, borders can all be specified to match the label
sheet being used.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/labels/labels.sty
%{_texmfdistdir}/tex/latex/labels/olabels.sty
%doc %{_texmfdistdir}/doc/latex/labels/README
%doc %{_texmfdistdir}/doc/latex/labels/labels.pdf
%doc %{_texmfdistdir}/doc/latex/labels/test/avery5162.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/badge.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/beebe.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/door.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/door209.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/names.dat
%doc %{_texmfdistdir}/doc/latex/labels/test/news.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test1.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test10.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test11.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test12.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test2.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test3.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test4.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test5.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test6.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test7.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test8.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/test9.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew1.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew10.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew11.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew12.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew13.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew2.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew3.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew4.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew5.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew6.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew7.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew8.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/testnew9.tex
%doc %{_texmfdistdir}/doc/latex/labels/test/zwekform.tex
#- source
%doc %{_texmfdistdir}/source/latex/labels/labels.dtx
%doc %{_texmfdistdir}/source/latex/labels/labels.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
