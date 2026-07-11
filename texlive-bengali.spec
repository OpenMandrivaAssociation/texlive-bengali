%global tl_name bengali
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Support for the Bengali language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/bengali/pandey
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is based on Velthuis' transliteration scheme, with
extensions to deal with the Bengali letters that are not in Devanagari.
The package also supports Assamese.

