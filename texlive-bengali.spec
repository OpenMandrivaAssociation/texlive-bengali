Name:		texlive-bengali
Version:	55475
Release:	2
Summary:	Support for the Bengali language
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/bengali/pandey
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bengali.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is based on Velthuis' transliteration scheme, with
extensions to deal with the Bengali letters that are not in
Devanagari. The package also supports Assamese.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/bengali/bn.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnbanjon.mf
%{_texmfdistdir}/fonts/source/public/bengali/bndigit.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnjuk.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnkaar.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnlig.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnligtbl.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnmacro.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnmisc.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnpunct.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnr10.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnsl10.mf
%{_texmfdistdir}/fonts/source/public/bengali/bnswar.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnr10.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnsl10.mf
%{_texmfdistdir}/fonts/source/public/bengali/xbnsupp.mf
%{_texmfdistdir}/fonts/tfm/public/bengali/bnr10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/bnsl10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/xbnr10.tfm
%{_texmfdistdir}/fonts/tfm/public/bengali/xbnsl10.tfm
%{_texmfdistdir}/tex/latex/bengali/beng.sty
%{_texmfdistdir}/tex/latex/bengali/ubn.fd
%{_texmfdistdir}/tex/latex/bengali/ubnx.fd
%doc %{_texmfdistdir}/doc/fonts/bengali/README
%doc %{_texmfdistdir}/doc/fonts/bengali/bengdoc.bn
%doc %{_texmfdistdir}/doc/fonts/bengali/bengdoc.pdf
%doc %{_texmfdistdir}/doc/fonts/bengali/example.bn
%doc %{_texmfdistdir}/doc/fonts/bengali/example.pdf
%doc %{_texmfdistdir}/doc/fonts/bengali/manifest.txt
#- source
%doc %{_texmfdistdir}/source/latex/bengali/beng.c

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
