%global tl_name labels
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	13
Release:	%{tl_revision}.1
Summary:	Print sheets of sticky labels
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/labels
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/labels.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/labels.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/labels.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A LaTeX package to print a regular grid of ragged-right labels on a
page, suitable for sheets of labels which can be fed through a printer.
Macros are provided to allow easy input of names and addresses in a form
free of TeX markup. Equally useful is a feature for making multiple
copies of a single label, e.g., return address stickers to go with the
labels. Rows, columns, borders can all be specified to match the label
sheet being used.

